# Casos de Uso - Sistema de Gestão de Eventos (Eventus)

---

## CU01 - Visualizar Eventos Disponíveis

| Campo | Descrição |
|-------|-----------|
| **Nome** | Visualizar Eventos Disponíveis |
| **Objetivo** | Permitir que o participante consulte a lista de eventos disponíveis para inscrição. |
| **Ator principal** | Participante |
| **Pré-condição** | O participante deve estar autenticado no sistema. |
| **Fluxo principal** | 1. O participante acessa a seção de eventos. 2. O sistema exibe a lista de eventos com informações essenciais (nome, data, horário, vagas, status). 3. O participante seleciona um evento para ver detalhes. 4. O sistema exibe detalhes do evento, incluindo programação e políticas. |
| **Fluxo alternativo** | Caso não existam eventos disponíveis, o sistema informa que não há eventos no momento. |
| **Pós-condição** | As informações do evento são apresentadas ao participante. |

---

## CU02 - Inscrever-se em Evento Gratuito

| Campo | Descrição |
|-------|-----------|
| **Nome** | Inscrever-se em Evento Gratuito |
| **Objetivo** | Permitir que o participante realize inscrição em um evento sem necessidade de pagamento. |
| **Ator principal** | Participante |
| **Pré-condição** | O participante deve estar autenticado e o evento deve possuir vagas disponíveis. |
| **Fluxo principal** | 1. O participante seleciona um evento gratuito. 2. O sistema verifica disponibilidade de vagas. 3. O sistema cria a inscrição com status "Confirmada". 4. O sistema envia comprovante de inscrição. 5. O sistema atualiza o painel de inscritos. |
| **Fluxo alternativo** | Caso o evento esteja lotado, o sistema oferece entrada na lista de espera. |
| **Pós-condição** | A inscrição é registrada e confirmada. |

---

## CU03 - Inscrever-se em Evento Pago

| Campo | Descrição |
|-------|-----------|
| **Nome** | Inscrever-se em Evento Pago |
| **Objetivo** | Permitir que o participante realize inscrição em um evento com pagamento. |
| **Ator principal** | Participante |
| **Pré-condição** | O participante deve estar autenticado e o evento deve possuir vagas disponíveis. |
| **Fluxo principal** | 1. O participante seleciona um evento pago. 2. O sistema verifica disponibilidade de vagas. 3. O sistema cria a inscrição com status "Pendente de Pagamento". 4. O participante realiza o pagamento. 5. A equipe financeira confirma o pagamento. 6. O sistema altera o status para "Confirmada". 7. O sistema envia comprovante e atualiza o painel. |
| **Fluxo alternativo** | Caso o prazo de pagamento expire, o sistema altera o status para "Expirada" e promove participante da lista de espera (se aplicável). |
| **Pós-condição** | A inscrição é registrada e confirmada após pagamento. |

---

## CU04 - Cancelar Inscrição

| Campo | Descrição |
|-------|-----------|
| **Nome** | Cancelar Inscrição |
| **Objetivo** | Permitir que o participante cancele sua inscrição respeitando as políticas do evento. |
| **Ator principal** | Participante |
| **Pré-condição** | O participante deve possuir inscrição confirmada no evento. |
| **Fluxo principal** | 1. O participante acessa suas inscrições. 2. O participante solicita o cancelamento. 3. O sistema valida a política de cancelamento do evento. 4. O sistema altera o status para "Cancelada". 5. Se evento pago, o sistema avalia elegibilidade de reembolso. 6. O sistema notifica o participante sobre o resultado. 7. Se liberar vaga, o sistema promove participante da lista de espera. |
| **Fluxo alternativo** | Caso o evento não permita cancelamento, o sistema informa o motivo ao participante. |
| **Pós-condição** | A inscrição é cancelada e vaga é liberada (quando aplicável). |

---

## CU05 - Processar Reembolso

