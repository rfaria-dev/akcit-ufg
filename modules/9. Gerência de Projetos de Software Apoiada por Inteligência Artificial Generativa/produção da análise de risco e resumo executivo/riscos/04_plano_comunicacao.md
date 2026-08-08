# Plano de Comunicação dos Riscos - Sistema de Gestão de Eventos (Eventus)

## Objetivo

Mapear os riscos aos stakeholders envolvidos e às ações de comunicação, garantindo que as informações cheguem às pessoas certas no momento adequado para decisão e resposta.

## Stakeholders

| Sigla | Stakeholder | Interesse principal |
|-------|-------------|---------------------|
| ORG | Organizadores | Operação dos eventos, políticas por evento |
| FIN | Equipe financeira | Pagamentos, reembolsos, receita |
| TI | Time de TI / Infraestrutura | Implementação, disponibilidade, segurança |
| PAR | Participantes | Experiência de inscrição, comunicação |
| PAL | Palestrantes | Inscrições em suas atividades, certificados |
| JUR | Jurídico / Compliance | LGPD, contratos, políticas |
| PRO | Provedores (pagamento, nuvem) | Serviços externos e SLAs |

## Comunicação por risco

### R01 - Sobrecarga de acesso em pico de inscrições (Alta)
- **Stakeholders:** TI, ORG
- **Ações de comunicação:** comunicar janelas de pico de inscrições; definir status de disponibilidade para a organização; alertar em caso de degradação.
- **Frequência:** antes e durante cada abertura de inscrições.

### R02 - Falha na integração com o provedor de pagamento (Alta)
- **Stakeholders:** TI, FIN, PRO
- **Ações de comunicação:** notificar incidentes de pagamento à equipe financeira; alinhar SLA e incidentes com o provedor; comunicar aos participantes apenas quando necessário (com orientações).
- **Frequência:** imediata em incidentes; revisão mensal de SLA.

### R03 - Inconsistência entre vaga, pagamento e confirmação (Alta)
- **Stakeholders:** TI, FIN, ORG
- **Ações de comunicação:** decidir o momento de reserva de vaga em conjunto; reportar divergências entre ocupação e confirmação; comunicar correções.
- **Frequência:** durante a decisão de regra e em auditorias de ocupação.

### R04 - Vazamento de dados pessoais e não conformidade com a LGPD (Alta)
- **Stakeholders:** JUR, TI, ORG
- **Ações de comunicação:** definir política de dados e visibilidade com o jurídico; reportar qualquer incidente de privacidade ao compliance imediatamente; informar participantes conforme exigido pela LGPD.
- **Frequência:** imediata em incidentes; revisão semestral da política.

### R05 - Ataque cibernético e acesso indevido (Média)
- **Stakeholders:** TI, JUR, ORG
- **Ações de comunicação:** comunicar incidentes de segurança ao comitê de resposta; acionar plano de resposta a incidentes; reportar às autoridades conforme aplicável.
- **Frequência:** imediata em incidentes; testes periódicos de segurança.

### R06 - Emissão indevida ou bloqueio de certificados (Média)
- **Stakeholders:** ORG, PAL, TI
- **Ações de comunicação:** alinhar critério de elegibilidade com organizadores e palestrantes; comunicar a regra aos participantes.
- **Frequência:** antes da emissão de certificados de cada evento.

### R07 - Falha ou atraso no envio de notificações críticas (Média)
- **Stakeholders:** TI, ORG
- **Ações de comunicação:** alertar sobre falhas na fila de notificações; manter os organizadores informados sobre entregas críticas (confirmação, status, certificado).
- **Frequência:** imediata em falhas; acompanhamento contínuo.

### R08 - Perda de dados por falha de backup e recuperação (Média)
- **Stakeholders:** TI, FIN, ORG
- **Ações de comunicação:** comunicar resultados dos testes de restauração; notificar em caso de indisponibilidade de backup.
- **Frequência:** após cada teste de restauração (periódico).

### R09 - Disputas de cancelamento e reembolso (Média)
- **Stakeholders:** FIN, ORG, PAR
- **Ações de comunicação:** publicar as políticas de cancelamento e reembolso no momento da inscrição; comunicar decisões de reembolso aos participantes; reportar volumes de disputas à organização.
- **Frequência:** contínua; revisão mensal de disputas.

### R10 - Tratamento desigual na promoção da lista de espera (Média)
- **Stakeholders:** ORG, TI, PAR
- **Ações de comunicação:** comunicar regras de lista de espera aos participantes; reportar promoções e critérios à organização para transparência.
- **Frequência:** durante cada evento com lista de espera.

### R11 - Políticas por evento não definidas antes da publicação (Alta)
- **Stakeholders:** ORG, FIN, JUR, TI
- **Ações de comunicação:** manter calendário de decisões com responsáveis e datas; comunicar pendências antes de cada publicação de inscrições.
- **Frequência:** semanal no início do projeto; antes de cada publicação.

### R12 - Indisponibilidade durante a operação do evento (Média)
- **Stakeholders:** TI, ORG
- **Ações de comunicação:** definir plano de contingência e canais de comunicação do dia do evento; comunicar indisponibilidade e ações corretivas.
- **Frequência:** antes e durante o evento.

### R13 - Conflito de horários entre atividades (Média)
- **Stakeholders:** ORG, TI, PAR
- **Ações de comunicação:** comunicar a política de sobreposição aos participantes; alertar sobre conflito de agenda no momento da inscrição.
- **Frequência:** no momento da inscrição.

### R14 - Baixa usabilidade e acessibilidade (Baixa)
- **Stakeholders:** TI, ORG
- **Ações de comunicação:** reportar resultados de testes de usabilidade; coletar feedback dos participantes.
- **Frequência:** em cada ciclo de melhoria.

### R15 - Ambiguidades de data e hora entre regiões (Baixa)
- **Stakeholders:** TI, ORG
- **Ações de comunicação:** comunicar o padrão de data e hora adotado; alinhar com organizadores a programação por fuso.
- **Frequência:** na configuração de cada evento.

## Matriz de comunicação resumo

| Risco | Prioridade | Stakeholders | Canais/Registro |
|-------|:----------:|--------------|-----------------|
| R01 | Alta | TI, ORG | Reuniões de operação, alertas de monitoramento |
| R02 | Alta | TI, FIN, PRO | Incidentes, SLA mensal, reconciliação |
| R03 | Alta | TI, FIN, ORG | Decisões de regra, auditorias |
| R04 | Alta | JUR, TI, ORG | Políticas, incidentes LGPD |
| R05 | Média | TI, JUR, ORG | Plano de resposta a incidentes |
| R06 | Média | ORG, PAL, TI | Critério de certificado |
| R07 | Média | TI, ORG | Monitoramento de notificações |
| R08 | Média | TI, FIN, ORG | Testes de restauração |
| R09 | Média | FIN, ORG, PAR | Políticas publicadas, disputas |
| R10 | Média | ORG, TI, PAR | Regras de lista de espera |
| R11 | Alta | ORG, FIN, JUR, TI | Calendário de decisões |
| R12 | Média | TI, ORG | Plano de contingência do evento |
| R13 | Média | ORG, TI, PAR | Alerta de conflito de agenda |
| R14 | Baixa | TI, ORG | Testes de usabilidade |
| R15 | Baixa | TI, ORG | Padrão regional configurado |

## Responsável geral

- **Gestor de riscos / líder do projeto:** consolida as comunicações, mantém o registro de riscos atualizado e convoca os responsáveis por cada resposta.
- **Cadência:** revisão semanal do registro durante o desenvolvimento e revisão por evento após o go-live.
