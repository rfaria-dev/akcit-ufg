# ADR 0003 — Ingestão do Coletor (mock, periodicidade, timeout e retry)

- **Status:** Aprovada
- **Data:** 2026-10-22
- **Decisores:** autor do projeto (assunções do plano aprovado em 2026-10-22)

## Contexto

`docs/descricao.md` deixa como lacunas o provedor de dados, a licença, a periodicidade e o tratamento de retries. O `AGENTS.md` obriga a usar provedor mockado atrás de interface e a nunca falhar em silêncio na ingestão. O diagrama de sequência define o fluxo: buscar → gravar brutos com data de referência → acionar cálculo; em indisponibilidade ou timeout, marcar dados como desatualizados.

## Decisão

- **Provedor mockado** `ProvedorMock` (obrigatório pelo AGENTS.md): universo fixo de 10 ativos da B3 com cotações, fundamentos e proventos determinísticos; cenários `sucesso`, `falha` e `timeout` controlados na construção.
- **Periodicidade padrão diária (1440 min)**, configurável por `RADAR_INTERVALO_MINUTOS` ou `--intervalo-minutos` (lacuna assumida; sem requisito nos docs).
- **Timeout de 10 s** na chamada do provedor (thread + `future.result(timeout)`); estouro vira `ProvedorTimeout`, com o mesmo tratamento de falha.
- **Sem retry automático no v1** (lacuna assumida): a próxima execução agendada recupera.
- **Proventos são coletados como dado bruto, sem ajuste de preço** (lacuna de ajustes por proventos/desdobramentos fica para versões futuras).
- **Falha do provedor:** mantém os dados anteriores, marca o snapshot de ranking mais recente como `desatualizado` (ver ADR 0002) e registra `ERROR` no log — nunca falha em silêncio. Erros inesperados propagam.
- **Acionamento do Motor in-process por porta** (`AcionadorMotor`), coerente com o ADR 0001.

## Consequências

- A API exibirá o ranking anterior com status `desatualizado` enquanto o provedor estiver fora do ar.
- O mock nunca integra API real: nenhuma chave, licença ou rede externa.
- Um dia sem coleta deixa o último snapshot marcado como desatualizado — comportamento visível ao investidor, conforme os diagramas.
