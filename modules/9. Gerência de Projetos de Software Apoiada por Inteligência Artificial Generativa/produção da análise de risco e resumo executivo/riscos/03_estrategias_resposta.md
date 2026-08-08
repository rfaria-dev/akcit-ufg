# Estratégias de Resposta - Sistema de Gestão de Eventos (Eventus)

## Objetivo

Definir a estratégia de resposta e as ações objetivas para cada risco identificado, considerando o nível de prioridade da matriz probabilidade x impacto (ver `02_analise_impacto_priorizacao.md`).

## Legenda de estratégias

| Estratégia | Significado |
|------------|-------------|
| **Evitar** | Eliminar a causa ou o risco, mudando o plano ou a abordagem |
| **Mitigar** | Reduzir a probabilidade e/ou o impacto do risco |
| **Transferir** | Compartilhar ou transferir a responsabilidade do risco a terceiros |
| **Aceitar** | Assumir o risco, com ou sem plano de contingência |

## Estratégias por risco

### R01 - Sobrecarga de acesso em pico de inscrições (Alta)
- **Estratégia:** Mitigar (com aceitação parcial de janelas residuais)
- **Ações:**
  - Dimensionar infraestrutura para o pico (auto-scaling) com base no histórico de inscrições (RNF-08).
  - Adotar cache e fila de processamento para inscrições em períodos de alto volume.
  - Preparar plano de contingência de degradação graciosa (RNF-09).
- **Responsáveis:** TI / Infraestrutura, Organizadores

### R02 - Falha na integração com o provedor de pagamento (Alta)
- **Estratégia:** Mitigar + Transferir
- **Ações:**
  - Monitorar a disponibilidade do provedor e implementar fila de retry com compensação (RNF-10).
  - Negociar SLA com o provedor de pagamento e documentar responsabilidades.
  - Implementar reconciliação diária entre inscrições e transações financeiras.
- **Responsáveis:** TI, Equipe financeira, Provedor de pagamento

### R03 - Inconsistência entre vaga, pagamento e confirmação (Alta)
- **Estratégia:** Evitar (eliminar a causa) + Mitigar
- **Ações:**
  - Definir e aprovar o momento de reserva de vaga (início do pagamento vs confirmação) antes do go-live (INC-02, RN-03).
  - Garantir consistência transacional entre pagamento, ocupação de vaga e confirmação (RNF-10).
  - Implementar bloqueio/controle de concorrência na ocupação de vagas.
- **Responsáveis:** TI, Equipe financeira, Organizadores

### R04 - Vazamento de dados pessoais e não conformidade com a LGPD (Alta)
- **Estratégia:** Evitar + Mitigar + Transferir
- **Ações:**
  - Aplicar minimização de coleta e uso de dados pessoais (RNF-05).
  - Definir política de visibilidade de dados por perfil (RN-15) e anonimizar dados de relatórios.
  - Adotar criptografia de dados em trânsito e armazenados (RNF-03, RNF-04).
  - Contratar serviços e fornecedores aderentes à LGPD, transferindo parte da responsabilidade via contratos.
- **Responsáveis:** Jurídico/Compliance, TI, Organizadores

### R05 - Ataque cibernético e acesso indevido (Média)
- **Estratégia:** Mitigar + Transferir
- **Ações:**
  - Exigir autenticação robusta (ex.: MFA) e aplicar autorização por perfil (RNF-01, RNF-02).
  - Realizar testes de segurança (pentest) e revisões de configuração.
  - Contratar seguro cibernético e serviços de resposta a incidentes.
- **Responsáveis:** TI / Segurança, Organizadores

### R06 - Emissão indevida ou bloqueio de certificados (Média)
- **Estratégia:** Mitigar
- **Ações:**
  - Definir critério objetivo de elegibilidade (ex.: presença confirmada) com stakeholders (AMB-01, INC-05, RN-14).
  - Implementar validação automática de elegibilidade e trilha de auditoria antes da emissão.
- **Responsáveis:** Organizadores, Palestrantes, TI

### R07 - Falha ou atraso no envio de notificações críticas (Média)
- **Estratégia:** Mitigar
- **Ações:**
  - Monitorar a fila de notificações e implementar retry com registro de envio e status (RNF-17, RN-19).
  - Definir canais e gatilhos de notificação por evento (RF-20).
- **Responsáveis:** TI, Organizadores

