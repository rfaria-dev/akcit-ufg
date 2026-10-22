"""Portas do Coletor para os demais containers."""

import sqlite3
from typing import Protocol


class AcionadorMotor(Protocol):
    """Porta para o Motor de ranking (implementada na Etapa 3)."""

    def __call__(self, conn: sqlite3.Connection, data_referencia: str) -> None: ...
