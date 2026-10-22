"""Contratos da API (Pydantic)."""

from pydantic import BaseModel


class Contribuicao(BaseModel):
    """Parcela de um indicador no score (score explicável — AGENTS.md)."""

    indicador: str
    disponivel: bool
    valor: float | None
    normalizado: float | None
    peso: float
    contribuicao: float


class IndicadorAtivo(BaseModel):
    indicador: str
    valor: float


class Oportunidade(BaseModel):
    posicao: int  # posição no ranking completo, preservada após filtros
    ticker: str
    nome: str
    setor: str
    score: float
    indicadores: list[IndicadorAtivo]
    contribuicoes: list[Contribuicao]


class RankingResponse(BaseModel):
    data_referencia: str
    status: str  # atualizado | desatualizado
    aviso: str
    itens: list[Oportunidade]
