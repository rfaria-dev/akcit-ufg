# ADR 0004 — Definição e pesos do score v1

- **Status:** Aprovada
- **Data:** 2026-10-22
- **Decisores:** autor do projeto (decisão aprovada no plano: pesos iguais)

## Contexto

`docs/descricao.md` lista "definição e pesos do score" e "comparação por setor" como lacunas. O `AGENTS.md` exige score explicável (expor os indicadores que contribuíram) e isola a lógica de ranking no Motor.

## Decisão

- **Indicadores v1**: os 7 exemplos da descrição — P/L, P/VP, Dividend Yield, ROE, Dívida líquida/EBITDA, margem líquida e liquidez média diária — calculados a partir dos dados brutos (fórmulas em `motor/indicadores.py`).
- **Pesos iguais** entre os indicadores disponíveis do ativo: score = média dos valores normalizados; indicador ausente sai do denominador e aparece na explicação com `disponivel: false` (sem contribuir).
- **Normalização min-max [0, 1] sobre o universo do snapshot**, com inversão para "menor é melhor" (P/L, P/VP, DL/EBITDA). Sem variação no universo (`max == min`, ex.: um único ativo) → normalizado 1.0.
- **Sem ajuste por setor no v1** (lacuna registrada): a comparação é global; setor fica disponível como filtro na API.
- **Sem ajuste por proventos/desdobramentos** (lacuna registrada): preço usado como veio do provedor.

## Consequências

- Comparações entre setores podem ser enganosas (ex.: P/L de banco vs. varejo) — comportamento conhecido e documentado; o filtro por setor da API mitiga.
- Um ativo com poucos indicadores disponíveis tem score baseado nos restantes — o denominador ajustado evita punição, e a explicação mostra o que faltou.
- Mudar pesos futuramente é localizado em `motor/score.py`, sem tocar Coletor nem API.
