"""CLI do Coletor.

Uso:
    python -m coletor --once [--db radar.db] [--cenario sucesso]
    python -m coletor --agendar [--db radar.db] [--intervalo-minutos 1440]
"""

import argparse
import logging
import os
import sqlite3
import sys
import time

from storage.db import conectar, inicializar

from .agendador import criar_agendador
from .coletor import executar
from .provedor_mock import ProvedorMock

logger = logging.getLogger("coletor")


def _configurar_logging() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
    )


def _motor_pendente(conn: sqlite3.Connection, data_referencia: str) -> None:
    """Stub até a Etapa 3: o wiring apontará para o Motor real."""
    logger.warning(
        "motor de ranking ainda não implementado; cálculo não acionado (data_referencia=%s)",
        data_referencia,
    )


def _argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Coletor de dados do Radar de Oportunidades")
    modo = parser.add_mutually_exclusive_group(required=True)
    modo.add_argument("--once", action="store_true", help="executa uma ingestão e encerra")
    modo.add_argument(
        "--agendar", action="store_true", help="mantém a ingestão agendada em execução"
    )
    parser.add_argument(
        "--db", default=os.environ.get("RADAR_DB", "radar.db"), help="caminho do SQLite"
    )
    parser.add_argument(
        "--cenario",
        default="sucesso",
        choices=["sucesso", "falha", "timeout"],
        help="cenário do provedor mockado",
    )
    parser.add_argument(
        "--intervalo-minutos",
        type=int,
        default=int(os.environ.get("RADAR_INTERVALO_MINUTOS", "1440")),
        help="intervalo entre ingestões (modo --agendar)",
    )
    return parser.parse_args()


def main(argv: list[str] | None = None) -> int:
    args = _argumentos()
    _configurar_logging()

    conn = conectar(args.db)
    inicializar(conn)
    provedor = ProvedorMock(cenario=args.cenario)

    def rodar() -> None:
        executar(conn, provedor, _motor_pendente)

    if args.once:
        rodar()
        return 0

    agendador = criar_agendador(args.intervalo_minutos, rodar)
    agendador.start()
    logger.info("ingestão agendada a cada %d minutos; Ctrl+C para encerrar", args.intervalo_minutos)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        agendador.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(main())
