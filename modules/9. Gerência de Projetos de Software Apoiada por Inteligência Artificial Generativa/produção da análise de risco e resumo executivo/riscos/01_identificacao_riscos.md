# Riscos Identificados - Sistema de Gestão de Eventos (Eventus)

## Premissas

- As estimativas de probabilidade e impacto utilizam escala de 1 a 5, descrita abaixo.
- A identificação foi derivada dos artefatos do módulo 10: requisitos funcionais (RF-01 a RF-23), requisitos não funcionais (RNF-01 a RNF-18), regras de negócio (RN-01 a RN-20) e dúvidas e lacunas (AMB-01 a AMB-06, INC-01 a INC-05).
- Probabilidades e impactos são estimativas iniciais e devem ser validadas com os stakeholders antes da priorização final.

## Escala de avaliação

| Valor | Probabilidade | Impacto |
|-------|---------------|---------|
| 1 | Muito baixa | Desprezível |
| 2 | Baixa | Menor |
| 3 | Média | Moderado |
| 4 | Alta | Alto |
| 5 | Muito alta | Catastrófico |

## Registro de riscos

### R01 - Sobrecarga de acesso em período de pico de inscrições
- **Categoria:** Operacional / Desempenho
- **Causa:** abertura simultânea de inscrições de eventos populares concentra acessos, pressionando a infraestrutura (RNF-07, RNF-08, RNF-09).
- **Consequência:** lentidão ou indisponibilidade do sistema, inscrições perdidas e insatisfação de participantes.
- **Probabilidade:** 4
- **Impacto:** 4

### R02 - Falha na integração com o provedor de pagamento
- **Categoria:** Integração / Financeiro
- **Causa:** indisponibilidade ou erro do provedor externo de pagamento durante o processamento (RF-10, RN-11).
- **Consequência:** inscrições pagas sem confirmação, divergência financeira, reclamações e perda de receita.
- **Probabilidade:** 3
- **Impacto:** 4

### R03 - Inconsistência entre vaga, pagamento e confirmação (overbooking)
- **Categoria:** Técnico / Confiabilidade
- **Causa:** momento de reserva de vaga indefinido (INC-02) e dependência entre pagamento, ocupação de vaga e confirmação (RN-03, RNF-10).
- **Consequência:** participantes com inscrição confirmada sem vaga, divergência entre financeiro e operação e dano à confiança no sistema.
- **Probabilidade:** 3
- **Impacto:** 5

### R04 - Vazamento de dados pessoais e não conformidade com a LGPD
- **Categoria:** Compliance / Legal
- **Causa:** tratamento inadequado de dados pessoais de participantes, sem minimização de coleta e sem política de visibilidade definida (RNF-05, RN-15).
- **Consequência:** multas, sanções regulatórias, dano reputacional e perda de confiança.
- **Probabilidade:** 3
- **Impacto:** 5

### R05 - Ataque cibernético e acesso indevido a contas
- **Categoria:** Segurança
- **Causa:** falhas de autenticação, autorização ou proteção de dados em trânsito/armazenados (RNF-01, RNF-02, RNF-03, RNF-04).
- **Consequência:** vazamento de dados de participantes e informações de pagamento, interrupção de serviço e dano reputacional.
- **Probabilidade:** 2
- **Impacto:** 5

### R06 - Emissão indevida ou bloqueio de certificados
- **Categoria:** Legal / Reputacional
- **Causa:** critério de elegibilidade de certificado indefinido (AMB-01, INC-05, RN-14).
- **Consequência:** certificados emitidos a quem não cumpriu os critérios ou bloqueio de participantes legítimos, gerando retrabalho e questionamentos.
- **Probabilidade:** 3
- **Impacto:** 3

### R07 - Falha ou atraso no envio de notificações críticas
- **Categoria:** Operacional / Comunicação
- **Causa:** falha no serviço de notificações ou ausência de registro de envio (RNF-17, RN-19, RF-20).
- **Consequência:** participantes sem confirmação, alteração de status ou disponibilidade de certificado, gerando insatisfação e cancelamentos.
- **Probabilidade:** 3
- **Impacto:** 3

