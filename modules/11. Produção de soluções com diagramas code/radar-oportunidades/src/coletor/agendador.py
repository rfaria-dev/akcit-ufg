"""Agendamento da ingestão (APScheduler, sem fila — ver ADR 0001)."""

from collections.abc import Callable

from apscheduler.schedulers.background import BackgroundScheduler


def criar_agendador(
    intervalo_minutos: int, executar: Callable[[], None]
) -> BackgroundScheduler:
    """Agendador com o job de ingestão repetido a cada `intervalo_minutos`."""
    agendador = BackgroundScheduler()
    agendador.add_job(executar, "interval", minutes=intervalo_minutos, id="ingestao")
    return agendador
