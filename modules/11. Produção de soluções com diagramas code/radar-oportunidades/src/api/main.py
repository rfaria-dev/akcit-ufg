"""Aplicação FastAPI do Radar de Oportunidades.

A API apenas lê e serve rankings e indicadores já calculados (AGENTS.md).
"""

import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers.oportunidades import router as oportunidades_router

app = FastAPI(
    title="Radar de Oportunidades",
    description=(
        "Consulta de ranking de oportunidades com score explicável. "
        "Ferramenta de triagem — não é recomendação de investimento."
    ),
    version="0.1.0",
)

app.include_router(oportunidades_router)


def montar_webapp(aplicacao: FastAPI, diretorio: str | Path) -> None:
    """Serve o build do Web App (React) como estático, se existir.

    O router da API mantém precedência: montado por último, o estático
    atende apenas caminhos fora de /oportunidades.
    """
    if Path(diretorio).is_dir():
        aplicacao.mount("/", StaticFiles(directory=str(diretorio), html=True), name="webapp")


# RADAR_WEBAPP_DIR aponta para o build; padrão: src/webapp/dist (ver ADR 0006)
montar_webapp(
    app,
    os.environ.get(
        "RADAR_WEBAPP_DIR",
        Path(__file__).resolve().parent.parent / "webapp" / "dist",
    ),
)
