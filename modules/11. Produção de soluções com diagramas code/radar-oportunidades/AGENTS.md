# Contexto para agentes de desenvolvimento

Fonte de verdade da arquitetura deste sistema (proposta, ainda não implementada):

1. `docs/descricao.md` — escopo, responsabilidades, restrições e lacunas
2. `docs/diagrams/containers.mmd` — visão estrutural
3. `docs/diagrams/sequencia.mmd` — jornadas críticas

Regras:
- Respeitar os limites e responsabilidades dos containers; não mover lógica de ranking para a API ou para o Web App.
- Não assumir o que está listado como lacuna; perguntar ou registrar um ADR.
- Nunca apresentar o resultado como recomendação de investimento.
- Se código e diagramas divergirem, atualizar os diagramas no mesmo PR.
