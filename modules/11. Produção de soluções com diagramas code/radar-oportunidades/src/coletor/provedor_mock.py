"""Provedor mockado e determinístico (ver AGENTS.md: sem APIs reais).

Cenários controlados na construção: `sucesso` (padrão), `falha`
(ProvedorIndisponivel) e `timeout` (dorme e levanta ProvedorTimeout).
"""

import time
from datetime import date

from storage.models import Ativo

from .provedor import DadoAtivo, LoteDados, ProvedorIndisponivel, ProvedorTimeout

# Universo fixo de ativos da B3: ticker -> (nome, setor)
UNIVERSO_PADRAO: dict[str, tuple[str, str]] = {
    "ABEV3": ("Ambev ON", "Bebidas"),
    "BBDC4": ("Bradesco PN", "Bancos"),
    "EGIE3": ("Engie Brasil ON", "Energia"),
    "ITUB4": ("Itaú Unibanco PN", "Bancos"),
    "LREN3": ("Lojas Renner ON", "Varejo"),
    "PETR4": ("Petrobras PN", "Petróleo"),
    "RENT3": ("Localiza ON", "Aluguel de Veículos"),
    "TAEE11": ("Taesa Units", "Energia"),
    "VALE3": ("Vale ON", "Mineração"),
    "WEGE3": ("WEG ON", "Bens Industriais"),
}

COTACOES: dict[str, dict[str, float | int]] = {
    "PETR4": {"fechamento": 36.42, "volume": 21_000_000, "liquidez_media_diaria": 680_000_000},
    "VALE3": {"fechamento": 58.90, "volume": 15_000_000, "liquidez_media_diaria": 900_000_000},
    "ITUB4": {"fechamento": 33.10, "volume": 18_000_000, "liquidez_media_diaria": 1_200_000_000},
    "BBDC4": {"fechamento": 14.75, "volume": 12_000_000, "liquidez_media_diaria": 500_000_000},
    "ABEV3": {"fechamento": 13.20, "volume": 25_000_000, "liquidez_media_diaria": 650_000_000},
    "WEGE3": {"fechamento": 52.40, "volume": 6_000_000, "liquidez_media_diaria": 300_000_000},
    "RENT3": {"fechamento": 42.80, "volume": 8_000_000, "liquidez_media_diaria": 350_000_000},
    "LREN3": {"fechamento": 15.90, "volume": 9_000_000, "liquidez_media_diaria": 260_000_000},
    "EGIE3": {"fechamento": 44.30, "volume": 2_000_000, "liquidez_media_diaria": 90_000_000},
    "TAEE11": {"fechamento": 36.10, "volume": 3_000_000, "liquidez_media_diaria": 110_000_000},
}

# Valores monetários em R$ milhões; indicadores por ação em R$.
FUNDAMENTOS: dict[str, dict[str, float]] = {
    "PETR4": {"lpa": 8.10, "vpa": 27.50, "dividendo_por_acao": 4.90, "lucro_liquido": 105_000.0, "patrimonio_liquido": 360_000.0, "divida_liquida": 180_000.0, "ebitda": 250_000.0, "receita_liquida": 480_000.0},
    "VALE3": {"lpa": 9.80, "vpa": 45.20, "dividendo_por_acao": 5.20, "lucro_liquido": 58_000.0, "patrimonio_liquido": 300_000.0, "divida_liquida": 70_000.0, "ebitda": 160_000.0, "receita_liquida": 220_000.0},
    "ITUB4": {"lpa": 4.10, "vpa": 20.80, "dividendo_por_acao": 1.30, "lucro_liquido": 38_000.0, "patrimonio_liquido": 190_000.0, "divida_liquida": 150_000.0, "ebitda": 90_000.0, "receita_liquida": 175_000.0},
    "BBDC4": {"lpa": 1.75, "vpa": 18.90, "dividendo_por_acao": 0.95, "lucro_liquido": 16_000.0, "patrimonio_liquido": 165_000.0, "divida_liquida": 120_000.0, "ebitda": 55_000.0, "receita_liquida": 95_000.0},
    "ABEV3": {"lpa": 0.85, "vpa": 5.10, "dividendo_por_acao": 0.72, "lucro_liquido": 12_500.0, "patrimonio_liquido": 80_000.0, "divida_liquida": 3_000.0, "ebitda": 21_000.0, "receita_liquida": 83_000.0},
    "WEGE3": {"lpa": 1.35, "vpa": 4.90, "dividendo_por_acao": 0.55, "lucro_liquido": 5_800.0, "patrimonio_liquido": 21_000.0, "divida_liquida": -4_000.0, "ebitda": 8_000.0, "receita_liquida": 36_000.0},
    "RENT3": {"lpa": 2.10, "vpa": 17.60, "dividendo_por_acao": 0.40, "lucro_liquido": 3_200.0, "patrimonio_liquido": 27_000.0, "divida_liquida": 41_000.0, "ebitda": 9_500.0, "receita_liquida": 32_000.0},
    "LREN3": {"lpa": 1.05, "vpa": 9.80, "dividendo_por_acao": 0.85, "lucro_liquido": 1_050.0, "patrimonio_liquido": 9_800.0, "divida_liquida": -1_500.0, "ebitda": 2_400.0, "receita_liquida": 14_000.0},
    "EGIE3": {"lpa": 4.20, "vpa": 17.30, "dividendo_por_acao": 3.10, "lucro_liquido": 3_300.0, "patrimonio_liquido": 14_000.0, "divida_liquida": 15_000.0, "ebitda": 6_800.0, "receita_liquida": 12_000.0},
    "TAEE11": {"lpa": 2.40, "vpa": 11.20, "dividendo_por_acao": 2.90, "lucro_liquido": 2_400.0, "patrimonio_liquido": 11_500.0, "divida_liquida": 5_200.0, "ebitda": 5_000.0, "receita_liquida": 8_300.0},
}

PROVENTOS: dict[str, dict[str, float]] = {
    ticker: {"total_12m": fundamento["dividendo_por_acao"]}
    for ticker, fundamento in FUNDAMENTOS.items()
}


class ProvedorMock:
    """Provedor determinístico para desenvolvimento e testes."""

    def __init__(
        self,
        cenario: str = "sucesso",
        data_referencia: str | None = None,
        universo: dict[str, tuple[str, str]] | None = None,
        atraso_segundos: float = 1.0,
    ):
        if cenario not in ("sucesso", "falha", "timeout"):
            raise ValueError(f"cenário inválido: {cenario!r}")
        self._cenario = cenario
        self._universo = universo or UNIVERSO_PADRAO
        self._data_referencia = data_referencia or date.today().isoformat()
        self._atraso_segundos = atraso_segundos

    def buscar(self) -> LoteDados:
        if self._cenario == "falha":
            raise ProvedorIndisponivel("provedor de dados fora do ar")
        if self._cenario == "timeout":
            time.sleep(self._atraso_segundos)
            raise ProvedorTimeout("provedor não respondeu a tempo")
        return self._montar_lote()

    def _montar_lote(self) -> LoteDados:
        ativos = [
            Ativo(ticker=ticker, nome=nome, setor=setor)
            for ticker, (nome, setor) in self._universo.items()
        ]
        itens = []
        for ticker in self._universo:
            itens.append(DadoAtivo(ticker, "cotacao", dict(COTACOES[ticker])))
            itens.append(DadoAtivo(ticker, "fundamento", dict(FUNDAMENTOS[ticker])))
            itens.append(DadoAtivo(ticker, "provento", dict(PROVENTOS[ticker])))
        return LoteDados(data_referencia=self._data_referencia, ativos=ativos, itens=itens)
