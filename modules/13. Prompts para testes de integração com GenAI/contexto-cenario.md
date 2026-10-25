# Contexto do Cenário de Integração

> Este contexto é o ponto de partida obrigatório para os prompts de geração de testes de integração.

## Produto

Plataforma de e-commerce (MVP) com fluxo de checkout.

## Componentes e comunicação

1. **Front-end (SPA React)** <-> **API Gateway REST/JSON** via HTTPS (Bearer token JWT).
2. **API Gateway** -> **Order Service** (chamada síncrona REST/JSON).
3. **Order Service** -> **Payment Service** (REST/JSON, síncrono).
4. **Order Service** -> **Stock Service** (REST/JSON, síncrono).
5. **RabbitMQ** (eventos assíncronos): `order.created`, `payment.approved`, `payment.failed`, `stock.reserved`.

## Contratos relevantes (representação)

- `POST /api/orders` — cria pedido (status inicial `PENDING`).
- `POST /api/payments/charge` — autoriza/estiliza pagamento (aprovado/recusado).
- `POST /api/stock/reserve` — reserva estoque para um pedido.
- `GET /api/orders/{id}` — consulta status.

## Regras de negócio relevantes para integração

- Pedido começa `PENDING`.
- Ao aprovar pagamento, Order Service tenta reservar estoque; se falhar por falta, cancela pedido.
- Se pagamento falhar/timeout, Order Service registra falha e libera estoque (estornável).
- Evento `payment.approved` confirma reserva no Stock Service (fluxo assíncrono).

## Objetivo da suíte de integração

Validar contratos, propagação de falhas, consistência transacional e resiliência entre front-end,
gateway, order, payment, stock e mensageria.
