# ADR 0001 — Stack de implementação

- **Status:** Aprovada
- **Data:** 2026-10-22
- **Decisores:** autor do projeto (aprovada após revisão do plano de implementação)

## Contexto

A documentação (`docs/descricao.md`) não define stack: tecnologia é lacuna. O `AGENTS.md` exige registro em ADR antes de adotar qualquer escolha, impõe provedor de dados mockado atrás de interface, proíbe filas, cache, autenticação, ordens e integração com corretoras, e manda implementar um container por vez (Armazenamento, Coletor, Motor, API, Web App) com testes ao lado.

## Decisão

- **Python 3.12** como linguagem única dos containers de backend (Armazenamento, Coletor, Motor, API): um só ecossistema, um só runner de testes.
- **FastAPI** para a API REST: OpenAPI/Swagger automáticos (pendência listada no README), validação de contrato com Pydantic e `TestClient` para testes sem infraestrutura.
- **SQLite via módulo `sqlite3` da stdlib, sem ORM**, acessado apenas pelo container Armazenamento (`src/storage/repository.py`): zero infraestrutura, SQL explícito e versionado em `schema.sql`.
- **pytest + httpx** como stack de testes; testes em `tests/<container>/`.
- **APScheduler no processo do Coletor**, com CLI `python -m coletor --once | --agendar`: agendamento versionado no código, sem fila (fora de escopo) e sem depender do SO.
- **Web App em HTML/JS/CSS vanilla, sem build**, servido como estático pelo FastAPI (detalhe confirmado na Etapa 5).

## Consequências

- Coletor e Motor rodam no **mesmo processo**: sem filas, o acionamento do cálculo é uma chamada in-process por uma porta definida pelo Coletor; os limites lógicos entre containers são preservados por módulos, não por processos.
- O banco é um arquivo SQLite local; não há serviço de banco a operar.
- Sem ferramenta de migração: evolução do schema é feita por `schema.sql` versionado (recriação em desenvolvimento).
- Dependências mínimas: fastapi, uvicorn, apscheduler (+ pytest, httpx em dev).

## Alternativas consideradas

- **SQLAlchemy 2.0**: modelos tipados e caminho de migração (Alembic); rejeitado — indireção sem retorno na escala do projeto.
- **Django/DRF**: ORM, admin e migrations inclusos; rejeitado — bateria inclusa demais para um endpoint de consulta.
- **Node/TypeScript (Express/Fastify)**: unificaria com o Web App; rejeitado — segundo runtime e toolchain no repositório.
- **Cron do SO**: rejeitado — agendamento vira estado de infraestrutura fora do código.
- **React + Vite no Web App**: rejeitado no v1 — o Web App apenas exibe; vanilla cobre sem toolchain Node.
