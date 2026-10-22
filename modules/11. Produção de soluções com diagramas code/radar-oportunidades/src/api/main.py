"""Aplicação FastAPI do Radar de Oportunidades.

A API apenas lê e serve rankings e indicadores já calculados (AGENTS.md).
"""

from fastapi import FastAPI

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
