# Requisitos Funcionais - Sistema de Gestão de Eventos (Eventus)

## Contexto

A empresa Eventus organiza congressos, workshops e eventos corporativos. O sistema deve centralizar inscrições, pagamentos, cancelamentos e emissão de certificados.

## Requisitos Funcionais

### RF-01 - Cadastro e autenticação de usuários
O sistema deve permitir o cadastro e autenticação de usuários com perfis distintos: participante, organizador, equipe financeira e palestrante.

### RF-02 - Visualização de eventos disponíveis
O sistema deve exibir, em um único local, a lista de eventos disponíveis para inscrição, com informações essenciais (nome, data, horário, local/modalidade, vagas e status).

### RF-03 - Consulta de programação de eventos e atividades
O sistema deve permitir a consulta da programação de cada evento, incluindo palestras e workshops, com seus respectivos horários.

### RF-04 - Criação e manutenção de eventos
O sistema deve permitir que organizadores criem, editem, publiquem e encerrem eventos.

### RF-05 - Configuração de vagas por evento/atividade
O sistema deve permitir que organizadores definam e alterem a quantidade de vagas por evento e por atividade associada.

### RF-06 - Inscrição em eventos e atividades
O sistema deve permitir que participantes realizem inscrições em eventos e atividades disponíveis.

### RF-07 - Controle automático de vagas
O sistema deve controlar automaticamente a ocupação de vagas durante o processo de inscrição.

### RF-08 - Tratamento de lotação com lista de espera
Quando uma atividade ou evento atingir lotação, o sistema deve permitir entrada em lista de espera.

### RF-09 - Classificação de evento gratuito ou pago
O sistema deve permitir que organizadores configurem eventos/atividades como gratuitos ou pagos.

### RF-10 - Registro e confirmação de pagamento
Para inscrições pagas, o sistema deve registrar o pagamento e permitir confirmação pela equipe financeira.

### RF-11 - Liberação condicional da inscrição
O sistema deve suportar inscrição condicionada à confirmação de pagamento, conforme regra definida pelo evento.

### RF-12 - Emissão de comprovante de inscrição
O sistema deve emitir comprovante de inscrição após a conclusão da inscrição.

### RF-13 - Consulta do status da inscrição
O sistema deve permitir que participantes acompanhem o status de suas inscrições (pendente, confirmada, cancelada, lista de espera).

### RF-14 - Cancelamento de inscrição pelo participante
O sistema deve permitir que o participante cancele sua inscrição sem contato manual com a organização, respeitando as políticas do evento.

### RF-15 - Aplicação de regras de cancelamento por evento
O sistema deve permitir que organizadores definam se o evento aceita ou não cancelamento.

### RF-16 - Solicitação e processamento de reembolso
O sistema deve permitir o registro de solicitações de reembolso e o processamento pela equipe financeira, conforme política do evento.

### RF-17 - Monitoramento em tempo real de inscritos
O sistema deve disponibilizar aos organizadores painel com quantidade de inscritos e vagas em tempo real.

### RF-18 - Consulta de participantes por palestrante
O sistema deve permitir ao palestrante consultar a lista de participantes inscritos em suas atividades.

### RF-19 - Emissão de certificados
O sistema deve permitir a emissão de certificados aos participantes após o evento, conforme critério de elegibilidade definido.

### RF-20 - Envio de notificações
O sistema deve enviar notificações aos participantes sobre eventos relevantes do ciclo de inscrição (confirmação, alteração de status, cancelamento e certificado disponível).

### RF-21 - Histórico de inscrições do participante
O sistema deve permitir a consulta do histórico de inscrições e respectivos resultados (participação, cancelamento, certificado).

### RF-22 - Gestão de participantes por organizadores
O sistema deve permitir aos organizadores consultar e gerenciar participantes inscritos por evento/atividade.

### RF-23 - Registro de operações administrativas
O sistema deve registrar operações relevantes de gestão (confirmações, cancelamentos, reembolsos e emissões) para rastreabilidade operacional.
