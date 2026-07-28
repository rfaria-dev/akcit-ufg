# Análise e Especificação de Requisitos com IA Generativa

**Sistema de Gestão de Eventos — Empresa Eventus**

## Artefatos de especificação produzidos

| Artefato | Quantidade | Descrição |
|----------|------------|-----------|
| Histórias de Usuário | 17 | Organizadas por perfil (participante, organizador, financeiro, palestrante) |
| Casos de Uso | 9 | Fluxos principais e alternativos detalhados |
| Critérios de Aceitação | Tabelas Given-When-Then | Condições objetivas e verificáveis por história |
| Protótipos de Interface | 6 wireframes | Telas principais em formato textual |

## Por que esses artefatos foram considerados adequados

- **Histórias de usuário** comunicam necessidades sob a perspectiva do usuário, favorecendo alinhamento com stakeholders não técnicos.
- **Casos de uso** detalham fluxos de interação e situações de exceção, reduzindo ambiguidades comportamentais.
- **Critérios de aceitação** (Given-When-Then) estabelecem condições objetivas de verificação, servindo como base para testes.
- **Protótipos** facilitam a validação visual da interface antes do desenvolvimento, reduzindo retrabalho.

Em conjunto, esses artefatos permitem evoluir da elicitação para uma especificação consistente, testável e auditável.

## Como a GenAI apoiou o desenvolvimento

A IA foi utilizada como ferramenta de **apoio à tomada de decisão**, não como substituição do julgamento humano:

- Organização da elicitação em requisitos funcionais, não funcionais e regras de negócio.
- Identificação de ambiguidades, inconsistências e lacunas que exigem validação com stakeholders.
- Sugestão do conjunto de artefatos (histórias de usuário + casos de uso + critérios de aceitação + protótipos).
- Elaboração de versões iniciais dos artefatos, posteriormente revisados e ajustados.

## Sugestões da IA: aproveitadas, modificadas ou descartadas

| Situação | Justificativa |
|----------|---------------|
| **Aproveitadas:** separação em pastas `analise/` e `especificacao/`, checklist de stakeholders, estrutura de histórias/casos de uso/critérios/protótipos | Seguem o padrão do curso e atendem ao escopo do exercício |
| **Modificadas:** fluxos registrados em formato textual (nos casos de uso) em vez de diagrama formal | Priorizou-se rapidez na validação funcional antes do detalhamento gráfico |
| **Descartadas:** diagrama de estados da inscrição e matriz de rastreabilidade completa | Complementares para iterações futuras; foco nos artefatos principais |
| **Mantidas como pendentes:** métricas quantitativas de RNF (SLA, tempos exatos) | Valores dependem de validação técnica e de negócio com stakeholders |

## Organização do repositório

```
Análise e Especificação de Requisitos com IA Generativa/
├── README.md
├── analise/
│   ├── requisitos_funcionais.md
│   ├── requisitos_nao_funcionais.md
│   ├── regras_de_negocio.md
│   ├── duvidas-e-lacunas.md
│   └── checklist_stakeholders.md
└── especificacao/
    ├── 01_historias_usuario.md
    ├── 02_casos_uso.md
    ├── 03_criterios_aceitacao.md
    └── 04_prototipos.md
```
