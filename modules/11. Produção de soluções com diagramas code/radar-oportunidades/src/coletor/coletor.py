"""Coletor: orquestração de uma ingestão completa.

Fluxo (ver docs/diagrams/sequencia.mmd):
buscar no provedor → gravar dados brutos com data de referência →
acionar o Motor de ranking. Em falha do provedor, manter o último dado
e marcá-lo como desatualizado — nunca falhar em silêncio.
"""

import logging
import sqlite3
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeout

from storage import repository

from .ports import AcionadorMotor
from .provedor import LoteDados, ProvedorDados, ProvedorIndisponivel, ProvedorTimeout

logger = logging.getLogger("coletor")


def _buscar_com_timeout(provedor: ProvedorDados, timeout_segundos: float) -> LoteDados:
    executor = ThreadPoolExecutor(max_workers=1)
    try:
        return executor.submit(provedor.buscar).result(timeout=timeout_segundos)
    except FuturesTimeout as exc:
        raise ProvedorTimeout(
            f"provedor não respondeu em {timeout_segundos:.1f}s"
        ) from exc
    finally:
        executor.shutdown(wait=False)


def executar(
    conn: sqlite3.Connection,
    provedor: ProvedorDados,
    acionar_motor: AcionadorMotor,
    timeout_segundos: float = 10.0,
) -> None:
    """Executa uma ingestão completa.

    Falha do provedor não lança: mantém os dados anteriores, marca o ranking
    como desatualizado e registra erro no log. Erros inesperados propagam.
    """
    try:
        lote = _buscar_com_timeout(provedor, timeout_segundos)
    except (ProvedorIndisponivel, ProvedorTimeout) as exc:
        repository.marcar_ranking_desatualizado(conn)
        conn.commit()
        logger.error(
            "falha ao buscar dados do provedor; dados anteriores mantidos e "
            "marcados como desatualizados: %s",
            exc,
        )
        return

    for ativo in lote.ativos:
        repository.upsert_ativo(conn, ativo.ticker, ativo.nome, ativo.setor)
    for item in lote.itens:
        repository.gravar_bruto(conn, item.ticker, item.tipo, lote.data_referencia, item.payload)
    conn.commit()

    logger.info(
        "coleta concluída: %d ativos, %d registros brutos, data de referência %s",
        len(lote.ativos),
        len(lote.itens),
        lote.data_referencia,
    )

    acionar_motor(conn, lote.data_referencia)
