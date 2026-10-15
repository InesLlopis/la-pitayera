import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [health, setHealth] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    fetch('/api/health/')
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Respuesta HTTP ${response.status}`)
        }
        return response.json()
      })
      .then(setHealth)
      .catch((requestError) => {
        setError(requestError.message)
      })
  }, [])

  return (
    <main>
      <h1>La Pitayera</h1>
      <p>Comprobación de conexión con el backend</p>

      {error && <p role="alert">No se pudo conectar: {error}</p>}
      {!health && !error && <p>Consultando el estado…</p>}
      {health && <pre>{JSON.stringify(health, null, 2)}</pre>}
    </main>
  )
}

export default App