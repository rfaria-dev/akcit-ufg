"""criar_agendador: job de ingestão com o intervalo configurado."""

from datetime import timedelta

from coletor.agendador import criar_agendador


def test_cria_job_de_ingestao_com_intervalo():
    chamadas = []
    agendador = criar_agendador(60, lambda: chamadas.append(1))

    job = agendador.get_job("ingestao")
    assert job is not None
    assert job.trigger.interval == timedelta(minutes=60)
    # sem start(), não há thread nem estado a encerrar
