# ADR 0006 — Web App com React (substitui a decisão do ADR 0001)

- **Status:** Aprovada
- **Data:** 2026-10-22
- **Decisores:** autor do projeto (pedido explícito: "use react js ao invés de vanilla js")

## Contexto

O ADR 0001 decidiu Web App em HTML/JS/CSS vanilla, sem build. O autor do projeto pediu React no lugar. O diagrama estrutural continua válido: o Web App permanece uma SPA que consome a API via JSON/HTTPS.

## Decisão

- **React 18 + Vite** (JavaScript/JSX, sem TypeScript no v1) em `src/webapp/`.
- **Build do Vite (`dist/`) servido pelo FastAPI como estático na raiz**, apenas quando o build existe (`RADAR_WEBAPP_DIR`, padrão `src/webapp/dist`): mesma origem, sem CORS (coerente com o ADR 0005). O router da API mantém precedência (`/oportunidades`).
- **Desenvolvimento:** `vite dev` com proxy de `/oportunidades` para a API local.
- **Testes:** Vitest + Testing Library em `src/webapp/src/__tests__/` (colocados junto do código — a convenção `tests/<container>/` do AGENTS.md segue valendo para os containers Python); o mount de estáticos é coberto por `tests/webapp/test_estaticos.py`.

## Consequências

- Toolchain Node passa a ser necessária para o Web App (`npm install` + `npm run build`); os containers Python continuam independentes.
- `dist/` e `node_modules/` não são versionados; o build é etapa local antes de servir a UI.
- Sem divergência de diagrama: W continua "Web App SPA" com JSON/HTTPS para a API.
