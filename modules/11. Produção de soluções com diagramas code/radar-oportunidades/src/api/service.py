"""Serviço de consulta do ranking: somente leitura no Armazenamento."""

import sqlite3

from storage import repository

from .aviso import AVISO
from .schemas import Contribuicao, IndicadorAtivo, Oportunidade, RankingResponse


def buscar_oportunidades(
    conn: sqlite3.Connection,
    setor: str | None = None,
    minimo: dict[str, float] | None = None,
    maximo: dict[str, float] | None = None,
    limite: int = 20,
) -> RankingResponse | None:
    """Monta a resposta de ranking a partir do snapshot mais recente.

    Retorna None quando não há ranking algum (nunca coletado).
    """
    ranking = repository.ler_ranking_mais_recente(conn)
    if ranking is None:
        return None

    ativos = {a.ticker: a for a in repository.ler_ativos(conn)}
    valores = {
        (i.ticker, i.indicador): i.valor
        for i in repository.ler_indicadores(conn, data_referencia=ranking.data_referencia)
    }

    itens: list[Oportunidade] = []
    for item in ranking.itens:
        ativo = ativos.get(item.ticker)
        if ativo is None:
            continue  # ativo fora do cadastro: não consta na resposta
        if setor is not None and ativo.setor != setor:
            continue

        # indicadores na ordem canônica das contribuições do Motor
        indicadores = []
        for contrib in item.contribuicoes:
            if not contrib["disponivel"]:
                continue
            valor = valores.get((item.ticker, contrib["indicador"]))
            if valor is None:
                continue
            indicadores.append(IndicadorAtivo(indicador=contrib["indicador"], valor=valor))

        if not _atende_filtros(indicadores, minimo, maximo):
            continue

        itens.append(
            Oportunidade(
                posicao=item.posicao,
                ticker=item.ticker,
                nome=ativo.nome,
                setor=ativo.setor,
                score=item.score,
                indicadores=indicadores,
                contribuicoes=[Contribuicao(**contrib) for contrib in item.contribuicoes],
            )
        )
        if len(itens) >= limite:
            break

    return RankingResponse(
        data_referencia=ranking.data_referencia,
        status=ranking.status,
        aviso=AVISO,
        itens=itens,
    )


def _atende_filtros(
    indicadores: list[IndicadorAtivo],
    minimo: dict[str, float] | None,
    maximo: dict[str, float] | None,
) -> bool:
    """Filtros são estritos: indicador indisponível reprova o filtro dele."""
    valores = {i.indicador: i.valor for i in indicadores}
    for nome, piso in (minimo or {}).items():
        if nome not in valores or valores[nome] < piso:
            return False
    for nome, teto in (maximo or {}).items():
        if nome not in valores or valores[nome] > teto:
            return False
    return True
