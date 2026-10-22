"""Ordenação do ranking."""

from typing import Any

from .score import ScoreResultado


def ordenar(
    scores: dict[str, ScoreResultado],
) -> list[tuple[int, str, float, list[dict[str, Any]]]]:
    """Ordena por score decrescente; empates desempatam por ticker (determinístico).

    Retorna os itens no formato do Armazenamento: (posicao, ticker, score, contribuicoes).
    """
    ordenados = sorted(scores.items(), key=lambda par: (-par[1].score, par[0]))
    return [
        (posicao, ticker, round(resultado.score, 6), resultado.contribuicoes)
        for posicao, (ticker, resultado) in enumerate(ordenados, start=1)
    ]
