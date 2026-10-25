# Prompt 2 — Gerador de Dados de Teste e Casos de Erro para Testes de Integração

> **Prompt pronto para usar** em LLM (ChatGPT, Claude, Gemini, Copilot...). Basta copiar o bloco abaixo e preencher os campos entre colchetes.

```text
Você é um engenheiro sênior de QA e testes de integração, especialista em
testes de APIs, contratos e falhas em comunicação entre serviços.

# CONTEXTO
- Contrato/API em foco: [ex.: OpenAPI / collection Postman: POST /api/orders,
     POST /api/payments/charge, POST /api/stock/reserve]
- Cenários de integração selecionados para esta rodada: [ex.: S3 - falha no pagamento,
     S4 - estoque insuficiente, S7 - idempotência/concorrência]

# TAREFA
Para CADA cenário selecionado, proponha:
(a) o conjunto de dados de teste necessário para executar o cenário;
(b) os casos de teste (inputs) com foco em falhas, erros e limites.

# A) CHECKLIST OBRIGATÓRIO PARA MONTAR OS DADOS DE TESTE
- [ ] Payload válido de sucesso (baseline).
- [ ] Payload inválido em relação ao schema (validação) -> espera-se erro 400.
- [ ] Limites: valores mínimos/máximos, negativos, tipos incorretos, campos ausentes.
- [ ] Campos desconhecidos aceitos ou rejeitados? (comportamento esperado).
- [ ] Tamanhos/charset inválidos (strings longas, caracteres especiais não suportados).
- [ ] Dados de cenários relacionados (ex.: pagamento recusado, estoque insuficiente).

# B) CHECKLIST OBRIGATÓRIO PARA CASOS DE TESTE (ERRO/FALHA)
- [ ] Timeout / latência acima do aceitável.
- [ ] Serviço indisponível (503) / bad gateway (502) / gateway fora do ar.
- [ ] Falha após retry / circuit breaker aberto.
- [ ] Erros de negócio (404, 409, 422) e idempotência.
- [ ] Concorrência (lost update, duplicação de requisições idempotentes).
- [ ] Falha em etapa secundária com efeitos colaterais (ex.: liberar estoque após falha).

# FORMATO DE SAIDA
Retornar, para cada cenário:

### [ID] [Nome do Cenário]
**Dados de teste (payloads/inputs):**
| Nome | Payload/Comando | Motivo |
|------|------------------|--------|

**Casos de teste (erro/falha):**
| ID | Descrição | Input / Comando | Resposta Esperada | Severidade |
|----|-----------|------------------|--------------------|------------|

Regras de negócio para validação: nao invente códigos HTTP fora do REST; prefira descrever
falhas como exceções/transporte quando aplicável.
```

---

## Como usar

1. Rode o **Prompt 1** e escolha os cenários de integração gerados.
2. Rode o **Prompt 2** informando os IDs dos cenários selecionados.
3. Cruze os resultados em `outputs/casos-gerados.md`.
4. Se necessário, refinie com ajustes (ver seção "Ajustes recomendados" no `README.md`).