### R08 - Perda de dados por falha de backup e recuperação (Média)
- **Estratégia:** Mitigar + Transferir
- **Ações:**
  - Implementar backup automatizado, teste periódico de restauração e plano de recuperação de desastres (RNF-11).
  - Adquirir infraestrutura cloud com SLA de durabilidade e cópia em região distinta.
- **Responsáveis:** TI / Infraestrutura

### R09 - Disputas de cancelamento e reembolso (Média)
- **Estratégia:** Mitigar + Aceitar
- **Ações:**
  - Definir políticas de cancelamento e reembolso por evento, com condições e prazos objetivos (RN-07 a RN-10, INC-03).
  - Automatizar a classificação reembolsável/não reembolsável (RN-10) e o processamento de reembolsos.
  - Aceitar que reclamações pontuais possam ocorrer, com fluxo de atendimento definido.
- **Responsáveis:** Equipe financeira, Organizadores

### R10 - Tratamento desigual na promoção da lista de espera (Média)
- **Estratégia:** Mitigar
- **Ações:**
  - Adotar ordenação FIFO como padrão, com regras de prioridade configuráveis e auditáveis (RN-04, RN-05, RN-06, INC-04).
  - Registrar logs de promoção para garantir rastreabilidade.
- **Responsáveis:** Organizadores, TI

### R11 - Políticas por evento não definidas antes da publicação (Alta)
- **Estratégia:** Evitar + Mitigar
- **Ações:**
  - Bloquear a publicação de inscrições enquanto as políticas do evento não estiverem definidas (RN-20).
  - Estabelecer calendário de decisões com stakeholders, resolvendo os itens pendentes do checklist do módulo 10.
- **Responsáveis:** Organizadores, Equipe de projeto

### R12 - Indisponibilidade durante a operação do evento (Média)
- **Estratégia:** Mitigar + Aceitar
- **Ações:**
  - Preparar plano de contingência para o dia do evento (credenciamento alternativo, acesso offline).
  - Garantir disponibilidade compatível no período do evento e planejar manutenções fora desse intervalo (RNF-09).
- **Responsáveis:** TI / Infraestrutura, Organizadores

### R13 - Conflito de horários entre atividades (Média)
- **Estratégia:** Mitigar
- **Ações:**
  - Definir política de sobreposição de horários por evento (bloquear, alertar ou permitir) (RN-13, AMB-06, INC-01).
  - Implementar validação de conflito de agenda no momento da inscrição.
- **Responsáveis:** Organizadores, TI

### R14 - Baixa usabilidade e acessibilidade (Baixa)
- **Estratégia:** Mitigar
- **Ações:**
  - Conduzir testes de usabilidade com usuários não técnicos (RNF-12).
  - Aplicar critérios mínimos de acessibilidade digital (RNF-13) e compatibilidade mobile/desktop (RNF-14).
- **Responsáveis:** TI / UX, Organizadores

### R15 - Ambiguidades de data e hora entre regiões (Baixa)
- **Estratégia:** Mitigar
- **Ações:**
  - Adotar padrão regional de data e hora (RNF-18) e testar a internacionalização em diferentes fusos.
- **Responsáveis:** TI

## Matriz resumo de respostas

| ID | Prioridade | Estratégia principal | Ações principais |
|----|:----------:|----------------------|------------------|
| R01 | Alta | Mitigar | Auto-scaling, cache, plano de contingência |
| R02 | Alta | Mitigar + Transferir | Retry, SLA com provedor, reconciliação |
| R03 | Alta | Evitar + Mitigar | Definir reserva de vaga, consistência transacional |
| R04 | Alta | Evitar + Mitigar + Transferir | LGPD, minimização, criptografia, contratos |
| R05 | Média | Mitigar + Transferir | MFA, pentest, seguro cibernético |
| R06 | Média | Mitigar | Critério de elegibilidade, validação automática |
| R07 | Média | Mitigar | Monitoramento de notificações, retry |
| R08 | Média | Mitigar + Transferir | Backup, DR, infra cloud com SLA |
| R09 | Média | Mitigar + Aceitar | Política clara, automação de reembolso |
| R10 | Média | Mitigar | FIFO, regras auditáveis |
| R11 | Alta | Evitar + Mitigar | Bloqueio de publicação, calendário de decisões |
| R12 | Média | Mitigar + Aceitar | Contingência no dia do evento |
| R13 | Média | Mitigar | Política de sobreposição, validação de agenda |
| R14 | Baixa | Mitigar | Testes de usabilidade, acessibilidade |
| R15 | Baixa | Mitigar | Padrão regional de data/hora |
