# Dúvidas e Lacunas Identificados

## Definições

- **Ambiguidade**: quando um requisito admite múltiplas interpretações, dificultando especificação, implementação e teste.
- **Inconsistência**: quando há conflito entre expectativas, regras ou comportamentos esperados para o sistema.

---

## Ambiguidades

### AMB-01 - Emissão de certificado "depois do evento"
**Interpretações possíveis:**
- Emissão automática ao término da data do evento;
- Emissão somente após confirmação de presença.

### AMB-02 - Comprovante "logo após a inscrição"
**Interpretações possíveis:**
- Comprovante de solicitação de inscrição;
- Comprovante de inscrição confirmada;
- Comprovante condicionado à confirmação de pagamento.

### AMB-03 - Acompanhamento de inscritos "em tempo real"
**Interpretações possíveis:**
- Atualização instantânea a cada operação;
- Atualização em intervalos periódicos (ex.: 1, 5 ou 10 minutos).

### AMB-04 - "Gerenciar participantes" pelos organizadores
**Interpretações possíveis:**
- Apenas consultar listagem;
- Executar ações administrativas (aprovar, mover lista de espera, cancelar, etc.).

### AMB-05 - Informações visíveis para palestrantes
**Interpretações possíveis:**
- Visualização mínima (nome e e-mail);
- Visualização ampliada (empresa, telefone, dados adicionais), sem política definida.

### AMB-06 - Inscrição em múltiplos workshops no mesmo dia
**Interpretações possíveis:**
- Permitido desde que não haja sobreposição de horário;
- Permitido mesmo com sobreposição;
- Bloqueado em qualquer conflito de agenda.

---

## Inconsistências

### INC-01 - Inscrição em workshops no mesmo dia vs conflito de horários indefinido
Participantes desejam múltiplas inscrições no mesmo dia, mas não há regra definida para sobreposição de horários. **Conflito:** sem política, o comportamento pode ser permissivo em uma área e bloqueante em outra.

### INC-02 - Controle automático de vagas vs momento de reserva indefinido
Organizadores precisam de controle automático de vagas, mas não está definido se a vaga é reservada no início do pagamento ou na confirmação. **Conflito:** contagem de vagas pode divergir entre financeiro e operação.

### INC-03 - Cancelamento autosserviço vs eventos sem cancelamento
Participantes esperam cancelar sem contato manual, mas organizadores afirmam que nem todos os eventos permitem cancelamento. **Conflito:** expectativa de autonomia do participante pode colidir com política por evento.

### INC-04 - Lista de espera prevista vs funcionamento não definido
Há demanda por lista de espera quando lotado, mas não há definição de ordenação, promoção e prazo de resposta. **Conflito:** risco de tratamento desigual entre participantes e inconsistência operacional.

### INC-05 - Emissão de certificado desejada vs critério de elegibilidade indefinido
Participantes querem emitir certificado após o evento, mas não foi definido se depende de presença confirmada. **Conflito:** possibilidade de emissão indevida ou bloqueio indevido de certificados.

---

## Impacto

- Risco de decisões divergentes entre negócio, desenvolvimento e testes.
- Possibilidade de retrabalho por mudanças tardias.
- Comportamentos contraditórios no sistema.
- Dificuldade de homologação.

## Ação recomendada

- Converter cada ambiguidade em regra de negócio explícita com critério verificável.
- Formalizar cada inconsistência em decisão de negócio aprovada por stakeholders responsáveis.
