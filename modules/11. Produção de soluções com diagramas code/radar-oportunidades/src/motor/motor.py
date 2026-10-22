"""Motor de indicadores e ranking: entrada acionada pelo Coletor.

Lê os dados brutos de uma data de referência, calcula indicadores e score
e grava indicadores + snapshot de ranking (docs/diagrams/sequencia.mmd).
"""

import logging
import sqlite3

from storage import repository

from .indicadores import calcular_indicadores
from .ranking import ordenar
from .score import calcular_scores

logger = logging.getLogger("motor")


def calcular(conn: sqlite3.Connection, data_referencia: str) -> None:
    """Calcula indicadores e ranking para a data de referência informada.

    Chamada pelo Coletor (porta AcionadorMotor). Faz commit ao final.
    """
    brutos = repository.ler_brutos(conn, data_referencia=data_referencia)
    if not brutos:
        logger.warning("sem dados brutos para %s; ranking não gerado", data_referencia)
        return

    por_ticker: dict[str, dict[str, dict]] = {}
    for bruto in brutos:
        por_ticker.setdefault(bruto.ticker, {})[bruto.tipo] = bruto.payload

    resultados: dict[str, dict[str, float]] = {}
    for ticker, dados in por_ticker.items():
        calculados = calcular_indicadores(
            dados.get("cotacao"), dados.get("fundamento"), dados.get("provento")
        )
        if not calculados.indicadores:
            logger.warning(
                "sem indicadores calculáveis para %s em %s; ativo fora do ranking",
                ticker,
                data_referencia,
            )
            continue
        if calculados.ausentes:
            logger.info(
                "indicadores indisponíveis para %s: %s",
                ticker,
                ", ".join(calculados.ausentes),
            )
        resultados[ticker] = calculados.indicadores
        for nome, valor in calculados.indicadores.items():
            repository.gravar_indicador(conn, ticker, data_referencia, nome, valor)

    scores = calcular_scores(resultados)
    itens = ordenar(scores)
    repository.gravar_ranking(conn, data_referencia, "atualizado", itens)
    conn.commit()

    logger.info("ranking calculado: %d ativos, data de referência %s", len(itens), data_referencia)
