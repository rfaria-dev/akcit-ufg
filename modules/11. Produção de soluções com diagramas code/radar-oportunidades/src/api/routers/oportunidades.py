"""Consulta de oportunidades: somente leitura (ver ADR 0005)."""

import sqlite3

from fastapi import APIRouter, Depends, HTTPException, Query

from ..deps import obter_conn
from ..schemas import RankingResponse
from ..service import buscar_oportunidades

router = APIRouter(tags=["oportunidades"])


@router.get("/oportunidades", response_model=RankingResponse)
def listar_oportunidades(
    conn: sqlite3.Connection = Depends(obter_conn),
    setor: str | None = Query(None, description="filtra por setor do ativo"),
    min_pl: float | None = None,
    max_pl: float | None = None,
    min_pvp: float | None = None,
    max_pvp: float | None = None,
    min_dy: float | None = None,
    max_dy: float | None = None,
    min_roe: float | None = None,
    max_roe: float | None = None,
    min_dl_ebitda: float | None = None,
    max_dl_ebitda: float | None = None,
    min_margem_liquida: float | None = None,
    max_margem_liquida: float | None = None,
    min_liquidez_media_diaria: float | None = None,
    max_liquidez_media_diaria: float | None = None,
    limite: int = Query(20, ge=1, le=100, description="quantidade máxima de itens"),
) -> RankingResponse:
    minimo = {
        nome: valor
        for nome, valor in {
            "pl": min_pl,
            "pvp": min_pvp,
            "dy": min_dy,
            "roe": min_roe,
            "dl_ebitda": min_dl_ebitda,
            "margem_liquida": min_margem_liquida,
            "liquidez_media_diaria": min_liquidez_media_diaria,
        }.items()
        if valor is not None
    }
    maximo = {
        nome: valor
        for nome, valor in {
            "pl": max_pl,
            "pvp": max_pvp,
            "dy": max_dy,
            "roe": max_roe,
            "dl_ebitda": max_dl_ebitda,
            "margem_liquida": max_margem_liquida,
            "liquidez_media_diaria": max_liquidez_media_diaria,
        }.items()
        if valor is not None
    }

    resposta = buscar_oportunidades(
        conn, setor=setor, minimo=minimo, maximo=maximo, limite=limite
    )
    if resposta is None:
        raise HTTPException(
            status_code=404,
            detail="nenhum ranking disponível; execute a coleta antes de consultar",
        )
    return resposta
