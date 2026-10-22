# Prompts usados (GenAI)

## Prompt 1 — Diagrama de containers
```
Com base na descrição abaixo, gere um diagrama Mermaid (flowchart LR) de containers
inspirado no C4. Mostre ator, containers, armazenamento e sistemas externos, com
rótulos nas setas. Não invente tecnologias, filas, microsserviços ou autenticação.
Retorne apenas o bloco mermaid.

<colar docs/descricao.md>
```

## Prompt 2 — Diagrama de sequência
```
Gere um diagrama de sequência Mermaid com duas partes: (1) ingestão agendada de
dados e cálculo do ranking e (2) consulta de oportunidades pelo investidor.
Use os mesmos componentes do diagrama de containers e inclua um fluxo alternativo
para indisponibilidade do provedor (alt/else). Retorne apenas o bloco mermaid.

<colar docs/descricao.md + diagrams/containers.mmd>
```
