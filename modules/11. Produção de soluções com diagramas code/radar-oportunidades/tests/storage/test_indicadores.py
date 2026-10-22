"""gravar_indicador e ler_indicadores."""

from storage.repository import gravar_indicador, ler_indicadores, upsert_ativo


def test_round_trip_e_upsert(conn):
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo")
    gravar_indicador(conn, "PETR4", "2026-10-21", "pl", 4.2)
    gravar_indicador(conn, "PETR4", "2026-10-21", "roe", 0.18)
    gravar_indicador(conn, "PETR4", "2026-10-21", "pl", 4.5)  # substitui o valor

    indicadores = ler_indicadores(conn)
    assert [(i.indicador, i.valor) for i in indicadores] == [("pl", 4.5), ("roe", 0.18)]


def test_filtra_por_data_referencia(conn):
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo")
    gravar_indicador(conn, "PETR4", "2026-10-21", "pl", 4.2)
    gravar_indicador(conn, "PETR4", "2026-10-22", "pl", 4.1)

    assert len(ler_indicadores(conn)) == 2
    assert len(ler_indicadores(conn, data_referencia="2026-10-22")) == 1
