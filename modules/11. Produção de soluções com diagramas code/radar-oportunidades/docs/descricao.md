# Descrição do sistema — Radar de Oportunidades

## 1. Visão geral
Sistema que coleta dados de ativos da bolsa de valores, calcula indicadores fundamentalistas e de mercado e apresenta um **ranking de oportunidades** segundo critérios definidos pelo investidor. É uma ferramenta de triagem, **não** uma recomendação de investimento.

## 2. Escopo e nível da visão
- **Dentro do escopo:** ingestão periódica de dados, cálculo de indicadores, score e ranking explicável, consulta com filtros, indicação de dados desatualizados.
- **Fora do escopo:** execução de ordens, integração com corretoras, gestão de carteira, backtesting, derivativos, recomendações personalizadas, autenticação.
- **Nível da visão:** containers (C4 nível 2), sem detalhar classes, tabelas ou endpoints.
- **Mercado de referência (hipótese):** ações da B3.

## 3. Limites e responsabilidades
| Componente | Responsabilidade |
|---|---|
| Web App | Capturar critérios e exibir ranking, indicadores e avisos |
| API REST | Servir rankings e indicadores já calculados |
| Coletor de dados | Buscar dados no provedor de forma agendada e persistir |
| Motor de indicadores e ranking | Calcular indicadores e score; manter a lógica de ranking isolada |
| Armazenamento | Manter dados brutos, indicadores, rankings e data de referência |

## 4. Integrações
| Sistema externo | Direção | Finalidade |
|---|---|---|
| Provedor de dados de mercado | Saída (coletor consulta) | Cotações, fundamentos e proventos |

## 5. Indicadores de exemplo (a definir)
P/L, P/VP, Dividend Yield, ROE, Dívida líquida/EBITDA, margem líquida, liquidez média diária. A lista final e os pesos do score são lacunas.

## 6. Restrições
- Resultado é apoio à análise, com aviso explícito de que não é recomendação de investimento.
- Dados podem ter defasagem; a data de referência deve sempre ser exibida.
- O score deve ser explicável (mostrar quais indicadores contribuíram).
- Uso dos dados sujeito aos termos de licença do provedor.
- Cálculo separado da coleta; processamento assíncrono em relação ao usuário.

## 7. Lacunas e dúvidas em aberto
- Provedor de dados, licença e periodicidade de atualização.
- Definição e pesos do score; comparação por setor (P/L de banco não é comparável ao de varejo).
- Ajustes por proventos, desdobramentos e grupamentos.
- Política de retenção de histórico, modelo de dados, autenticação.
- Requisitos de desempenho, tratamento de retries e critérios de aceite.
