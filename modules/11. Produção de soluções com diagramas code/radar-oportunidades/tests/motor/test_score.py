"""Score v1: pesos iguais, min-max e contribuições explicáveis."""

import pytest

from motor.indicadores import NOME_INDICADORES
from motor.score import calcular_scores


def test_um_ativo_recebe_score_um():
    valores = {nome: 1.0 for nome in NOME_INDICADORES}
    resultado = calcular_scores({"PETR4": valores})["PETR4"]

    # sem variação no universo: normalizado 1.0; peso 1/7 por indicador
    assert resultado.score == pytest.approx(1.0)
    assert sum(c["contribuicao"] for c in resultado.contribuicoes) == pytest.approx(
        resultado.score
    )


def test_normalizacao_min_max_maior_melhor():
    scores = calcular_scores({"AAA": {"roe": 0.2}, "BBB": {"roe": 0.1}})
    assert scores["AAA"].score == pytest.approx(1.0)
    assert scores["BBB"].score == pytest.approx(0.0)


def test_menor_melhor_inverte():
    # P/L menor é melhor: 5 normaliza para 1.0 e 10 para 0.0
    scores = calcular_scores({"AAA": {"pl": 5.0}, "BBB": {"pl": 10.0}})
    assert scores["AAA"].score == pytest.approx(1.0)
    assert scores["BBB"].score == pytest.approx(0.0)


def test_pesos_iguais_entre_disponiveis():
    valores = {nome: 1.0 for nome in ("pl", "pvp", "dy", "roe")}
    resultado = calcular_scores({"PETR4": valores})["PETR4"]

    assert resultado.score == pytest.approx(1.0)
    pesos = {c["indicador"]: c["peso"] for c in resultado.contribuicoes if c["disponivel"]}
    assert pesos == {"pl": 0.25, "pvp": 0.25, "dy": 0.25, "roe": 0.25}


def test_indisponiveis_aparecem_na_explicacao_sem_contribuir():
    resultado = calcular_scores({"AAA": {"roe": 0.2}})["AAA"]

    contribuicoes = resultado.contribuicoes
    assert len(contribuicoes) == len(NOME_INDICADORES)
    indisponiveis = [c for c in contribuicoes if not c["disponivel"]]
    assert len(indisponiveis) == 6
    assert all(c["contribuicao"] == 0.0 and c["peso"] == 0.0 for c in indisponiveis)
    assert resultado.score == pytest.approx(1.0)


def test_contribuicoes_somam_ao_score():
    valores = {
        "pl": 4.0,
        "pvp": 2.0,
        "dy": 0.05,
        "roe": 0.2,
        "dl_ebitda": 0.8,
        "margem_liquida": 0.16,
        "liquidez_media_diaria": 500_000_000,
    }
    scores = calcular_scores({"AAA": valores, "BBB": {k: v * 2 for k, v in valores.items()}})

    for resultado in scores.values():
        soma = sum(c["contribuicao"] for c in resultado.contribuicoes)
        assert soma == pytest.approx(resultado.score)


def test_sem_indicadores_score_zero():
    resultado = calcular_scores({"AAA": {}})["AAA"]

    assert resultado.score == 0.0
    assert all(not c["disponivel"] for c in resultado.contribuicoes)
