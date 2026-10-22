"""Cálculo dos indicadores fundamentalistas e de mercado (descricao §5).

Indicadores v1: P/L, P/VP, Dividend Yield, ROE, Dívida líquida/EBITDA,
margem líquida e liquidez média diária.
"""

import math
from dataclasses import dataclass
from typing import Any

NOME_INDICADORES = (
    "pl",
    "pvp",
    "dy",
    "roe",
    "dl_ebitda",
    "margem_liquida",
    "liquidez_media_diaria",
)

# Sentido de cada indicador, usado na normalização do score
SENTIDO: dict[str, str] = {
    "pl": "menor_melhor",
    "pvp": "menor_melhor",
    "dy": "maior_melhor",
    "roe": "maior_melhor",
    "dl_ebitda": "menor_melhor",
    "margem_liquida": "maior_melhor",
    "liquidez_media_diaria": "maior_melhor",
}


@dataclass(frozen=True)
class ResultadoIndicadores:
    indicadores: dict[str, float]
    ausentes: list[str]


def _campo(dados: dict[str, Any] | None, campo: str) -> Any:
    return dados.get(campo) if dados else None


def _razao(numerador: Any, denominador: Any) -> float | None:
    """Divisão segura: valor ausente ou denominador zero → None."""
    if numerador is None or denominador is None:
        return None
    try:
        return numerador / denominador
    except ZeroDivisionError:
        return None


def calcular_indicadores(
    cotacao: dict[str, Any] | None,
    fundamento: dict[str, Any] | None,
    provento: dict[str, Any] | None,
) -> ResultadoIndicadores:
    """Calcula os indicadores v1 a partir dos payloads brutos do provedor."""
    indicadores: dict[str, float] = {}
    ausentes: list[str] = []

    def definir(nome: str, valor: float | None) -> None:
        if valor is None or not math.isfinite(valor):
            ausentes.append(nome)
        else:
            indicadores[nome] = valor

    fechamento = _campo(cotacao, "fechamento")
    lpa = _campo(fundamento, "lpa")
    vpa = _campo(fundamento, "vpa")
    total_12m = _campo(provento, "total_12m")
    lucro = _campo(fundamento, "lucro_liquido")
    patrimonio = _campo(fundamento, "patrimonio_liquido")
    divida = _campo(fundamento, "divida_liquida")
    ebitda = _campo(fundamento, "ebitda")
    receita = _campo(fundamento, "receita_liquida")
    liquidez = _campo(cotacao, "liquidez_media_diaria")

    definir("pl", _razao(fechamento, lpa))
    definir("pvp", _razao(fechamento, vpa))
    definir("dy", _razao(total_12m, fechamento))
    definir("roe", _razao(lucro, patrimonio))
    definir("dl_ebitda", _razao(divida, ebitda))
    definir("margem_liquida", _razao(lucro, receita))
    definir(
        "liquidez_media_diaria",
        liquidez if liquidez is not None and math.isfinite(liquidez) else None,
    )

    return ResultadoIndicadores(indicadores=indicadores, ausentes=ausentes)
