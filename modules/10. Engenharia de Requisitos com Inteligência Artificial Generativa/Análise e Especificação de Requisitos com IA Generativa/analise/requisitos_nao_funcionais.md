# Requisitos Não Funcionais - Sistema de Gestão de Eventos (Eventus)

## RNF-01 - Segurança de autenticação
O sistema deve exigir autenticação para acesso às funcionalidades restritas, com credenciais individuais por usuário.

## RNF-02 - Controle de acesso por perfil
O sistema deve aplicar autorização baseada em perfis (participante, organizador, financeiro, palestrante), limitando cada usuário às funções permitidas.

## RNF-03 - Proteção de dados em trânsito
O sistema deve utilizar comunicação segura (HTTPS/TLS) para proteger dados transmitidos entre cliente e servidor.

## RNF-04 - Proteção de dados armazenados
O sistema deve adotar mecanismos de proteção para dados sensíveis armazenados (por exemplo, criptografia quando aplicável e controle de acesso ao banco de dados).

## RNF-05 - Privacidade e conformidade legal
O sistema deve atender à legislação de proteção de dados aplicável (LGPD), incluindo tratamento adequado de dados pessoais, finalidade de uso e minimização de coleta.

## RNF-06 - Rastreabilidade e auditoria
O sistema deve registrar logs de operações críticas (inscrição, confirmação de pagamento, cancelamento, reembolso, emissão de certificado), com identificação de usuário, data e ação.

## RNF-07 - Desempenho de resposta
O sistema deve responder às operações mais frequentes (listar eventos, consultar inscrições e efetuar inscrição) em tempo adequado ao uso operacional.

## RNF-08 - Escalabilidade operacional
O sistema deve suportar crescimento no número de eventos e participantes sem degradação significativa da experiência de uso.

## RNF-09 - Disponibilidade
O sistema deve manter disponibilidade compatível com uso contínuo durante períodos de inscrições e eventos, com planejamento de manutenção.

## RNF-10 - Confiabilidade transacional
O sistema deve garantir consistência de dados em operações críticas, especialmente no vínculo entre pagamento, confirmação de inscrição e ocupação de vaga.

## RNF-11 - Recuperação de falhas
O sistema deve possuir mecanismos de backup e recuperação para minimizar perda de dados em falhas operacionais.

## RNF-12 - Usabilidade
O sistema deve apresentar interface clara e de fácil navegação para usuários não técnicos.

## RNF-13 - Acessibilidade
O sistema deve atender a critérios básicos de acessibilidade digital, permitindo uso por pessoas com diferentes necessidades.

## RNF-14 - Compatibilidade de acesso
O sistema deve funcionar adequadamente em navegadores modernos e em diferentes tamanhos de tela (desktop e mobile).

## RNF-15 - Manutenibilidade
O sistema deve possuir estrutura que facilite correções e evolução, incluindo padronização de código e documentação técnica mínima.

## RNF-16 - Monitoramento operacional
O sistema deve disponibilizar mecanismos de monitoramento de erros e métricas de uso para suporte à operação e melhoria contínua.

## RNF-17 - Integridade de notificações
O sistema deve garantir registro de envio e status das notificações relevantes (confirmações, cancelamentos e disponibilização de certificados).

## RNF-18 - Internacionalização de data e hora
O sistema deve apresentar datas e horários de forma consistente com o padrão regional configurado para evitar ambiguidades de programação.
