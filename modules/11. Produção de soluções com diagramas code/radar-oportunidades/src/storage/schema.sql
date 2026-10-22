-- Modelo v1 do Armazenamento (ver docs/adr/0002-modelo-de-dados.md)

CREATE TABLE IF NOT EXISTS ativos (
    ticker TEXT PRIMARY KEY,
    nome   TEXT NOT NULL,
    setor  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dados_brutos (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker          TEXT NOT NULL REFERENCES ativos(ticker),
    tipo            TEXT NOT NULL CHECK (tipo IN ('cotacao', 'fundamento', 'provento')),
    data_referencia TEXT NOT NULL,  -- data do dado no provedor (YYYY-MM-DD)
    payload         TEXT NOT NULL,  -- JSON bruto do provedor
    coletado_em     TEXT NOT NULL,  -- instante da coleta (UTC ISO 8601)
    UNIQUE (ticker, tipo, data_referencia)
);

CREATE TABLE IF NOT EXISTS indicadores (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker          TEXT NOT NULL REFERENCES ativos(ticker),
    data_referencia TEXT NOT NULL,
    indicador       TEXT NOT NULL,
    valor           REAL NOT NULL,
    UNIQUE (ticker, indicador, data_referencia)
);

CREATE TABLE IF NOT EXISTS rankings (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    data_referencia TEXT NOT NULL,
    status          TEXT NOT NULL CHECK (status IN ('atualizado', 'desatualizado')),
    calculado_em    TEXT NOT NULL  -- instante do cálculo (UTC ISO 8601)
);

CREATE TABLE IF NOT EXISTS ranking_itens (
    ranking_id    INTEGER NOT NULL REFERENCES rankings(id),
    posicao       INTEGER NOT NULL,
    ticker        TEXT NOT NULL REFERENCES ativos(ticker),
    score         REAL NOT NULL,
    contribuicoes TEXT NOT NULL,  -- JSON: indicadores que contribuíram para o score
    UNIQUE (ranking_id, ticker)
);
