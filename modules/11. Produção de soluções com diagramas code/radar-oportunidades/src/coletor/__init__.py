"""Container Coletor: ingestão agendada de dados do provedor mockado."""

from .coletor import executar
from .provedor import (
    DadoAtivo,
    ErroProvedor,
    LoteDados,
    ProvedorDados,
    ProvedorIndisponivel,
    ProvedorTimeout,
)
from .provedor_mock import ProvedorMock

__all__ = [
    "DadoAtivo",
    "ErroProvedor",
    "LoteDados",
    "ProvedorDados",
    "ProvedorIndisponivel",
    "ProvedorMock",
    "ProvedorTimeout",
    "executar",
]
