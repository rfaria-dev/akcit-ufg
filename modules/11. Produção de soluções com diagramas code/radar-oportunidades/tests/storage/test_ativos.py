"""upsert_ativo e ler_ativos."""

from storage.repository import ler_ativos, upsert_ativo


def test_upsert_insere_e_atualiza(conn):
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo")
    upsert_ativo(conn, "VALE3", "Vale ON", "Mineração")
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo e Gás")  # atualiza o setor

    ativos = ler_ativos(conn)
    assert [(a.ticker, a.setor) for a in ativos] == [
        ("PETR4", "Petróleo e Gás"),
        ("VALE3", "Mineração"),
    ]


def test_ler_ativos_filtra_por_setor(conn):
    upsert_ativo(conn, "PETR4", "Petrobras PN", "Petróleo")
    upsert_ativo(conn, "ITUB4", "Itaú Unibanco PN", "Bancos")

    assert [a.ticker for a in ler_ativos(conn, setor="Bancos")] == ["ITUB4"]


def test_ler_ativos_sem_dados(conn):
    assert ler_ativos(conn) == []
