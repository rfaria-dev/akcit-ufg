# Produção da Análise de Risco e Resumo Executivo

**Sistema de Gestão de Eventos — Empresa Eventus**

Atividade prática da unidade "Gerência de Projetos de Software Apoiada por Inteligência Artificial Generativa".

## Premissas da atividade

- **Cenário utilizado:** estudo de caso do curso — Sistema de Gestão de Eventos (Eventus), mesmo cenário do projeto "Análise e Especificação de Requisitos com IA Generativa" (módulo 10), garantindo consistência entre as unidades.
- **Referência de estrutura e estilo:** projeto do módulo 10, mantido na pasta `modules/10. Engenharia de Requisitos com Inteligência Artificial Generativa/`.
- **Nota sobre `examples.txt`:** o arquivo `examples.txt` fornecido na pasta desta atividade estava **vazio**; por isso, a estrutura, o estilo e a profundidade dos artefatos foram modelados com base no projeto do módulo 10 e no enunciado da atividade.

## Artefatos produzidos

| Artefato | Arquivo | Descrição |
|----------|---------|-----------|
| Identificação de riscos | `riscos/01_identificacao_riscos.md` | 15 riscos com categoria, causa, consequência, probabilidade e impacto |
| Análise de impactos e priorização | `riscos/02_analise_impacto_priorizacao.md` | Matriz probabilidade x impacto e ordenação por prioridade |
| Estratégias de resposta | `riscos/03_estrategias_resposta.md` | Estratégias (evitar, mitigar, transferir, aceitar) e ações por risco |
| Plano de comunicação | `riscos/04_plano_comunicacao.md` | Mapeamento dos riscos aos stakeholders e ações de comunicação |
| Resumo executivo | `resumo_executivo.md` | Síntese dos riscos, impactos, estratégias e próximos passos |
| Postagem do fórum | `postagem_forum.md` | Texto da postagem com os seis itens obrigatórios da atividade |

## Como a GenAI apoiou o desenvolvimento

A IA foi utilizada como ferramenta de **apoio à tomada de decisão**, não como substituição do julgamento humano:

- Proposição da lista inicial de riscos derivada dos requisitos, não funcionais e regras de negócio do módulo 10, organizando categoria, causa e consequência.
- Estruturação da matriz de probabilidade x impacto e das zonas de prioridade.
- Sugestão de estratégias de resposta (evitar, mitigar, transferir, aceitar) e do plano de comunicação por stakeholder.
- Redação assistida do resumo executivo e da postagem do fórum, sempre a partir dos dados levantados manualmente.

## Sugestões da IA: aproveitadas, modificadas ou descartadas

| Situação | Justificativa |
|----------|---------------|
| **Aproveitadas:** estrutura de identificação (categoria, causa, consequência, probabilidade, impacto), matriz probabilidade x impacto com zonas de prioridade, uso de estratégias evitar/mitigar/transferir/aceitar e plano de comunicação por stakeholder | Seguem as práticas de gestão de riscos do curso e atendem ao escopo do exercício |
| **Modificadas:** probabilidades e impactos propostos pela IA foram recalibrados manualmente; lista de riscos ajustada para eliminar itens genéricos sem base nos requisitos | As estimativas iniciais da IA não refletem o contexto real do negócio e exigem calibragem sob a ótica dos stakeholders |
| **Descartadas:** riscos genéricos de "qualquer sistema" (ex.: custo de infraestrutura sem contexto) e sugestões de monitoramento sem responsável definido | Sem base nos artefatos do módulo 10 ou fora do escopo da atividade |
| **Mantidas como pendentes:** valores definitivos de probabilidade/impacto e a regra exata do momento de reserva de vaga | Dependem de validação com organizadores, financeiro e TI antes da priorização final |

## Limitações, dificuldades e cuidados percebidos no uso da IA

- **Risco de "alucinação":** a IA tende a gerar riscos genéricos ou desconectados do cenário — cada item foi cruzado com os requisitos reais do módulo 10.
- **Estimativas subjetivas:** a IA não possui contexto real de probabilidade e impacto; os valores exigem calibragem humana.
- **Necessidade de revisão:** as sugestões foram tratadas como rascunho; a curadoria e a validação permaneceram humanas.
- **Cuidado com o excesso de confiança:** toda entrega da IA foi verificada contra os requisitos e regras de negócio antes de integrar os artefatos.

## Organização do repositório

```
produção da análise de risco e resumo executivo/
├── README.md
├── examples.txt          (vazio — fornecido pela atividade)
├── riscos/
│   ├── 01_identificacao_riscos.md
│   ├── 02_analise_impacto_priorizacao.md
│   ├── 03_estrategias_resposta.md
│   └── 04_plano_comunicacao.md
├── resumo_executivo.md
└── postagem_forum.md
```
