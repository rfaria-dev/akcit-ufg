# Resultados — Prompt 2: Gerador de Dados de Teste e Casos de Erro para Testes de Integração

**Prompt utilizada:** `prompts/02-gerador-de-dados-e-casos-de-erro.md`
**Contexto:** `contexto-cenario.md` (checkout de e-commerce: front-end -> gateway -> order -> payment/stock, eventos via RabbitMQ)
**Cenários de integração selecionados para esta rodada:** falha de pagamento, estoque insuficiente, indisponibilidade/timeout/retry/circuit breaker, idempotência e concorrência.

## Cenários e Casos Gerados

### [SC-01] Falha de Pagamento (Recusado / Timeout) e Cancelamento do Pedido

**Dados de teste (payloads/inputs):**

| Nome                              | Payload/Comando                                                                                                                                                                                            | Motivo                                       |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| Baseline — aprovação de pagamento | `POST /api/payments/charge`: `{"orderId":"ord_1001","customerId":"cus_1001","paymentMethod":"credit_card","amount":499.90,"currency":"BRL"}`                                                               | Sucesso esperado; dispara reserva de estoque |
| Pagamento recusado                | `POST /api/payments/charge`: `{"orderId":"ord_1002","customerId":"cus_1001","paymentMethod":"credit_card","amount":120.00,"currency":"BRL","gatewayStatus":"DECLINED","declineCode":"insufficient_funds"}` | Falha de negócio; deve cancelar pedido       |
| Timeout de pagamento              | `POST /api/payments/charge`: `{"orderId":"ord_1003","customerId":"cus_1001","paymentMethod":"credit_card","amount":150.00,"currency":"BRL","gatewayStatus":"TIMEOUT"}` (latência 30s / SLA 5s)             | Falha de comunicação com gateway             |
| Pedido inexistente (consulta)     | `GET /api/orders/ord_9999`                                                                                                                                                                                 | Erro 404 esperado                            |

**Casos de teste (erro/falha):**

| ID       | Descrição                         | Input / Comando                      | Resposta Esperada                                                | Severidade |
| -------- | --------------------------------- | ------------------------------------ | ---------------------------------------------------------------- | ---------- |
| SC-01-01 | Baseline de pagamento aprovado    | charge válido (amount 499.90)        | 200/201; order PENDING→confirmada; payment.approved              | Alta       |
| SC-01-02 | Pagamento recusado cancela pedido | charge (amount 120.00, DECLINED)     | 402/422; order → CANCELLED; estoque liberado; payment.failed     | Alta       |
| SC-01-03 | Timeout de gateway de pagamento   | charge (amount 150.00, TIMEOUT, 30s) | 504/timeout; falha registrada; order cancelado; estoque liberado | Alta       |
| SC-01-04 | Consulta de pedido inexistente    | `GET /api/orders/ord_9999`           | 404                                                              | Média      |

---

### [SC-02] Estoque Insuficiente

**Dados de teste (payloads/inputs):**

| Nome                                      | Payload/Comando                                                                                         | Motivo           |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------- |
| Baseline — reserva com estoque suficiente | `POST /api/stock/reserve`: `{"orderId":"ord_2001","productId":"prd_3001","quantity":2}`                 | Sucesso esperado |
| Estoque insuficiente                      | `POST /api/stock/reserve`: `{"orderId":"ord_2002","productId":"prd_3001","quantity":5}` (disponível: 3) | Falha de negócio |

**Casos de teste (erro/falha):**

| ID       | Descrição                                 | Input / Comando                  | Resposta Esperada                                 | Severidade |
| -------- | ----------------------------------------- | -------------------------------- | ------------------------------------------------- | ---------- |
| SC-02-01 | Quantidade solicitada acima do disponível | reserve (quantity 5 > 3)         | 409/422; order → CANCELLED; estoque não consumido | Alta       |
| SC-02-02 | Quantidade inválida (zero/negativa)       | reserve (quantity -1)            | 400                                               | Alta       |
| SC-02-03 | Produto inexistente                       | reserve (productId prd_invalido) | 404                                               | Média      |

---

### [SC-03] Indisponibilidade / Timeout / Retry / Circuit Breaker nos Serviços

**Dados de teste (payloads/inputs):**

| Nome                                     | Payload/Comando                                        | Motivo                       |
| ---------------------------------------- | ------------------------------------------------------ | ---------------------------- |
| Baseline degradação — Order Service fora | `POST /api/orders` com Order Service retornando 503    | Cenário de indisponibilidade |
| Retry excedido — Payment Service lento   | charge com timeout downstream > SLA, retries esgotados | Falha após retry             |

**Casos de teste (erro/falha):**

| ID       | Descrição                                        | Input / Comando                                  | Resposta Esperada                                    | Severidade |
| -------- | ------------------------------------------------ | ------------------------------------------------ | ---------------------------------------------------- | ---------- |
| SC-03-01 | Order Service indisponível (API Gateway)         | `POST /api/orders` → Order Service 503           | Gateway responde 503/502                             | Alta       |
| SC-03-02 | Falha após retry / circuit breaker aberto        | charge → retries esgotados                       | 504/503; falha registrada; estoque liberado          | Alta       |
| SC-03-03 | Falha em etapa secundária com efeitos colaterais | payment.approved OK → stock reserve indisponível | Estoque não reservado; ação de compensação executada | Alta       |

---

### [SC-04] Idempotência e Concorrência

**Dados de teste (payloads/inputs):**

| Nome                                        | Payload/Comando                                                                            | Motivo                  |
| ------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------- |
| Baseline — duplicação de charge idempotente | `POST /api/payments/charge` com `idempotencyKey: idem_1001` (mesmo payload repetido)       | Cenário de idempotência |
| Baseline — concorrência em reserva          | `POST /api/stock/reserve` simultâneo: ord_3001 (qty 2) e ord_3002 (qty 2), estoque total 3 | Cenário de corrida      |

**Casos de teste (erro/falha):**

| ID       | Descrição                          | Input / Comando                                  | Resposta Esperada                                                        | Severidade |
| -------- | ---------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------ | ---------- |
| SC-04-01 | Duplicação de charge idempotente   | charge repetido com mesmo idempotencyKey/orderId | Resposta 200/201 idem; estoque reservado 1x; payment.approved emitido 1x | Alta       |
| SC-04-02 | Lost update em reserva concorrente | reserve simultâneo (qty 2 + qty 2, estoque 3)    | Uma reserva falha (409/422); estoque consistente, sem oversell           | Alta       |
| SC-04-03 | Pedido duplicado por idempotência  | `POST /api/orders` com mesmo `orderId`           | Resposta idempotente; sem duplicação                                     | Média      |

---

## Observações sobre os Resultados

- Os cenários gerados pelo **Prompt 2** (SC-01 a SC-04) são auto-suficientes, porém usam a numeração própria e não fazem 1:1 com os IDs do Prompt 1 (CT-01 a CT-08). Em uma próxima iteração, o prompt pode ser ajustado para receber como entrada os IDs dos cenários selecionados.
- Os códigos HTTP esperados estão como opções (ex.: `402/422`, `409/422`), refletindo ambiguidade inerente ao contexto não-ressolável pelo LLM.
