"""Dependências da API."""

import os
import sqlite3

from storage.db import conectar, inicializar

CAMINHO_BANCO = os.environ.get("RADAR_DB", "radar.db")


def obter_conn() -> sqlite3.Connection:
    """Conexão por requisição (gerenciada pelo FastAPI, fechada no teardown)."""
    conn = conectar(CAMINHO_BANCO)
    inicializar(conn)
    try:
        yield conn
    finally:
        conn.close()
