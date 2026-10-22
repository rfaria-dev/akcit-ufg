"""Cálculo dos indicadores a partir de payloads brutos."""

from motor.indicadores import NOME_INDICADORES, calcular_indicadores

COTACAO = {"fechamento": 40.0, "volume": 1_000_000, "liquidez_media_diaria": 500_000_000}
FUNDAMENTO = {
    "lpa": 4.0,
    "vpa": 20.0,
    "dividendo_por_acao": 2.0,
    "lucro_liquido": 8_000.0,
    "patrimonio_liquido": 40_000.0,
    "divida_liquida": 16_000.0,
    "ebitda": 20_000.0,
    "receita_liquida": 50_000.0,
}
PROVENTO = {"total_12m": 2.0}


def test_calcula_todos_os_indicadores():
    resultado = calcular_indicadores(COTACAO, FUNDAMENTO, PROVENTO)

    assert resultado.indicadores == {
        "pl": 10.0,  # 40 / 4
        "pvp": 2.0,  # 40 / 20
        "dy": 0.05,  # 2 / 40
        "roe": 0.2,  # 8000 / 40000
        "dl_ebitda": 0.8,  # 16000 / 20000
        "margem_liquida": 0.16,  # 8000 / 50000
        "liquidez_media_diaria": 500_000_000,
    }
    assert resultado.ausentes == []


def test_divisor_zero_torna_indicador_ausente():
    fundamento = {**FUNDAMENTO, "lpa": 0.0, "ebitda": 0.0}
    resultado = calcular_indicadores(COTACAO, fundamento, PROVENTO)

    assert resultado.ausentes == ["pl", "dl_ebitda"]
    assert "pl" not in resultado.indicadores
    assert resultado.indicadores["pvp"] == 2.0


def test_dados_ausentes_tornam_todos_ausentes():
    resultado = calcular_indicadores(None, None, None)

    assert resultado.indicadores == {}
    assert set(resultado.ausentes) == set(NOME_INDICADORES)


def test_sem_provento_dy_ausente():
    resultado = calcular_indicadores(COTACAO, FUNDAMENTO, None)

    assert resultado.ausentes == ["dy"]
