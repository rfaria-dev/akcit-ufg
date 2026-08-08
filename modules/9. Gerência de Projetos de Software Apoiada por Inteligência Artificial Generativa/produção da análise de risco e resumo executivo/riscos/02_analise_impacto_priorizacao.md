# Análise de Impactos e Priorização - Sistema de Gestão de Eventos (Eventus)

## Objetivo

Posicionar os riscos identificados (ver `01_identificacao_riscos.md`) em uma matriz de probabilidade x impacto e atribuir nível de prioridade (alta, média, baixa), para orientar o direcionamento dos esforços de resposta.

## Critério de priorização

- **Score do risco** = Probabilidade × Impacto (escala 1–5).
- **Zonas de prioridade:**
  - **Alta:** score de 12 a 25 — requer resposta imediata e acompanhamento contínuo.
  - **Média:** score de 5 a 11 — requer resposta planejada e monitoramento.
  - **Baixa:** score de 1 a 4 — monitorar; resposta acionada por gatilho.

## Matriz probabilidade x impacto

| Probabilidade \\ Impacto | 1 | 2 | 3 | 4 | 5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **5 (Muito alta)** | Média | Média | Alta | Alta | Alta |
| **4 (Alta)** | Média | Média | Alta | **R01** | Alta |
| **3 (Média)** | Baixa | **R13** | **R06, R07, R09, R10** | **R02** | **R03, R04** |
| **2 (Baixa)** | Baixa | **R14, R15** | Baixa | **R12** | **R05, R08** |
| **1 (Muito baixa)** | Baixa | Baixa | Baixa | Média | Média |

*Células com a legenda de cor da zona (Alta/Média/Baixa).*

## Posicionamento dos riscos

| ID | Risco | Probabilidade | Impacto | Score | Prioridade |
|----|-------|:-------------:|:-------:|:-----:|:----------:|
| R01 | Sobrecarga de acesso em pico de inscrições | 4 | 4 | 16 | **Alta** |
| R03 | Inconsistência entre vaga, pagamento e confirmação | 3 | 5 | 15 | **Alta** |
| R04 | Vazamento de dados pessoais e não conformidade com a LGPD | 3 | 5 | 15 | **Alta** |
| R02 | Falha na integração com o provedor de pagamento | 3 | 4 | 12 | **Alta** |
| R11 | Políticas por evento não definidas antes da publicação | 4 | 3 | 12 | **Alta** |
| R05 | Ataque cibernético e acesso indevido | 2 | 5 | 10 | Média |
| R08 | Perda de dados por falha de backup e recuperação | 2 | 5 | 10 | Média |
| R06 | Emissão indevida ou bloqueio de certificados | 3 | 3 | 9 | Média |
| R07 | Falha ou atraso no envio de notificações críticas | 3 | 3 | 9 | Média |
| R09 | Disputas de cancelamento e reembolso | 3 | 3 | 9 | Média |
| R10 | Tratamento desigual na promoção da lista de espera | 3 | 3 | 9 | Média |
| R12 | Indisponibilidade durante a operação do evento | 2 | 4 | 8 | Média |
| R13 | Conflito de horários entre atividades | 3 | 2 | 6 | Média |
| R14 | Baixa usabilidade e acessibilidade | 2 | 2 | 4 | Baixa |
| R15 | Ambiguidades de data e hora entre regiões | 2 | 2 | 4 | Baixa |

## Ranking por prioridade

1. **Alta:** R01, R03, R04, R02, R11 — cinco riscos que exigem resposta imediata e acompanhamento contínuo.
2. **Média:** R05, R08, R06, R07, R09, R10, R12, R13 — oito riscos a responder de forma planejada e monitorar.
3. **Baixa:** R14, R15 — dois riscos a monitorar, com resposta acionada por gatilho.

## Observações

- R03 e R04 são os riscos de maior impacto (impacto 5): afetam diretamente a confiança no sistema e a sustentabilidade do negócio.
- Os valores são estimativas iniciais e devem ser validados com os stakeholders, conforme checklist do módulo 10.
