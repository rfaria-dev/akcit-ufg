"""Conexão e inicialização do SQLite do Armazenamento."""

import sqlite3
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def conectar(caminho: str | Path) -> sqlite3.Connection:
    """Abre a conexão com linhas como `sqlite3.Row` e chaves estrangeiras ativas."""
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar(conn: sqlite3.Connection) -> None:
    """Cria o schema v1 (idempotente; ver docs/adr/0002-modelo-de-dados.md)."""
    conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
