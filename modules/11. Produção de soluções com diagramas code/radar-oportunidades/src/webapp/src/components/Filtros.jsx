import { useState } from 'react'

export const INDICADORES = [
  { nome: 'pl', rotulo: 'P/L' },
  { nome: 'pvp', rotulo: 'P/VP' },
  { nome: 'dy', rotulo: 'Dividend Yield' },
  { nome: 'roe', rotulo: 'ROE' },
  { nome: 'dl_ebitda', rotulo: 'Dívida líquida/EBITDA' },
  { nome: 'margem_liquida', rotulo: 'Margem líquida' },
  { nome: 'liquidez_media_diaria', rotulo: 'Liquidez média diária' },
]

export default function Filtros({ aoAplicar }) {
  const [setor, setSetor] = useState('')
  const [limite, setLimite] = useState(20)
  const [minimos, setMinimos] = useState({})
  const [maximos, setMaximos] = useState({})

  const aplicar = (evento) => {
    evento.preventDefault()
    const filtros = { setor, limite }
    for (const { nome } of INDICADORES) {
      if (minimos[nome] !== undefined && minimos[nome] !== '') {
        filtros[`min_${nome}`] = minimos[nome]
      }
      if (maximos[nome] !== undefined && maximos[nome] !== '') {
        filtros[`max_${nome}`] = maximos[nome]
      }
    }
    aoAplicar(filtros)
  }

  const limpar = () => {
    setSetor('')
    setLimite(20)
    setMinimos({})
    setMaximos({})
    aoAplicar({})
  }

  return (
    <form className="filtros" onSubmit={aplicar}>
      <label>
        Setor{' '}
        <input
          value={setor}
          onChange={(evento) => setSetor(evento.target.value)}
          placeholder="ex.: Bancos"
        />
      </label>
      <label>
        Limite{' '}
        <input
          type="number"
          min="1"
          max="100"
          value={limite}
          onChange={(evento) => setLimite(evento.target.value)}
        />
      </label>
      {INDICADORES.map(({ nome, rotulo }) => (
        <div key={nome} className="filtro-indicador">
          <span>{rotulo}</span>
          <input
            type="number"
            step="any"
            placeholder="mín"
            aria-label={`mínimo de ${rotulo}`}
            value={minimos[nome] ?? ''}
            onChange={(evento) => setMinimos({ ...minimos, [nome]: evento.target.value })}
          />
          <input
            type="number"
            step="any"
            placeholder="máx"
            aria-label={`máximo de ${rotulo}`}
            value={maximos[nome] ?? ''}
            onChange={(evento) => setMaximos({ ...maximos, [nome]: evento.target.value })}
          />
        </div>
      ))}
      <button type="submit">Aplicar</button>
      <button type="button" onClick={limpar}>
        Limpar
      </button>
    </form>
  )
}
