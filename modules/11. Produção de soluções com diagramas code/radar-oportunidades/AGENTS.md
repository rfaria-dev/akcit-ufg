# Contexto para agentes de desenvolvimento

Sistema **proposto, ainda não implementado**. A arquitetura está documentada; seu trabalho é implementá-la com aderência a ela.

## Fonte de verdade

1. `docs/descricao.md` — escopo, responsabilidades, restrições e lacunas
2. `docs/diagrams/containers.mmd` — visão estrutural
3. `docs/diagrams/sequencia.mmd` — jornadas críticas

## Como trabalhar

- Antes de codar, proponha um plano e aguarde aprovação.
- Implemente **um container por vez**, na ordem: Armazenamento, Coletor, Motor de ranking, API, Web App.
- Código em `src/<container>/`; testes ao lado, em `tests/<container>/`.
- Stack não definida na documentação: proponha e registre a escolha em `docs/adr/NNN-titulo.md` (contexto, decisão, consequências). Não adote nada sem aprovação.
- Provedor de dados: use implementação **mockada** atrás de uma interface; não integre APIs reais.
- Cada etapa termina com: testes passando, lista das decisões assumidas e das divergências com os diagramas.

## Regras de arquitetura

- Respeitar os limites dos containers. Lógica de indicadores e ranking só no Motor; a API apenas lê e serve; o Web App apenas exibe.
- Coleta e cálculo são separados; o cálculo é acionado pelo Coletor.
- Falha do provedor: manter o último dado e marcá-lo como **desatualizado**; nunca falhar em silêncio.
- Toda resposta de ranking inclui a **data de referência** e o status do dado.
- O score é **explicável**: expor os indicadores que contribuíram.

## Restrições

- Não é recomendação de investimento: a UI e a API devem exibir o aviso; evite linguagem como "compre" ou "venda".
- O que está em "lacunas" não é decisão aprovada: pergunte ou registre ADR.
- Não crie autenticação, filas, cache, ordens, carteira ou integração com corretoras (fora de escopo).

## Divergências

Se o código e os diagramas divergirem, atualize os diagramas (`.mmd` e o bloco no README) no mesmo commit.

## Convenções

- Português (pt-BR) em docs e mensagens de commit; Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`).
- Um commit por etapa.