### R08 - Perda de dados por falha de backup e recuperação
- **Categoria:** Técnico
- **Causa:** ausência ou falha de mecanismos de backup e recuperação (RNF-11).
- **Consequência:** perda de inscrições, dados financeiros e registros de auditoria.
- **Probabilidade:** 2
- **Impacto:** 5

### R09 - Disputas de cancelamento e reembolso
- **Categoria:** Financeiro / Operacional
- **Causa:** políticas de cancelamento e reembolso por evento não definidas com clareza (RN-07, RN-08, RN-09, RN-10, INC-03).
- **Consequência:** disputas com participantes, sobrecarga da equipe financeira e impacto reputacional.
- **Probabilidade:** 3
- **Impacto:** 3

### R10 - Tratamento desigual na promoção da lista de espera
- **Categoria:** Operacional / Reputacional
- **Causa:** regras de ordenação e promoção da lista de espera indefinidas (RN-04, RN-05, RN-06, INC-04).
- **Consequência:** participantes tratados de forma desigual e reclamações sobre o processo de promoção.
- **Probabilidade:** 3
- **Impacto:** 3

### R11 - Políticas por evento não definidas antes da publicação das inscrições
- **Categoria:** Projeto
- **Causa:** decisões pendentes de stakeholders (checklist do módulo 10) e ausência de governança das políticas (RN-20).
- **Consequência:** retrabalho, atraso na entrega e comportamento inconsistente entre eventos.
- **Probabilidade:** 4
- **Impacto:** 3

### R12 - Indisponibilidade durante a operação do evento
- **Categoria:** Operacional
- **Causa:** dependência do sistema em credenciamento e consultas no dia do evento (RNF-09).
- **Consequência:** filas, impossibilidade de credenciar participantes e impacto direto na realização do evento.
- **Probabilidade:** 2
- **Impacto:** 4

### R13 - Conflito de horários entre atividades
- **Categoria:** Operacional
- **Causa:** política de sobreposição de horários indefinida (RN-13, AMB-06, INC-01).
- **Consequência:** participantes inscritos em atividades simultâneas, comprometendo a programação e a presença.
- **Probabilidade:** 3
- **Impacto:** 2

### R14 - Baixa usabilidade e acessibilidade
- **Categoria:** Produto / Usabilidade
- **Causa:** interface complexa ou não acessível para usuários não técnicos e pessoas com diferentes necessidades (RNF-12, RNF-13, RNF-14).
- **Consequência:** erros de uso, volume elevado de suporte e exclusão de usuários.
- **Probabilidade:** 2
- **Impacto:** 2

### R15 - Ambiguidades de data e hora entre regiões
- **Categoria:** Técnico / Usabilidade
- **Causa:** apresentação de datas e horários sem padrão regional consistente (RNF-18).
- **Consequência:** participantes comparecem em horários errados e reclamações sobre a programação.
- **Probabilidade:** 2
- **Impacto:** 2

## Síntese

| ID | Risco | Probabilidade | Impacto |
|----|-------|:-------------:|:-------:|
| R01 | Sobrecarga de acesso em pico de inscrições | 4 | 4 |
| R02 | Falha na integração com o provedor de pagamento | 3 | 4 |
| R03 | Inconsistência entre vaga, pagamento e confirmação | 3 | 5 |
| R04 | Vazamento de dados pessoais e não conformidade com a LGPD | 3 | 5 |
| R05 | Ataque cibernético e acesso indevido | 2 | 5 |
| R06 | Emissão indevida ou bloqueio de certificados | 3 | 3 |
| R07 | Falha ou atraso no envio de notificações críticas | 3 | 3 |
| R08 | Perda de dados por falha de backup e recuperação | 2 | 5 |
| R09 | Disputas de cancelamento e reembolso | 3 | 3 |
| R10 | Tratamento desigual na promoção da lista de espera | 3 | 3 |
| R11 | Políticas por evento não definidas antes da publicação | 4 | 3 |
| R12 | Indisponibilidade durante a operação do evento | 2 | 4 |
| R13 | Conflito de horários entre atividades | 3 | 2 |
| R14 | Baixa usabilidade e acessibilidade | 2 | 2 |
| R15 | Ambiguidades de data e hora entre regiões | 2 | 2 |
