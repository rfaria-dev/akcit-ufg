import { render, screen } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import App from '../App'

const RESPOSTA = {
  data_referencia: '2026-10-21',
  status: 'atualizado',
  aviso: 'Ferramenta de triagem e apoio à análise. Não constitui recomendação de investimento.',
  itens: [
    {
      posicao: 1,
      ticker: 'PETR4',
      nome: 'Petrobras PN',
      setor: 'Petróleo',
      score: 0.839,
      indicadores: [{ indicador: 'pl', valor: 4.49 }],
      contribuicoes: [
        {
          indicador: 'pl',
          disponivel: true,
          valor: 4.49,
          normalizado: 1,
          peso: 0.5,
          contribuicao: 0.5,
        },
        {
          indicador: 'dy',
          disponivel: false,
          valor: null,
          normalizado: null,
          peso: 0,
          contribuicao: 0,
        },
      ],
    },
  ],
}

function mockarFetch(resposta) {
  vi.stubGlobal(
    'fetch',
    vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => resposta,
    })
  )
}

describe('App', () => {
  beforeEach(() => mockarFetch(RESPOSTA))
  afterEach(() => vi.unstubAllGlobals())

  it('exibe aviso, data de referência e ranking', async () => {
    render(<App />)

    expect(await screen.findByText(/não constitui recomendação de investimento/i)).toBeInTheDocument()
    expect(screen.getByText(/2026-10-21/)).toBeInTheDocument()
    expect(screen.getByText('PETR4')).toBeInTheDocument()
  })

  it('exibe badge quando os dados estão desatualizados', async () => {
    mockarFetch({ ...RESPOSTA, status: 'desatualizado' })
    render(<App />)

    expect(await screen.findByText('desatualizados')).toBeInTheDocument()
  })

  it('exibe erro quando não há ranking (404)', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn().mockResolvedValue({
        ok: false,
        status: 404,
        json: async () => ({ detail: 'nenhum ranking disponível; execute a coleta antes de consultar' }),
      })
    )
    render(<App />)

    expect(await screen.findByRole('alert')).toHaveTextContent(/execute a coleta/)
  })
})
