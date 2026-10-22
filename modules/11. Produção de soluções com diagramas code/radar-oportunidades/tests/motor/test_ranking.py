"""Ordenação do ranking: score decrescente, empates determinísticos."""

from motor.ranking import ordenar
from motor.score import ScoreResultado


def test_ordena_por_score_decrescente():
    scores = {
        "AAA": ScoreResultado(0.5, []),
        "BBB": ScoreResultado(0.9, []),
        "CCC": ScoreResultado(0.7, []),
    }
    itens = ordenar(scores)

    assert [(pos, ticker, score) for pos, ticker, score, _ in itens] == [
        (1, "BBB", 0.9),
        (2, "CCC", 0.7),
        (3, "AAA", 0.5),
    ]


def test_empate_desempata_por_ticker():
    scores = {
        "PETR4": ScoreResultado(0.5, []),
        "ABEV3": ScoreResultado(0.5, []),
    }
    itens = ordenar(scores)

    assert [ticker for _, ticker, _, _ in itens] == ["ABEV3", "PETR4"]
