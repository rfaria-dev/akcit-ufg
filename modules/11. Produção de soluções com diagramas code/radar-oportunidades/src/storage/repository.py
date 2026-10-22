"""Operações do Armazenamento.

Único ponto de acesso ao SQLite: os demais containers usam estas funções
e nunca tocam o banco diretamente. As funções não fazem commit — o chamador
controla a transação.
"""

import json
import sqlite3
from datetime import datetime, timezone
from typing import Any

from .models import Ativo, DadoBruto, Indicador, ItemRanking, Ranking

TIPOS_BRUTOS = ("cotacao", "fundamento", "provento")
STATUS_RANKING = ("atualizado", "desatualizado")


def _agora() -> str:
    return datetime.now(timezone.utc).isoformat()


def upsert_ativo(conn: sqlite3.Connection, ticker: str, nome: str, setor: str) -> None:
    conn.execute(
        "INSERT INTO ativos (ticker, nome, setor) VALUES (?, ?, ?) "
        "ON CONFLICT(ticker) DO UPDATE SET nome = excluded.nome, setor = excluded.setor",
        (ticker, nome, setor),
    )


def ler_ativos(conn: sqlite3.Connection, setor: str | None = None) -> list[Ativo]:
    if setor is None:
        linhas = conn.execute("SELECT ticker, nome, setor FROM ativos ORDER BY ticker").fetchall()
    else:
        linhas = conn.execute(
            "SELECT ticker, nome, setor FROM ativos WHERE setor = ? ORDER BY ticker", (setor,)
        ).fetchall()
    return [Ativo(ticker=r["ticker"], nome=r["nome"], setor=r["setor"]) for r in linhas]


def gravar_bruto(
    conn: sqlite3.Connection,
    ticker: str,
    tipo: str,
    data_referencia: str,
    payload: dict[str, Any],
) -> None:
    if tipo not in TIPOS_BRUTOS:
        raise ValueError(f"tipo inválido: {tipo!r}; esperado um de {TIPOS_BRUTOS}")
    conn.execute(
        "INSERT INTO dados_brutos (ticker, tipo, data_referencia, payload, coletado_em) "
        "VALUES (?, ?, ?, ?, ?) "
        "ON CONFLICT(ticker, tipo, data_referencia) DO UPDATE SET "
        "payload = excluded.payload, coletado_em = excluded.coletado_em",
        (ticker, tipo, data_referencia, json.dumps(payload), _agora()),
    )


def ler_brutos(
    conn: sqlite3.Connection,
    data_referencia: str | None = None,
    tipo: str | None = None,
) -> list[DadoBruto]:
    sql = "SELECT ticker, tipo, data_referencia, payload, coletado_em FROM dados_brutos"
    condicoes: list[str] = []
    params: list[Any] = []
    if data_referencia is not None:
        condicoes.append("data_referencia = ?")
        params.append(data_referencia)
    if tipo is not None:
        condicoes.append("tipo = ?")
        params.append(tipo)
    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)
    sql += " ORDER BY ticker, tipo"
    linhas = conn.execute(sql, params).fetchall()
    return [
        DadoBruto(
            ticker=r["ticker"],
            tipo=r["tipo"],
            data_referencia=r["data_referencia"],
            payload=json.loads(r["payload"]),
            coletado_em=r["coletado_em"],
        )
        for r in linhas
    ]


def gravar_indicador(
    conn: sqlite3.Connection,
    ticker: str,
    data_referencia: str,
    indicador: str,
    valor: float,
) -> None:
    conn.execute(
        "INSERT INTO indicadores (ticker, data_referencia, indicador, valor) VALUES (?, ?, ?, ?) "
        "ON CONFLICT(ticker, indicador, data_referencia) DO UPDATE SET valor = excluded.valor",
        (ticker, data_referencia, indicador, valor),
    )


def ler_indicadores(
    conn: sqlite3.Connection, data_referencia: str | None = None
) -> list[Indicador]:
    if data_referencia is None:
        linhas = conn.execute(
            "SELECT ticker, data_referencia, indicador, valor FROM indicadores "
            "ORDER BY ticker, indicador"
        ).fetchall()
    else:
        linhas = conn.execute(
            "SELECT ticker, data_referencia, indicador, valor FROM indicadores "
            "WHERE data_referencia = ? ORDER BY ticker, indicador",
            (data_referencia,),
        ).fetchall()
    return [
        Indicador(
            ticker=r["ticker"],
            data_referencia=r["data_referencia"],
            indicador=r["indicador"],
            valor=r["valor"],
        )
        for r in linhas
    ]


def gravar_ranking(
    conn: sqlite3.Connection,
    data_referencia: str,
    status: str,
    itens: list[tuple[int, str, float, list[dict[str, Any]]]],
) -> int:
    """Grava um snapshot de ranking e seus itens; retorna o id do snapshot."""
    if status not in STATUS_RANKING:
        raise ValueError(f"status inválido: {status!r}; esperado um de {STATUS_RANKING}")
    cursor = conn.execute(
        "INSERT INTO rankings (data_referencia, status, calculado_em) VALUES (?, ?, ?)",
        (data_referencia, status, _agora()),
    )
    ranking_id = cursor.lastrowid
    for posicao, ticker, score, contribuicoes in itens:
        conn.execute(
            "INSERT INTO ranking_itens (ranking_id, posicao, ticker, score, contribuicoes) "
            "VALUES (?, ?, ?, ?, ?)",
            (ranking_id, posicao, ticker, score, json.dumps(contribuicoes)),
        )
    return ranking_id


def ler_ranking_mais_recente(conn: sqlite3.Connection) -> Ranking | None:
    linha = conn.execute(
        "SELECT id, data_referencia, status, calculado_em FROM rankings ORDER BY id DESC LIMIT 1"
    ).fetchone()
    if linha is None:
        return None
    itens = conn.execute(
        "SELECT posicao, ticker, score, contribuicoes FROM ranking_itens "
        "WHERE ranking_id = ? ORDER BY posicao",
        (linha["id"],),
    ).fetchall()
    return Ranking(
        data_referencia=linha["data_referencia"],
        status=linha["status"],
        calculado_em=linha["calculado_em"],
        itens=[
            ItemRanking(
                posicao=r["posicao"],
                ticker=r["ticker"],
                score=r["score"],
                contribuicoes=json.loads(r["contribuicoes"]),
            )
            for r in itens
        ],
    )


def marcar_ranking_desatualizado(conn: sqlite3.Connection) -> None:
    """Marca o snapshot de ranking mais recente como desatualizado (falha do provedor).

    Mantém os dados anteriores; só muda o status — regra do AGENTS.md.
    """
    conn.execute(
        "UPDATE rankings SET status = 'desatualizado' "
        "WHERE id = (SELECT id FROM rankings ORDER BY id DESC LIMIT 1)"
    )
