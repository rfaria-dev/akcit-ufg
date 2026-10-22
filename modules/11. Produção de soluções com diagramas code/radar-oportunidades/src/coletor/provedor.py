"""Contrato do provedor de dados de mercado.

O provedor real não é integrado (ver AGENTS.md): apenas uma implementação
mockada atrás desta interface.
"""

from dataclasses import dataclass
from typing import Any, Protocol

from storage.models import Ativo


class ErroProvedor(Exception):
    """Base para falhas do provedor de dados."""


class ProvedorIndisponivel(ErroProvedor):
    """Provedor fora do ar."""


class ProvedorTimeout(ErroProvedor):
    """Provedor não respondeu dentro do tempo limite."""


@dataclass(frozen=True)
class DadoAtivo:
    ticker: str
    tipo: str  # cotacao | fundamento | provento
    payload: dict[str, Any]


@dataclass(frozen=True)
class LoteDados:
    data_referencia: str
    ativos: list[Ativo]
    itens: list[DadoAtivo]


class ProvedorDados(Protocol):
    """Porta do provedor: devolve cotações, fundamentos e proventos."""

    def buscar(self) -> LoteDados: ...
