"""Coletor: ingestão com sucesso, falha do provedor e timeout."""

import logging
import time

import pytest

from coletor.coletor import executar
from coletor.provedor_mock import ProvedorMock
from storage import repository
from storage.db import conectar, inicializar


class MotorFake:
    """Fake da porta AcionadorMotor: registra as chamadas."""

    def __init__(self):
        self.chamadas = []

    def __call__(self, conn, data_referencia):
        self.chamadas.append(data_referencia)


class ProvedorQueDorme:
    """Provedor lento para exercitar o timeout real do Coletor."""

    def buscar(self):
        time.sleep(0.5)
        raise AssertionError("não deveria chegar aqui")


class ProvedorQuebrado:
    """Provedor com erro inesperado (bug): deve propagar."""

    def buscar(self):
        raise RuntimeError("bug inesperado")


@pytest.fixture
def conn(tmp_path):
    conexao = conectar(tmp_path / "teste.db")
    inicializar(conexao)
    yield conexao
    conexao.close()


def test_sucesso_persiste_brutos_e_aciona_motor(conn):
    motor = MotorFake()
    mock = ProvedorMock(data_referencia="2026-10-21")

    executar(conn, mock, motor)

    brutos = repository.ler_brutos(conn)
    assert len(brutos) == 30  # 10 ativos × 3 tipos
    assert {b.data_referencia for b in brutos} == {"2026-10-21"}
    assert len(repository.ler_ativos(conn)) == 10
    assert motor.chamadas == ["2026-10-21"]


def test_falha_mantem_dados_e_marca_desatualizado(conn, caplog):
    motor = MotorFake()
    executar(conn, ProvedorMock(data_referencia="2026-10-21"), motor)
    repository.gravar_ranking(conn, "2026-10-21", "atualizado", [])
    conn.commit()

    with caplog.at_level(logging.ERROR, logger="coletor"):
        executar(conn, ProvedorMock(cenario="falha"), motor)

    ranking = repository.ler_ranking_mais_recente(conn)
    assert ranking is not None
    assert ranking.status == "desatualizado"
    assert ranking.data_referencia == "2026-10-21"  # dado anterior mantido
    assert len(repository.ler_brutos(conn)) == 30  # nada foi apagado
    assert motor.chamadas == ["2026-10-21"]  # motor não acionado na falha
    assert any("desatualizados" in r.message for r in caplog.records)


def test_falha_sem_ranking_anterior_nao_lanca(conn, caplog):
    with caplog.at_level(logging.ERROR, logger="coletor"):
        executar(conn, ProvedorMock(cenario="falha"), MotorFake())

    assert repository.ler_ranking_mais_recente(conn) is None
    assert len(caplog.records) == 1


def test_timeout_real_marca_desatualizado(conn, caplog):
    executar(conn, ProvedorMock(data_referencia="2026-10-21"), MotorFake())
    repository.gravar_ranking(conn, "2026-10-21", "atualizado", [])
    conn.commit()

    with caplog.at_level(logging.ERROR, logger="coletor"):
        executar(conn, ProvedorQueDorme(), MotorFake(), timeout_segundos=0.05)

    assert repository.ler_ranking_mais_recente(conn).status == "desatualizado"


def test_erro_inesperado_propaga(conn):
    with pytest.raises(RuntimeError):
        executar(conn, ProvedorQuebrado(), MotorFake())
