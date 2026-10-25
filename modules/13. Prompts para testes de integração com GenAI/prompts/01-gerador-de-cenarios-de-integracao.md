# Prompt 1 — Gerador de Cenários de Teste de Integração

> **Prompt pronto para usar** em LLM (ChatGPT, Claude, Gemini, Copilot...). Basta copiar o bloco abaixo e preencher os campos entre colchetes.

```text
Você é um especialista sênior em testes de integração e sistemas distribuídos,
com experiência em testes de APIs, comunicação entre microsserviços e
integração front-end/back-end.

# CONTEXTO DO SISTEMA
- Produto: [descreva o produto/sistema, ex.: plataforma de e-commerce]
- Componentes que se comunicam: [ex.: Front-end (SPA) <-> API Gateway <-> Order Service;
     Order Service <-> Payment Service; Order Service <-> Stock Service; eventos via RabbitMQ]
- Protocolo e formato: [ex.: REST/JSON via HTTPS; sincronia gateway<->order; chamada síncrona
     order->payment e order->stock; eventos assíncronos via RabbitMQ]
- Contratos relevantes: [ex.: OpenAPI do Gateway: POST /orders, POST /payments/charge, POST /stock/reserve]

# OBJETIVO
Com base no contexto acima, proponha uma suíte inicial de [N] cenários de teste de
integração para o fluxo de [área de negócio, ex.: checkout/pagamentos].

# O QUE CONSTITUI UM CENÁRIO DE INTEGRAÇÃO BEM-DEFINIDO
- Foca na interação/contrato entre componentes, não apenas no comportamento isolado.
- Inclui caminho feliz, caminhos alternativos e casos de borda.
- Considera falhas de infraestrutura, resiliência, idempotência e concorrência
  quando o protocolo/protocolo de consistência permitir.

# REGRAS
1. Não repita cobertura já existente em testes de unidade.
2. Priorize interações críticas (ex.: pedido -> pagamento -> estoque).
3. Nao ultrapasse [8] cenários.

# FORMATO DE SAIDA
Retorne um documento em Markdown contendo UMA tabela:

| ID | Nome | Objetivo | Componentes Envolvidos | Gatilho | Passo a Passo Resumido | Expectativas de Integração | Casos de Borda |
|----|------|----------|------------------------|---------|-------------------------|---------------------------|----------------|

Ao final, acrescente uma seção "Justificativa das escolhas" com 3 a 5 linhas.
```

---

## Como usar

1. Cole o prompt no LLM escolhido.
2. Preencha os campos entre colchetes.
3. Peça: `Aplique o prompt acima e retorne o resultado.` (ou ajuste o N).
4. Salve a resposta em `outputs/cenarios-gerados.md`.
5. Encaminhe o resultado ao **Prompt 2** para gerar dados e casos de erro.
