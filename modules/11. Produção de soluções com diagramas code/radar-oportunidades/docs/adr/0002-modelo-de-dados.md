# ADR 0002 — Modelo de dados v1 do Armazenamento

- **Status:** Aprovada
- **Data:** 2026-10-22
- **Decisores:** autor do projeto (assunção registrada conforme AGENTS.md: modelo de dados é lacuna na descrição)

## Contexto

`docs/descricao.md` lista "modelo de dados" e "política de retenção" como lacunas. O container Armazenamento precisa de um schema v1 para as etapas seguintes (Coletor grava dados brutos; Motor grava indicadores e ranking; API lê).

## Decisão

Schema em `src/storage/schema.sql` (SQLite, sem ORM — ver ADR 0001):

- `ativos(ticker PK, nome, setor)` — universo de ativos.
- `dados_brutos(ticker, tipo ∈ {cotacao, fundamento, provento}, data_referencia, payload JSON, coletado_em)` — chave natural `(ticker, tipo, data_referencia)`, upsert na regravação.
- `indicadores(ticker, data_referencia, indicador, valor REAL)` — chave natural `(ticker, indicador, data_referencia)`.
- `rankings(id, data_referencia, status ∈ {atualizado, desatualizado}, calculado_em)` — um snapshot por execução do Motor.
- `ranking_itens(ranking_id, posicao, ticker, score, contribuicoes JSON)` — explicação do score por ativo.

Decisões associadas:

- **O status do dado vive no snapshot de ranking** (é o que a API serve): falha do provedor marca o ranking mais recente como `desatualizado` e mantém os dados anteriores — regra do AGENTS.md ("manter o último dado e marcá-lo como desatualizado").
- `data_referencia` é a data do dado no provedor (string ISO `YYYY-MM-DD`), não a data da coleta; `coletado_em`/`calculado_em` em UTC ISO 8601.
- Valores em `REAL` (float); payloads e contribuições em colunas de texto com JSON.
- Sem política de expurgo no v1 (retenção é lacuna): snapshots acumulam.

## Consequências

- A API sempre devolve `data_referencia` + `status` junto do ranking (regra do AGENTS.md), lidos do snapshot.
- "Desatualizado" é uma marca no snapshot mais recente, não um dado apagado — o dado anterior permanece consultável.
- Mudanças futuras de schema exigem editar `schema.sql` e recriar o banco em desenvolvimento (sem migrações — ver ADR 0001).
