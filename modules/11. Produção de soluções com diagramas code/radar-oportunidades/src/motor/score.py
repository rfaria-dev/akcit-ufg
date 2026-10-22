"""Score v1: pesos iguais, normalização min-max e explicável (ADR 0004).

Cada contribuição registra o valor bruto, o valor normalizado, o peso e a
parcela do score — indicadores indisponíveis aparecem com `disponivel: false`
e não contribuem (o denominador é ajustado).
"""

from dataclasses import dataclass
from typing import Any

from .indicadores import NOME_INDICADORES, SENTIDO


@dataclass(frozen=True)
class ScoreResultado:
    score: float
    contribuicoes: list[dict[str, Any]]


def calcular_scores(resultados: dict[str, dict[str, float]]) -> dict[str, ScoreResultado]:
    """Calcula o score explicável de cada ativo.

    `resultados`: ticker -> {indicador -> valor calculado}.
    """
    # min/max por indicador sobre o universo do snapshot
    por_indicador: dict[str, dict[str, float]] = {nome: {} for nome in NOME_INDICADORES}
    for ticker, indicadores in resultados.items():
        for nome, valor in indicadores.items():
            por_indicador[nome][ticker] = valor
    min_max = {
        nome: (min(valores.values()), max(valores.values()))
        for nome, valores in por_indicador.items()
        if valores
    }

    def normalizar(nome: str, valor: float) -> float:
        minimo, maximo = min_max[nome]
        if maximo == minimo:
            return 1.0  # sem variação no universo: ninguém é penalizado
        faixa = maximo - minimo
        if SENTIDO[nome] == "menor_melhor":
            return (maximo - valor) / faixa
        return (valor - minimo) / faixa

    scores: dict[str, ScoreResultado] = {}
    for ticker, indicadores in resultados.items():
        disponiveis = list(indicadores)
        peso = 1.0 / len(disponiveis) if disponiveis else 0.0
        contribuicoes: list[dict[str, Any]] = []
        total = 0.0
        for nome in NOME_INDICADORES:
            if nome in indicadores:
                valor = indicadores[nome]
                normalizado = normalizar(nome, valor)
                contribuicao = normalizado * peso
                total += contribuicao
                contribuicoes.append(
                    {
                        "indicador": nome,
                        "disponivel": True,
                        "valor": valor,
                        "normalizado": normalizado,
                        "peso": peso,
                        "contribuicao": contribuicao,
                    }
                )
            else:
                contribuicoes.append(
                    {
                        "indicador": nome,
                        "disponivel": False,
                        "valor": None,
                        "normalizado": None,
                        "peso": 0.0,
                        "contribuicao": 0.0,
                    }
                )
        scores[ticker] = ScoreResultado(score=total, contribuicoes=contribuicoes)
    return scores
