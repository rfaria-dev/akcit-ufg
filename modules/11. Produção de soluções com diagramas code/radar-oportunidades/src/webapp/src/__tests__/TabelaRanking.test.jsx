import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { describe, expect, it } from 'vitest'

import TabelaRanking from '../components/TabelaRanking'

const ITEM = {
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
}

describe('TabelaRanking', () => {
  it('expande a linha e mostra contribuições e indisponíveis', async () => {
    const usuario = userEvent.setup()
    render(<TabelaRanking itens={[ITEM]} />)

    expect(screen.queryByText(/contribuições para o score/i)).not.toBeInTheDocument()

    await usuario.click(screen.getByText('PETR4'))

    expect(screen.getByText(/contribuições para o score/i)).toBeInTheDocument()
    expect(screen.getByText(/indisponível/)).toBeInTheDocument()
  })

  it('lista vazia mostra mensagem', () => {
    render(<TabelaRanking itens={[]} />)

    expect(screen.getByText(/nenhum ativo atende/i)).toBeInTheDocument()
  })
})
