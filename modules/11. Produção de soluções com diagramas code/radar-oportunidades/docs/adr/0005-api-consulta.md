# ADR 0005 — Contrato de consulta da API

- **Status:** Aprovada
- **Data:** 2026-10-22
- **Decisores:** autor do projeto (assunções do plano aprovado)

## Contexto

`docs/descricao.md` deixa em aberto requisitos de desempenho e autenticação. O diagrama de sequência fixa a consulta: `GET /oportunidades` com critérios, retornando ativos ranqueados, data de referência e status. O `AGENTS.md` exige que toda resposta de ranking inclua data de referência e status, que o score seja explicável, que o aviso de não recomendação apareça na API e na UI, e veta autenticação.

## Decisão

- **`GET /oportunidades`** com filtros opcionais: `setor`, `min_<indicador>`/`max_<indicador>` (7 indicadores v1) e `limite` (padrão 20, 1–100).
- **Filtros estritos**: ativo sem o indicador filtrado é reprovado no filtro.
- **Sem paginação no v1** (desempenho é lacuna): `limite` trunca a lista.
- **Sem ranking → `404`** com orientação para executar a coleta; ranking existente com zero itens após filtros → `200` com lista vazia (data de referência e status permanecem).
- **Aviso de não recomendação no corpo de toda resposta** (`aviso`), além da UI.
- **Sem autenticação** (vetada pelo AGENTS.md; a menção na descrição fica como lacuna não atendida).
- OpenAPI gerado automaticamente pelo FastAPI (pendência do README §5).

## Consequências

- A posição exibida é a posição no ranking completo, preservada após filtros.
- `limite` não substitui paginação: consultas grandes são truncadas, sem cursor.
- O endpoint é somente leitura: não altera estado do Armazenamento.
