import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [serverStatus, setServerStatus] = useState('checking')

  useEffect(() => {
    let componentIsMounted = true

    const checkServer = async () => {
      try {
        const response = await fetch('/api/health/', { cache: 'no-store' })
        const data = await response.json()

        if (!response.ok || data.status !== 'ok') {
          throw new Error('El backend no está disponible')
        }

        if (componentIsMounted) {
          setServerStatus('connected')
        }
      } catch {
        if (componentIsMounted) {
          setServerStatus('disconnected')
        }
      }
    }

    checkServer()
    const intervalId = window.setInterval(checkServer, 5000)

    return () => {
      componentIsMounted = false
      window.clearInterval(intervalId)
    }
  }, [])

  const statusText =
    serverStatus === 'connected'
      ? 'Servidor conectado'
      : serverStatus === 'disconnected'
        ? 'Servidor desconectado'
        : 'Comprobando servidor…'
  return (
    <div className='landing'>
      <header className='site-header'>
        <a className='brand' href="#inicio">
          <span className='brand-mark' aria-hidden="true">✿</span>
          <span>La Pitayera</span>
        </a>

        <span
          className={`status status--${serverStatus}`}
          role="status"
          aria-live="polite"
        >
          <span className="status-dot" aria-hidden="true" />
          {statusText}
        </span>
      </header>

      <main className='hero' id='inicio'>
        <section className='hero-copy'>
          <p className='eyebrow'>FRUTA FRESCA, MUY PRONTO</p>
          <h1>Una nueva forma de descubir <span>fruta.</span></h1>
          <p className='description'>
            Estamos preparando La Pitayera. Muy pronto podrás descubrir nuestra selección de pitahayas y otras frutas.
          </p>
          <p className='coming-soon'>
            <span aria-hidden="true">✦</span>
            Nuestra tienda abrirá pronto
          </p>
        </section>

        <div className='fruit-art' aria-hidden="true">
          <div className='fruit-orbit orbit-one' />
          <div className='fruit-orbit orbit-two' />
          <span className='dragon-fruit'>🐉</span>
          <span className='grapes'>🍇</span>
          <span className='fruit-label'>Color · Sabor · Frescura</span>
        </div>
      </main>

      <footer className='site-footer'>
        La Pitayera <span aria-hiden="true">·</span> En construcción
      </footer>
    </div>
  )
}

export default App