"""GET /oportunidades: contrato, filtros, status e aviso (ADR 0005)."""

import pytest
from fastapi.testclient import TestClient

from api.deps import obter_conn
from api.main import app
from coletor.coletor import executar
from coletor.provedor_mock import ProvedorMock
from motor.motor import calcular
from storage import repository
from storage.db import conectar, inicializar

DATA_REFERENCIA = "2026-10-21"


def _conectar_por_requisicao(caminho):
    """Override de obter_conn: conexão criada na thread da requisição (como em produção)."""

    def _obter_conn():
        conexao = conectar(caminho)
        try:
            yield conexao
        finally:
            conexao.close()

    return _obter_conn


@pytest.fixture
def client(tmp_path):
    """App com banco temporário populado pelo pipeline completo (Coletor + Motor)."""
    caminho = tmp_path / "teste.db"
    conn = conectar(caminho)
    inicializar(conn)
    executar(conn, ProvedorMock(data_referencia=DATA_REFERENCIA), calcular)
    conn.close()

    app.dependency_overrides[obter_conn] = _conectar_por_requisicao(caminho)
    app.state.caminho_banco = caminho
    with TestClient(app) as cliente:
        yield cliente
    app.dependency_overrides.clear()


@pytest.fixture
def client_vazio(tmp_path):
    """App com banco vazio (nunca coletado)."""
    caminho = tmp_path / "teste.db"
    conn = conectar(caminho)
    inicializar(conn)
    conn.close()

    app.dependency_overrides[obter_conn] = _conectar_por_requisicao(caminho)
    with TestClient(app) as cliente:
        yield cliente
    app.dependency_overrides.clear()


def test_ranking_completo_contrato(client):
    resposta = client.get("/oportunidades")

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["data_referencia"] == DATA_REFERENCIA
    assert corpo["status"] == "atualizado"
    assert "recomendação de investimento" in corpo["aviso"]
    assert len(corpo["itens"]) == 10

    primeiro = corpo["itens"][0]
    assert primeiro["ticker"] and primeiro["nome"] and primeiro["setor"]
    assert len(primeiro["indicadores"]) == 7
    assert len(primeiro["contribuicoes"]) == 7
    # score explicável: contribuições somam ao score
    assert sum(c["contribuicao"] for c in primeiro["contribuicoes"]) == pytest.approx(
        primeiro["score"]
    )
    # posições em ordem crescente
    posicoes = [i["posicao"] for i in corpo["itens"]]
    assert posicoes == sorted(posicoes)


def test_sem_ranking_retorna_404(client_vazio):
    resposta = client_vazio.get("/oportunidades")

    assert resposta.status_code == 404
    assert "coleta" in resposta.json()["detail"]


def test_filtro_por_setor(client):
    resposta = client.get("/oportunidades", params={"setor": "Bancos"})

    assert resposta.status_code == 200
    itens = resposta.json()["itens"]
    assert [i["ticker"] for i in itens] == ["ITUB4", "BBDC4"]
    assert all(i["setor"] == "Bancos" for i in itens)


def test_filtro_min_max_por_indicador(client):
    # P/L entre 5 e 10 no mock: só VALE3 (6,01), ITUB4 (8,07) e BBDC4 (8,43)
    resposta = client.get("/oportunidades", params={"min_pl": 5, "max_pl": 10})

    assert resposta.status_code == 200
    itens = resposta.json()["itens"]
    assert [i["ticker"] for i in itens] == ["VALE3", "ITUB4", "BBDC4"]
    valores_pl = [
        next(i["valor"] for i in item["indicadores"] if i["indicador"] == "pl")
        for item in itens
    ]
    assert all(5 <= valor <= 10 for valor in valores_pl)


def test_filtro_sem_resultado_mantem_contrato(client):
    resposta = client.get("/oportunidades", params={"min_dy": 10})

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["itens"] == []
    assert corpo["data_referencia"] == DATA_REFERENCIA
    assert corpo["status"] == "atualizado"
    assert corpo["aviso"]


def test_limite_trunca(client):
    resposta = client.get("/oportunidades", params={"limite": 3})

    assert resposta.status_code == 200
    assert len(resposta.json()["itens"]) == 3


def test_limite_invalido_rejeitado(client):
    assert client.get("/oportunidades", params={"limite": 0}).status_code == 422


def test_dados_desatualizados_propagados(client):
    # falha do provedor na coleta seguinte: marca o snapshot como desatualizado
    conn = conectar(client.app.state.caminho_banco)
    repository.marcar_ranking_desatualizado(conn)
    conn.commit()
    conn.close()

    resposta = client.get("/oportunidades")

    assert resposta.status_code == 200
    corpo = resposta.json()
    assert corpo["status"] == "desatualizado"
    assert corpo["data_referencia"] == DATA_REFERENCIA
    assert len(corpo["itens"]) == 10  # dados anteriores mantidos


def test_openapi_documenta_endpoint(client):
    resposta = client.get("/openapi.json")

    assert resposta.status_code == 200
    assert "/oportunidades" in resposta.json()["paths"]
