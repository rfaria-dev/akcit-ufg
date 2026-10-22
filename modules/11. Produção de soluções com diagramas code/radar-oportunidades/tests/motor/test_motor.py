"""Motor: fluxo completo a partir dos dados brutos do Armazenamento."""

import logging

import pytest

from coletor.provedor_mock import ProvedorMock
from motor.motor import calcular
from storage import repository
from storage.db import conectar, inicializar


@pytest.fixture
def conn(tmp_path):
    conexao = conectar(tmp_path / "teste.db")
    inicializar(conexao)
    yield conexao
    conexao.close()


def _popular_brutos(conn, data_referencia="2026-10-21"):
    lote = ProvedorMock(data_referencia=data_referencia).buscar()
    for ativo in lote.ativos:
        repository.upsert_ativo(conn, ativo.ticker, ativo.nome, ativo.setor)
    for item in lote.itens:
        repository.gravar_bruto(conn, item.ticker, item.tipo, lote.data_referencia, item.payload)
    conn.commit()


def test_calcula_indicadores_e_grava_ranking(conn):
    _popular_brutos(conn)

    calcular(conn, "2026-10-21")

    indicadores = repository.ler_indicadores(conn, data_referencia="2026-10-21")
    assert len(indicadores) == 10 * 7

    ranking = repository.ler_ranking_mais_recente(conn)
    assert ranking is not None
    assert ranking.status == "atualizado"
    assert ranking.data_referencia == "2026-10-21"
    assert len(ranking.itens) == 10
    assert [i.posicao for i in ranking.itens] == list(range(1, 11))
    scores = [i.score for i in ranking.itens]
    assert scores == sorted(scores, reverse=True)
    # cada item é explicável: contribuições somam ao score
    for item in ranking.itens:
        assert sum(c["contribuicao"] for c in item.contribuicoes) == pytest.approx(item.score)


def test_nao_grava_ranking_sem_dados_brutos(conn, caplog):
    with caplog.at_level(logging.WARNING, logger="motor"):
        calcular(conn, "2026-10-21")

    assert repository.ler_ranking_mais_recente(conn) is None
    assert any("sem dados brutos" in r.message for r in caplog.records)


def test_recalcular_e_idempotente_para_indicadores(conn):
    _popular_brutos(conn)
    calcular(conn, "2026-10-21")
    calcular(conn, "2026-10-21")

    # indicadores: chave natural (ticker, indicador, data) — sem duplicatas
    assert len(repository.ler_indicadores(conn, data_referencia="2026-10-21")) == 70
    # rankings: cada execução gera um snapshot novo (sem expurgo — ADR 0002)
    total = conn.execute("SELECT COUNT(*) AS n FROM rankings").fetchone()["n"]
    assert total == 2
