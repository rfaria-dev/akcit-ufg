"""Modelos de leitura/escrita do Armazenamento (sem acoplamento com SQLite)."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Ativo:
    ticker: str
    nome: str
    setor: str


@dataclass(frozen=True)
class DadoBruto:
    ticker: str
    tipo: str
    data_referencia: str
    payload: dict[str, Any]
    coletado_em: str


@dataclass(frozen=True)
class Indicador:
    ticker: str
    data_referencia: str
    indicador: str
    valor: float


@dataclass(frozen=True)
class ItemRanking:
    posicao: int
    ticker: str
    score: float
    contribuicoes: list[dict[str, Any]]


@dataclass(frozen=True)
class Ranking:
    data_referencia: str
    status: str
    calculado_em: str
    itens: list[ItemRanking] = field(default_factory=list)