| Campo | Descrição |
|-------|-----------|
| **Nome** | Processar Reembolso |
| **Objetivo** | Permitir que a equipe financeira processe reembolsos conforme política do evento. |
| **Ator principal** | Equipe Financeira |
| **Pré-condição** | Deve existir inscrição cancelada elegível para reembolso. |
| **Fluxo principal** | 1. A equipe financeira acessa a lista de solicitações de reembolso. 2. O sistema exibe inscrições canceladas elegíveis. 3. A equipe financeira avalia e processa o reembolso. 4. O sistema registra o resultado do reembolso. 5. O sistema notifica o participante. |
| **Fluxo alternativo** | Caso a inscrição não seja elegível, o sistema informa o motivo. |
| **Pós-condição** | O reembolso é registrado e o participante notificado. |

---

## CU06 - Emitir Certificado

| Campo | Descrição |
|-------|-----------|
| **Nome** | Emitir Certificado |
| **Objetivo** | Permitir que o participante emita certificado após o evento, conforme elegibilidade. |
| **Ator principal** | Participante |
| **Pré-condição** | O evento deve estar encerrado e o participante deve ser elegível. |
| **Fluxo principal** | 1. O participante acessa a seção de certificados. 2. O sistema verifica critério de elegibilidade. 3. O sistema gera o certificado. 4. O sistema disponibiliza o certificado para consulta/download. 5. O sistema envia notificação de certificado disponível. |
| **Fluxo alternativo** | Caso o participante não seja elegível, o sistema informa o motivo. |
| **Pós-condição** | O certificado é gerado e disponível ao participante. |

---

## CU07 - Gerenciar Eventos (Organizador)

| Campo | Descrição |
|-------|-----------|
| **Nome** | Gerenciar Eventos |
| **Objetivo** | Permitir que organizadores criem, editem e publiquem eventos. |
| **Ator principal** | Organizador |
| **Pré-condição** | O organizador deve estar autenticado com perfil autorizado. |
| **Fluxo principal** | 1. O organizador acessa o painel de gestão. 2. O organizador cria um novo evento informando dados (nome, data, local, vagas, políticas). 3. O sistema valida e registra o evento. 4. O organizador publica o evento. 5. O sistema disponibiliza o evento para inscrições. |
| **Fluxo alternativo** | O organizador pode editar evento já publicado, atualizando informações e políticas. |
| **Pós-condição** | O evento é criado e disponível para inscrições. |

---

## CU08 - Confirmar Pagamento

| Campo | Descrição |
|-------|-----------|
| **Nome** | Confirmar Pagamento |
| **Objetivo** | Permitir que a equipe financeira confirme pagamentos de inscrições. |
| **Ator principal** | Equipe Financeira |
| **Pré-condição** | Deve existir inscrição com pagamento pendente de confirmação. |
| **Fluxo principal** | 1. A equipe financeira acessa a lista de pagamentos pendentes. 2. O sistema exibe inscrições com pagamento a confirmar. 3. A equipe financeira confirma o pagamento. 4. O sistema altera o status da inscrição para "Confirmada". 5. O sistema envia comprovante ao participante. |
| **Fluxo alternativo** | Caso o pagamento não seja válido, a equipe financeira recusa e o sistema notifica o participante. |
| **Pós-condição** | O pagamento é confirmado e a inscrição liberada. |

---

## CU09 - Consultar Participantes (Palestrante)

| Campo | Descrição |
|-------|-----------|
| **Nome** | Consultar Participantes |
| **Objetivo** | Permitir que o palestrante consulte a lista de participantes de suas atividades. |
| **Ator principal** | Palestrante |
| **Pré-condição** | O palestrante deve estar autenticado e vinculado a atividades do evento. |
| **Fluxo principal** | 1. O palestrante acessa a área de suas atividades. 2. O sistema exibe a lista de atividades vinculadas. 3. O palestrante seleciona uma atividade. 4. O sistema exibe os participantes inscritos (apenas campos autorizados). |
| **Fluxo alternativo** | Caso não haja participantes inscritos, o sistema informa que a lista está vazia. |
| **Pós-condição** | A lista de participantes é apresentada ao palestrante. |
