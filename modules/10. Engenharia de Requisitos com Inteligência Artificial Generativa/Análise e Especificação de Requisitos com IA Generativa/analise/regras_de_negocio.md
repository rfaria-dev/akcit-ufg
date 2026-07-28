# Regras de Negócio - Sistema de Gestão de Eventos (Eventus)

## RN-01 - Classificação de evento
Todo evento/atividade deve ser classificado como gratuito ou pago no momento de sua configuração.

## RN-02 - Capacidade máxima
Cada evento/atividade deve possuir limite de vagas definido pelo organizador.

## RN-03 - Ocupação de vaga
A vaga só pode ser considerada ocupada quando a inscrição atingir o estado de confirmação, conforme política de pagamento aplicável.

## RN-04 - Inscrição em evento lotado
Quando o limite de vagas for atingido, novas solicitações de inscrição devem ser direcionadas para lista de espera.

## RN-05 - Prioridade da lista de espera
A lista de espera deve respeitar ordem de entrada (FIFO), salvo configuração explícita de prioridade definida pelo organizador.

## RN-06 - Promoção da lista de espera
Quando houver liberação de vaga, o primeiro participante elegível da lista de espera deve ser promovido para inscrição pendente/confirmada conforme política do evento.

## RN-07 - Janela de cancelamento
O cancelamento de inscrição deve respeitar prazo limite configurado para o evento.

## RN-08 - Eventos sem cancelamento
Eventos configurados como não canceláveis não devem permitir cancelamento pelo participante após confirmação.

## RN-09 - Elegibilidade de reembolso
Reembolso só pode ser concedido quando a inscrição atender às condições definidas na política de reembolso do evento.

## RN-10 - Resultado do cancelamento em evento pago
Ao cancelar inscrição paga, o sistema deve classificar automaticamente o caso como reembolsável ou não reembolsável, conforme política vigente.

## RN-11 - Confirmação financeira
Inscrições condicionadas a pagamento só devem ser confirmadas após validação pela equipe financeira (ou integração de pagamento aprovada).

## RN-12 - Comprovante de inscrição
Todo participante com inscrição concluída deve receber comprovante contendo identificação do evento, participante e status da inscrição.

## RN-13 - Conflito de horários
A inscrição em atividades com sobreposição de horário deve seguir política definida pelo evento (bloquear, permitir com alerta, ou permitir livremente).

## RN-14 - Certificado por elegibilidade
Certificados só podem ser emitidos para inscrições elegíveis conforme critério definido para o evento (ex.: presença confirmada).

## RN-15 - Visibilidade para palestrantes
Palestrantes só podem visualizar dados de participantes vinculados às suas próprias atividades e apenas campos autorizados pela política de privacidade.

## RN-16 - Atualização de indicadores
Indicadores de inscritos e vagas disponíveis devem ser atualizados após cada operação que altere o estado da inscrição.

## RN-17 - Unicidade de inscrição
Um participante não pode possuir duas inscrições ativas para a mesma atividade/evento, exceto se houver regra explícita permitindo múltiplas inscrições.

## RN-18 - Histórico e rastreabilidade
Toda mudança relevante no ciclo da inscrição (criação, confirmação, cancelamento, reembolso, certificado) deve ser registrada para auditoria.

## RN-19 - Política de notificação
Eventos de negócio relevantes devem gerar notificação ao participante de acordo com canal e gatilhos configurados.

## RN-20 - Governança das políticas por evento
As políticas de cancelamento, reembolso, conflito de horário e certificado devem ser definidas por evento antes da publicação das inscrições.

---

## Decisões pendentes para validação com stakeholders

| # | Decisão | Responsável |
|---|---------|-------------|
| 1 | Definir prazo exato de cancelamento por tipo de evento | Organizadores |
| 2 | Definir critérios objetivos de reembolso (integral, parcial, não aplicável) | Financeiro |
| 3 | Definir se a promoção da lista de espera será automática ou manual | Organizadores |
| 4 | Definir momento de reserva de vaga em eventos pagos (início do pagamento vs confirmação) | Financeiro + TI |
| 5 | Definir política padrão para conflito de horários | Organizadores |
| 6 | Definir campos de dados visíveis aos palestrantes | Organizadores + Jurídico |
| 7 | Definir critério final de emissão de certificado (automático ou por presença) | Organizadores |
