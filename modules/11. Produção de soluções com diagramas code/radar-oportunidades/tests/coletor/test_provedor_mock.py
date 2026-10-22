"""ProvedorMock: determinismo e cenários."""

import pytest

from coletor.provedor import ProvedorIndisponivel, ProvedorTimeout
from coletor.provedor_mock import ProvedorMock


def test_sucesso_retorna_universo_completo():
    mock = ProvedorMock(data_referencia="2026-10-21")
    lote = mock.buscar()

    assert lote.data_referencia == "2026-10-21"
    assert len(lote.ativos) == 10
    # cada ativo com os três tipos de dado bruto
    assert len(lote.itens) == 3 * len(lote.ativos)
    assert {item.tipo for item in lote.itens} == {"cotacao", "fundamento", "provento"}
    assert {item.ticker for item in lote.itens} == {a.ticker for a in lote.ativos}


def test_sucesso_e_deterministico():
    mock = ProvedorMock(data_referencia="2026-10-21")
    assert mock.buscar() == mock.buscar()


def test_falha_levanta_indisponivel():
    mock = ProvedorMock(cenario="falha")
    with pytest.raises(ProvedorIndisponivel):
        mock.buscar()


def test_timeout_dorme_e_levanta_timeout():
    mock = ProvedorMock(cenario="timeout", atraso_segundos=0.01)
    with pytest.raises(ProvedorTimeout):
        mock.buscar()


def test_cenario_invalido_e_rejeitado():
    with pytest.raises(ValueError):
        ProvedorMock(cenario="inexistente")
