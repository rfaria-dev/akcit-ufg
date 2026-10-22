"""Container Armazenamento: único ponto de acesso ao SQLite do sistema.

Os demais containers usam apenas as funções de `repository` e os modelos;
nunca abrem o banco diretamente.
"""

from . import db, models, repository

__all__ = ["db", "models", "repository"]
