"""Servir o Web App como estático mantém o router da API com precedência."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.deps import obter_conn
from api.main import montar_webapp
from api.routers.oportunidades import router
from storage.db import conectar, inicializar


def _cliente(tmp_path, com_build=True):
    if com_build:
        (tmp_path / "index.html").write_text(
            "<html><body>não é recomendação de investimento</body></html>",
            encoding="utf-8",
        )

    caminho = tmp_path / "teste.db"
    conn = conectar(caminho)
    inicializar(conn)
    conn.close()

    def _obter_conn():
        conexao = conectar(caminho)
        try:
            yield conexao
        finally:
            conexao.close()

    aplicacao = FastAPI()
    aplicacao.include_router(router)
    aplicacao.dependency_overrides[obter_conn] = _obter_conn
    if com_build:
        montar_webapp(aplicacao, tmp_path)
    return TestClient(aplicacao)


def test_index_servido_na_raiz(tmp_path):
    cliente = _cliente(tmp_path)
    with cliente:
        resposta = cliente.get("/")

        assert resposta.status_code == 200
        assert "não é recomendação" in resposta.text


def test_router_da_api_tem_precedencia(tmp_path):
    cliente = _cliente(tmp_path)
    with cliente:
        # sem ranking: 404 do router, não o index.html do estático
        resposta = cliente.get("/oportunidades")

        assert resposta.status_code == 404
        assert resposta.json()["detail"]


def test_sem_build_nao_monta_e_nao_quebra(tmp_path):
    cliente = _cliente(tmp_path, com_build=False)
    with cliente:
        assert cliente.get("/").status_code == 404
        assert cliente.get("/oportunidades").status_code == 404
