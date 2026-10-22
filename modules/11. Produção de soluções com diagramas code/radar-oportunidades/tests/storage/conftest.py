"""Fixtures comuns dos testes do Armazenamento."""

import sqlite3

import pytest

from storage.db import conectar, inicializar


@pytest.fixture
def conn(tmp_path) -> sqlite3.Connection:
    """Banco SQLite temporário inicializado com o schema v1."""
    conexao = conectar(tmp_path / "teste.db")
    inicializar(conexao)
    yield conexao
    conexao.close()
