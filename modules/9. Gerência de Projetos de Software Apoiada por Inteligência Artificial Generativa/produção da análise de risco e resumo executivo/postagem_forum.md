# Postagem do Fórum - Atividade: Produção da Análise de Risco e Resumo Executivo

> Texto pronto para publicação no fórum da disciplina "Gerência de Projetos de Software Apoiada por Inteligência Artificial Generativa".

---

Olá, colegas!

Compartilho o resultado da atividade prática de **gestão de riscos e comunicação** com apoio de Inteligência Artificial Generativa.

**1. Link do repositório GitHub**

https://github.com/rfaria-dev/akcit-ufg

**2. Cenário utilizado**

Utilizei o **estudo de caso do curso**: o Sistema de Gestão de Eventos da empresa **Eventus**, o mesmo cenário do projeto da unidade anterior (análise e especificação de requisitos). Isso me permitiu derivar os riscos diretamente dos requisitos funcionais, não funcionais e regras de negócio já levantados, mantendo consistência entre as unidades.

**3. Breve resumo dos principais riscos identificados**

Identifiquei **15 riscos**, priorizados em uma matriz de probabilidade x impacto. Os de prioridade **alta** foram:

- **Sobrecarga de acesso em período de pico de inscrições** — abertura simultânea de inscrições pressiona a infraestrutura, com risco de lentidão e indisponibilidade.
- **Inconsistência entre vaga, pagamento e confirmação** — sem uma regra clara do momento de reserva da vaga, há risco de *overbooking* e de divergência entre financeiro e operação.
- **Vazamento de dados pessoais e não conformidade com a LGPD** — tratamento inadequado de dados de participantes, com risco de sanções e dano reputacional.
- **Falha na integração com o provedor de pagamento** — indisponibilidade do provedor gera inscrições pagas sem confirmação e perda de receita.
- **Políticas por evento não definidas antes da publicação das inscrições** — decisões pendentes de stakeholders geram retrabalho e comportamento inconsistente entre eventos.

**4. Estratégia de resposta particularmente importante**

Destaco a estratégia **"Evitar" para o risco de inconsistência entre vaga, pagamento e confirmação**. Esse é o risco que ataca o núcleo de valor do sistema: garantir que uma inscrição confirmada corresponda a uma vaga real e a um pagamento válido. A ação-chave é **definir e aprovar, antes do go-live, o momento de reserva da vaga** (início do pagamento vs confirmação), eliminando a causa do risco, e garantir consistência transacional e controle de concorrência na ocupação de vagas. Considero essa estratégia a mais importante porque, sem ela, qualquer outro esforço de mitigação é ofuscado pela perda de confiança dos participantes e pela divergência entre áreas.

**5. Como a IA generativa apoiou a realização da atividade**

A IA generativa atuou como **apoio à tomada de decisão**, e não como substituição do julgamento humano:

- Propôs uma **lista inicial de riscos** derivada dos requisitos e regras de negócio do módulo 10, organizando categoria, causa e consequência.
- Auxiliou na estruturação da **matriz de probabilidade x impacto** e na distribuição das zonas de prioridade.
- Sugeriu **estratégias de resposta** (evitar, mitigar, transferir, aceitar) e o **plano de comunicação** por stakeholder.
- Contribuiu para a redação do **resumo executivo** e da postagem, sempre a partir dos dados levantados manualmente.

**6. Limitações, dificuldades ou cuidados percebidos durante o uso da IA**

- **Risco de "alucinação"**: a IA tende a gerar riscos genéricos ou desconectados do cenário. Foi necessário cruzar cada item com os requisitos reais do módulo 10 e descartar ou reescrever o que não tinha base.
- **Estimativas subjetivas**: a IA não possui contexto real de probabilidade/impacto — os valores precisaram de calibragem manual sob a ótica do negócio.
- **Verificação necessária**: as sugestões da IA foram tratadas como rascunho; a revisão humana foi essencial para garantir rastreabilidade e coerência com os artefatos da unidade anterior.
- **Cuidado com o excesso de confiança**: é preciso sempre validar as entregas da IA com os requisitos e com os stakeholders antes de incorporá-las aos artefatos.

Em resumo, a IA generativa acelerou a **estruturação e a abrangência** da análise, mas a **curadoria, a validação e o julgamento** permaneceram humanos.

Fico à disposição para trocas!
