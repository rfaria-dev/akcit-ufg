"""gravar_bruto e ler_brutos: round-trip, upsert, filtros e restrições."""

import pytest

from storage.repository import gravar_bruto, ler_brutos, upsert_ativo

PAYLOAD = {"fechamento": 36.42, "volume": 5_000_000}


@pytest.fixture
def petr4(conn) -> str:
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo")
    return "PETR4"


def test_round_trip(conn, petr4):
    gravar_bruto(conn, petr4, "cotacao", "2026-10-21", PAYLOAD)

    brutos = ler_brutos(conn)
    assert len(brutos) == 1
    assert brutos[0].ticker == petr4
    assert brutos[0].tipo == "cotacao"
    assert brutos[0].data_referencia == "2026-10-21"
    assert brutos[0].payload == PAYLOAD
    assert brutos[0].coletado_em  # preenchido automaticamente


def test_regravar_mesma_chave_substitui(conn, petr4):
    gravar_bruto(conn, petr4, "cotacao", "2026-10-21", {"fechamento": 36.42})
    gravar_bruto(conn, petr4, "cotacao", "2026-10-21", {"fechamento": 37.00})

    brutos = ler_brutos(conn)
    assert len(brutos) == 1
    assert brutos[0].payload["fechamento"] == 37.00


def test_filtra_por_tipo_e_data(conn, petr4):
    gravar_bruto(conn, petr4, "cotacao", "2026-10-21", PAYLOAD)
    gravar_bruto(conn, petr4, "fundamento", "2026-10-21", {"pl": 4.2})

    assert [b.tipo for b in ler_brutos(conn, tipo="cotacao")] == ["cotacao"]
    assert [b.tipo for b in ler_brutos(conn, data_referencia="2026-10-21")] == [
        "cotacao",
        "fundamento",
    ]


def test_tipo_invalido_e_rejeitado(conn, petr4):
    with pytest.raises(ValueError):
        gravar_bruto(conn, petr4, "tipo_inexistente", "2026-10-21", PAYLOAD)


def test_chave_estrangeira_impede_ticker_desconhecido(conn):
    with pytest.raises(Exception):
        gravar_bruto(conn, "NAOEXISTE", "cotacao", "2026-10-21", PAYLOAD)
