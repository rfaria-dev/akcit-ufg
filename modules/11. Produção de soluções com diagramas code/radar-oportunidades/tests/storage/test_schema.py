"""O schema v1 é criado com as tabelas e restrições esperadas."""

import sqlite3

import pytest

from storage.db import inicializar


def _tabelas(conn: sqlite3.Connection) -> set[str]:
    return {
        r["name"]
        for r in conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
    }


def test_cria_todas_as_tabelas(conn):
    assert {"ativos", "dados_brutos", "indicadores", "rankings", "ranking_itens"} <= _tabelas(conn)


def test_inicializar_e_idempotente(conn):
    inicializar(conn)  # segunda execução não pode falhar


def test_status_de_ranking_invalido_e_rejeitado(conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO rankings (data_referencia, status, calculado_em) "
            "VALUES ('2026-10-21', 'desconhecido', 'x')"
        )


def test_chave_estrangeira_impede_ticker_desconhecido(conn):
    with pytest.raises(sqlite3.IntegrityError):
        conn.execute(
            "INSERT INTO dados_brutos (ticker, tipo, data_referencia, payload, coletado_em) "
            "VALUES ('NAOEXISTE', 'cotacao', '2026-10-21', '{}', 'x')"
        )
