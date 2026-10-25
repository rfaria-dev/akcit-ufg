# Testes de Integração com Geração Assistida por LLM

Repositório criado para o fórum sobre **testes com IA generativa**, com foco em **testes de integração**.

## Objetivo

Explorar como prompts podem apoiar a geração de casos de teste de integração entre componentes de um sistema,
com foco em comunicação entre serviços REST, módulos internos e fluxo front-end/back-end.

## Estrutura do Repositório

```text
.
├── contexto-cenario.md                                  # Contexto do cenário de integração usado como base
├── prompts/
│   ├── 01-gerador-de-cenarios-de-integracao.md         # Prompt 1: geração de cenários de integração
│   └── 02-gerador-de-dados-e-casos-de-erro.md         # Prompt 2: dados de teste + casos de erro/falha
├── outputs/
│   ├── 01-cenarios-gerados.md                          # Resultado da execução do Prompt 1
│   └── 02-dados-e-casos-erro-gerados.md               # Resultado da execução do Prompt 2
└── README.md                                            # Este arquivo
```

## Como os Prompts Foram Usados

### Prompt 1 — Gerador de Cenários de Integração

- **Entrada:** contexto do sistema (componentes, protocolos, contratos, regras de negócio).
- **Saída:** suíte de cenários de integração em formato de tabela.
- **Execução:** com LLM generativa, usando o contexto de um fluxo de checkout de e-commerce
  (front-end -> API Gateway -> Order Service -> Payment/Stock Services, eventos via RabbitMQ).

### Prompt 2 — Gerador de Dados de Teste e Casos de Erro

- **Entrada:** contexto + seleção de cenários críticos para a rodada.
- **Saída:** dados de teste (payloads válidos/inválidos/limites) e casos de teste de falha
  (timeout, 503, retry, circuit breaker, idempotência, concorrência, efeitos colaterais).

## Casos de Teste de Integração Gerados

- **Prompt 1:** 8 cenários cobrindo fluxo feliz, falhas de negócio, resiliência, idempotência,
  consistência eventual, falha de infraestrutura e concorrência.
- **Prompt 2:** dados de teste e casos de erro para falhas de pagamento, estoque insuficiente,
  indisponibilidade/timeout/retry/circuit breaker, idempotência e concorrência.

Detalhes completos em `outputs/`.
