# Protótipos de Interface - Sistema de Gestão de Eventos (Eventus)

## Objetivo

Representar visualmente as principais telas do sistema para validação com stakeholders. Protótipos de baixa fidelidade (wireframes textuais).

---

## Tela 1 - Catálogo de Eventos (Participante)

```
+-----------------------------------------------------------+
| LOGO Eventus                             [Perfil] [Sair]  |
+-----------------------------------------------------------+
| Buscar evento: [_______________________] (Filtrar)        |
| Categoria: [Todos]  Data: [__/__/____]  Tipo: [Grat/Pago]|
+-----------------------------------------------------------+
| Evento: Congresso Inovação 2026                           |
| Data: 15/09/2026   Vagas: 42/100   Tipo: Pago             |
| [Ver detalhes] [Inscrever-se]                             |
+-----------------------------------------------------------+
| Evento: Workshop IA Aplicada                              |
| Data: 15/09/2026   Vagas: ESGOTADO   Tipo: Gratuito       |
| [Ver detalhes] [Entrar na lista de espera]                |
+-----------------------------------------------------------+
```

**Pontos para validar com stakeholders:**
- Informações mínimas exibidas no card de evento.
- Destaque de lotação e lista de espera.

---

## Tela 2 - Detalhe do Evento e Inscrição

```
+-----------------------------------------------------------+
| Evento: Workshop IA Aplicada                              |
| Data/Hora: 15/09/2026 10:00-12:00                         |
| Local: Sala A / Online                                    |
| Vagas disponíveis: 0                                      |
+-----------------------------------------------------------+
| Políticas do evento                                       |
| - Cancelamento: permitido até 48h antes                  |
| - Reembolso: parcial até 7 dias antes                    |
| - Certificado: mediante presença                          |
+-----------------------------------------------------------+
| [Entrar na lista de espera]                               |
+-----------------------------------------------------------+
```

**Pontos para validar:**
- Exibição transparente das políticas no momento da inscrição.
- Mensagens de restrição de negócio.

---

## Tela 3 - Minhas Inscrições (Participante)

```
+----------------------------------------------------------------+
| Minhas Inscrições                                               |
+----------------------------------------------------------------+
| Evento               | Status              | Ações              |
| Congresso Inovação   | Confirmada          | [Comprovante]      |
| Workshop IA Aplicada | Lista de espera     | [Cancelar fila]    |
| Evento Corporativo   | Pendente pagamento  | [Pagar agora]      |
+----------------------------------------------------------------+
```

**Pontos para validar:**
- Estados de inscrição que precisam ser visíveis.
- Ações permitidas por estado.

---

## Tela 4 - Painel do Organizador

```
+-----------------------------------------------------------+
| Painel do Organizador                                     |
+-----------------------------------------------------------+
| Total inscritos hoje: 238                                 |
| Vagas restantes (eventos ativos): 74                      |
| Lista de espera total: 31                                 |
+-----------------------------------------------------------+
| [Criar evento] [Gerenciar atividades] [Exportar inscritos]|
+-----------------------------------------------------------+
| Evento: Congresso Inovação                                |
| Confirmados: 180  Pendentes: 22  Lista espera: 8          |
| [Ver participantes] [Ajustar vagas] [Políticas]           |
+-----------------------------------------------------------+
```

**Pontos para validar:**
- Indicadores essenciais para operação em tempo real.
- Permissões de alteração de vagas e políticas.

---

## Tela 5 - Painel Financeiro

```
+--------------------------------------------------------------+
| Pagamentos Pendentes de Confirmação                          |
+--------------------------------------------------------------+
| Participante   | Evento                | Valor | Ações       |
| Ana Souza      | Congresso Inovação    | 350   | [Confirmar] |
| João Lima      | Workshop Premium      | 120   | [Recusar]   |
+--------------------------------------------------------------+
| Reembolsos                                                   |
| Participante   | Evento                | Regra | [Processar] |
+--------------------------------------------------------------+
```

**Pontos para validar:**
- Fluxo operacional do financeiro.
- Regra de reembolso exibida junto ao pedido.

---

## Tela 6 - Área do Palestrante

```
+-----------------------------------------------------------+
| Minhas Atividades                                         |
+-----------------------------------------------------------+
| Oficina Engenharia de Requisitos                          |
| Horário: 15/09/2026 14:00-16:00                           |
| Inscritos: 45                                              |
| [Ver lista de participantes]                               |
+-----------------------------------------------------------+
```

**Pontos para validar:**
- Campos de dados visíveis dos participantes.
- Necessidade de exportação da lista.

---

## Jornada de Referência para Demo

1. Participante localiza evento e inicia inscrição.
2. Sistema valida vaga e regra de pagamento.
3. Inscrição muda de estado e gera comprovante.
4. Participante acompanha status e cancela, se permitido.
5. Organizadores e financeiro gerenciam confirmações e exceções.
6. Ao final do evento, certificado é disponibilizado conforme elegibilidade.
