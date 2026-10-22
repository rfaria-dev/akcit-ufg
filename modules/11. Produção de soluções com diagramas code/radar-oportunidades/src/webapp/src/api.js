/** Consulta GET /oportunidades (mesma origem em produção; proxy em dev). */
export async function buscarOportunidades(filtros = {}) {
  const params = new URLSearchParams()
  for (const [chave, valor] of Object.entries(filtros)) {
    if (valor !== '' && valor !== null && valor !== undefined) {
      params.set(chave, valor)
    }
  }
  const resposta = await fetch(`/oportunidades?${params}`)
  if (!resposta.ok) {
    const corpo = await resposta.json().catch(() => ({}))
    throw new Error(corpo.detail || `erro inesperado (${resposta.status})`)
  }
  return resposta.json()
}
