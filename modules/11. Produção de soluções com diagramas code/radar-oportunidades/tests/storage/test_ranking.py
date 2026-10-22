"""gravar_ranking, ler_ranking_mais_recente e marcar_ranking_desatualizado."""

import pytest

from storage.repository import (
    gravar_ranking,
    ler_ranking_mais_recente,
    marcar_ranking_desatualizado,
    upsert_ativo,
)


def _itens():
    return [
        (1, "PETR4", 0.87, [{"indicador": "pl", "contribuicao": 0.1}]),
        (2, "VALE3", 0.72, [{"indicador": "pl", "contribuicao": 0.08}]),
    ]


@pytest.fixture
def ativos(conn):
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo")
    upsert_ativo(conn, "VALE3", "Vale ON", "Mineração")


def test_round_trip_ordenado_por_posicao(conn, ativos):
    gravar_ranking(conn, "2026-10-21", "atualizado", _itens())

    ranking = ler_ranking_mais_recente(conn)
    assert ranking is not None
    assert ranking.data_referencia == "2026-10-21"
    assert ranking.status == "atualizado"
    assert [i.ticker for i in ranking.itens] == ["PETR4", "VALE3"]
    assert ranking.itens[0].score == 0.87
    assert ranking.itens[0].contribuicoes[0]["indicador"] == "pl"


def test_mais_recente_e_o_ultimo_snapshot(conn, ativos):
    gravar_ranking(conn, "2026-10-21", "atualizado", _itens())
    gravar_ranking(conn, "2026-10-22", "atualizado", _itens())

    assert ler_ranking_mais_recente(conn).data_referencia == "2026-10-22"


def test_sem_ranking_retorna_none(conn):
    assert ler_ranking_mais_recente(conn) is None


def test_marcar_desatualizado_afeta_apenas_o_mais_recente(conn, ativos):
    gravar_ranking(conn, "2026-10-21", "atualizado", _itens())
    gravar_ranking(conn, "2026-10-22", "atualizado", _itens())

    marcar_ranking_desatualizado(conn)

    assert ler_ranking_mais_recente(conn).status == "desatualizado"
    # o snapshot anterior permanece intacto
    anterior = conn.execute(
        "SELECT status FROM rankings WHERE data_referencia = '2026-10-21'"
    ).fetchone()
    assert anterior["status"] == "atualizado"


def test_status_invalido_e_rejeitado(conn, ativos):
    with pytest.raises(ValueError):
        gravar_ranking(conn, "2026-10-21", "desconhecido", _itens())
