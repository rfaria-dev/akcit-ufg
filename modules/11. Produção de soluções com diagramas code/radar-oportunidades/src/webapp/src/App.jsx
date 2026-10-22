import { useCallback, useEffect, useState } from 'react'

import { buscarOportunidades } from './api'
import Aviso from './components/Aviso'
import Filtros from './components/Filtros'
import TabelaRanking from './components/TabelaRanking'

export default function App() {
  const [resultado, setResultado] = useState(null)
  const [erro, setErro] = useState(null)
  const [carregando, setCarregando] = useState(true)

  const consultar = useCallback(async (filtros = {}) => {
    setCarregando(true)
    setErro(null)
    try {
      setResultado(await buscarOportunidades(filtros))
    } catch (excecao) {
      setResultado(null)
      setErro(excecao.message)
    } finally {
      setCarregando(false)
    }
  }, [])

  useEffect(() => {
    consultar()
  }, [consultar])

  return (
    <main className="container">
      <h1>Radar de Oportunidades</h1>
      <Aviso texto={resultado?.aviso} />
      <Filtros aoAplicar={consultar} />
      {carregando && <p>Carregando…</p>}
      {erro && (
        <p className="erro" role="alert">
          {erro}
        </p>
      )}
      {resultado && (
        <>
          <p className="meta">
            Dados de {resultado.data_referencia}{' '}
            {resultado.status === 'desatualizado' && (
              <span className="badge">desatualizados</span>
            )}
          </p>
          <TabelaRanking itens={resultado.itens} />
        </>
      )}
    </main>
  )
}
