# Critérios de Aceitação - Sistema de Gestão de Eventos (Eventus)

## Formato: Dado - Quando - Então (Given - When - Then)

---

## US01 - Visualizar Eventos Disponíveis

| Dado | Quando | Então |
|------|--------|-------|
| O participante está autenticado no sistema. | Acessa a seção de eventos. | O sistema apresenta a lista de eventos disponíveis com nome, data, horário, vagas e status. |
| O participante visualiza a lista de eventos. | Seleciona um evento. | O sistema exibe detalhes do evento, incluindo programação e políticas. |
| Não existem eventos cadastrados. | O participante acessa a seção de eventos. | O sistema informa que não há eventos disponíveis. |

---

## US02 - Inscrever-se em Evento Gratuito

| Dado | Quando | Então |
|------|--------|-------|
| O participante está autenticado e o evento gratuito possui vagas. | Solicita inscrição no evento. | O sistema registra a inscrição com status "Confirmada" e decrementa vagas disponíveis. |
| O participante está autenticado e o evento gratuito está lotado. | Solicita inscrição no evento. | O sistema oferece entrada na lista de espera. |

---

## US03 - Inscrever-se em Evento Pago

| Dado | Quando | Então |
|------|--------|-------|
| O participante está autenticado e o evento pago possui vagas. | Solicita inscrição no evento. | O sistema registra a inscrição com status "Pendente de Pagamento". |
| A inscrição está com pagamento pendente. | O participante realiza o pagamento. | O sistema registra o pagamento e aguarda confirmação da equipe financeira. |
| A equipe financeira confirma o pagamento. | O pagamento é validado. | O sistema altera o status para "Confirmada" e envia comprovante ao participante. |
| O prazo de pagamento expira. | O pagamento não é confirmado no prazo. | O sistema altera o status para "Expirada" e promove participante da lista de espera (se aplicável). |

---

## US04 - Receber Comprovante de Inscrição

| Dado | Quando | Então |
|------|--------|-------|
| A inscrição foi confirmada (gratuito) ou pagamento confirmado (pago). | A inscrição é concluída. | O sistema gera comprovante com identificação do evento, participante e status da inscrição. |
| O comprovante está disponível. | O participante acessa suas inscrições. | O sistema disponibiliza o comprovante para consulta e download. |

---

## US05 - Cancelar Inscrição

| Dado | Quando | Então |
|------|--------|-------|
| O participante possui inscrição confirmada e o evento permite cancelamento. | Solicita cancelamento dentro do prazo. | O sistema altera o status para "Cancelada" e libera a vaga. |
| O participante possui inscrição confirmada em evento pago e cancelamento é elegível para reembolso. | O cancelamento é processado. | O sistema classifica o caso como reembolsável e notifica a equipe financeira. |
| O evento não permite cancelamento. | O participante tenta cancelar. | O sistema impede o cancelamento e informa o motivo. |
| O cancelamento é processado e há participantes na lista de espera. | A vaga é liberada. | O sistema promove o primeiro participante da lista de espera. |

---

## US06 - Emitir Certificado

| Dado | Quando | Então |
|------|--------|-------|
| O evento está encerrado e o participante é elegível. | Solicita emissão do certificado. | O sistema gera o certificado e disponibiliza para consulta/download. |
| O evento está encerrado e o participante não é elegível. | Solicita emissão do certificado. | O sistema informa que o participante não atende aos critérios de elegibilidade. |

---

## US07 - Gerenciar Eventos (Organizador)

| Dado | Quando | Então |
|------|--------|-------|
| O organizador está autenticado com perfil autorizado. | Cria um novo evento com dados válidos. | O sistema registra o evento e o disponibiliza para publicação. |
| O organizador publica um evento. | O evento é publicado. | O sistema torna o evento visível para inscrições. |
| O organizador edita um evento publicado. | As alterações são salvas. | O sistema atualiza as informações do evento. |

---

## US08 - Configurar Vagas por Atividade

| Dado | Quando | Então |
|------|--------|-------|
| O organizador está gerenciando um evento. | Define a quantidade de vagas por atividade. | O sistema atualiza o limite de vagas e reflete na disponibilidade. |

---

## US09 - Acompanhar Inscritos em Tempo Real

| Dado | Quando | Então |
|------|--------|-------|
| O organizador acessa o painel de gestão. | Visualiza os indicadores. | O sistema exibe total de inscritos, confirmados, pendentes e lista de espera atualizados. |

---

## US10 - Confirmar Pagamento

| Dado | Quando | Então |
|------|--------|-------|
| A equipe financeira acessa a lista de pagamentos pendentes. | Confirma um pagamento. | O sistema altera o status da inscrição para "Confirmada" e envia comprovante ao participante. |
| A equipe financeira recusa um pagamento. | O pagamento é invalidado. | O sistema notifica o participante sobre a recusa. |

---

## US11 - Processar Reembolso

| Dado | Quando | Então |
|------|--------|-------|
| Existe inscrição cancelada elegível para reembolso. | A equipe financeira processa o reembolso. | O sistema registra o reembolso e notifica o participante. |
| A inscrição não é elegível para reembolso. | A equipe financeira avalia a solicitação. | O sistema informa o motivo da não elegibilidade. |

---

## US12 - Consultar Participantes (Palestrante)

| Dado | Quando | Então |
|------|--------|-------|
| O palestrante está autenticado e vinculado a atividades. | Acessa a lista de participantes de uma atividade. | O sistema exibe os participantes inscritos com os campos autorizados pela política de privacidade. |
| Não há participantes inscritos na atividade. | O palestrante acessa a lista. | O sistema informa que não há participantes inscritos. |
