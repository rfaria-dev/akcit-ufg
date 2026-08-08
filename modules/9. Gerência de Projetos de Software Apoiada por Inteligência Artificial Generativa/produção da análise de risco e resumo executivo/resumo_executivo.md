# Resumo Executivo - Gestão de Riscos do Sistema de Gestão de Eventos (Eventus)

**Empresa Eventus** | **Sistema de Gestão de Eventos** | **Atividade: produção da análise de risco e resumo executivo**

## Visão geral

A análise de riscos do Sistema de Gestão de Eventos (Eventus) identificou **15 riscos**, classificados em uma matriz de probabilidade x impacto e distribuídos em: **5 riscos de prioridade alta**, **8 de prioridade média** e **2 de prioridade baixa**. Os riscos foram derivados dos requisitos funcionais, não funcionais e regras de negócio levantados na unidade anterior (módulo 10), garantindo rastreabilidade entre elicitação e gestão.

## Principais riscos e impactos

| Prioridade | Riscos | Impacto principal |
|:----------:|--------|-------------------|
| **Alta** | R01 Sobrecarga de acesso em pico; R03 Inconsistência vaga/pagamento/confirmação; R04 Vazamento de dados (LGPD); R02 Falha na integração de pagamento; R11 Políticas por evento não definidas | Disponibilidade, confiança no sistema, receita, conformidade legal e prazo do projeto |
| **Média** | R05 Ataque cibernético; R08 Perda de dados; R06 Certificados; R07 Notificações; R09 Cancelamento/reembolso; R10 Lista de espera; R12 Indisponibilidade no evento; R13 Conflito de horários | Segurança, operação, atendimento e experiência do participante |
| **Baixa** | R14 Usabilidade/acessibilidade; R15 Data e hora entre regiões | Qualidade percebida e conveniência |

Os dois riscos de **maior impacto (impacto 5)** são o **R03** (inconsistência entre vaga, pagamento e confirmação) e o **R04** (vazamento de dados pessoais e não conformidade com a LGPD), por afetarem diretamente a sustentabilidade do negócio e a confiança dos participantes.

## Estratégia de resposta particularmente importante: R03 - Evitar a inconsistência entre vaga, pagamento e confirmação

**Por que é a mais importante:** o R03 ataca o núcleo de valor do sistema — a garantia de que uma inscrição confirmada corresponde a uma vaga real e a um pagamento válido. Um descasamento aqui gera *overbooking*, divergência entre financeiro e operação e participantes sem vaga no dia do evento, comprometendo a credibilidade da Eventus.

**Estratégia:** **Evitar** (eliminar a causa) combinada com **Mitigar**:
- definir e aprovar, antes do go-live, o momento de reserva da vaga (início do pagamento vs confirmação), resolvendo a inconsistência INC-02 levantada no módulo 10;
- garantir consistência transacional entre pagamento, ocupação de vaga e confirmação (RNF-10);
- implementar controle de concorrência na ocupação de vagas.

**Decisão recomendada:** adotar reserva provisória no início do pagamento, com expiração automática, e confirmação definitiva após a validação financeira, mantendo a contagem de vagas única e auditável.

## Próximos passos

1. Validar probabilidades, impactos e prioridades com os stakeholders (organizadores, financeiro e TI).
2. Resolver os itens pendentes do checklist do módulo 10 (prazo de cancelamento, política de reembolso, lista de espera, momento de reserva de vaga, certificados), destravando o R11.
3. Incluir os riscos de prioridade alta no cronograma do projeto, com dono e data de resposta.
4. Estabelecer a cadência de revisão do registro de riscos (semanal durante o desenvolvimento, por evento após o go-live).

## Apoio da IA generativa na elaboração

A IA generativa apoiou a atividade na **proposição inicial** dos riscos a partir dos requisitos do módulo 10, na estruturação de categorias, causas e consequências, na sugestão de estratégias de resposta (evitar, mitigar, transferir, aceitar) e na organização da matriz e do plano de comunicação. Todas as propostas foram **revisadas e ajustadas manualmente**, confrontadas com os requisitos e regras de negócio reais, e as estimativas foram validadas sob a ótica do negócio. As limitações, dificuldades e cuidados observados estão detalhados no `README.md` e na `postagem_forum.md`.
