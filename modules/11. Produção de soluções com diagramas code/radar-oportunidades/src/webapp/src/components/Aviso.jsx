export const TEXTO_AVISO =
  'Ferramenta de triagem e apoio à análise. Não constitui recomendação de investimento.'

export default function Aviso({ texto }) {
  return <p className="aviso">{texto || TEXTO_AVISO}</p>
}
