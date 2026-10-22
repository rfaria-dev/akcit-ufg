import { useState } from 'react'

function formatarNota(valor) {
  return (valor * 100).toFixed(1)
}

function LinhaAtivo({ item }) {
  const [aberta, setAberta] = useState(false)
  return (
    <>
      <tr className="linha-ativo" onClick={() => setAberta(!aberta)}>
        <td>{item.posicao}</td>
        <td>{item.ticker}</td>
        <td>{item.nome}</td>
        <td>{item.setor}</td>
        <td className="score">{formatarNota(item.score)}</td>
      </tr>
      {aberta && (
        <tr className="detalhe">
          <td colSpan="5">
            <h4>Contribuições para o score</h4>
            <ul>
              {item.contribuicoes.map((contrib) => (
                <li key={contrib.indicador}>
                  <strong>{contrib.indicador}</strong>
                  {contrib.disponivel ? (
                    <>
                      : valor {contrib.valor}, nota {formatarNota(contrib.normalizado)} (peso{' '}
                      {contrib.peso})
                    </>
                  ) : (
                    ': indisponível'
                  )}
                </li>
              ))}
            </ul>
          </td>
        </tr>
      )}
    </>
  )
}

export default function TabelaRanking({ itens }) {
  if (itens.length === 0) {
    return <p>Nenhum ativo atende aos critérios.</p>
  }
  return (
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Ticker</th>
          <th>Nome</th>
          <th>Setor</th>
          <th>Score (0–100)</th>
        </tr>
      </thead>
      <tbody>
        {itens.map((item) => (
          <LinhaAtivo key={item.ticker} item={item} />
        ))}
      </tbody>
    </table>
  )
}
