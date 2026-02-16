import { useState, useEffect } from 'react'

function App() {
  const [message, setMessage] = useState('')

  // Fetch greeting from Flask backend on the first render 
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/hellocosmos')
    .then(res => res.json())
    .then(data => setMessage(data.message))
  }, [])

  return (
    <div style={{ textAlign : 'center', marginTop: '100px' }}>
      <h1>Welcome to The Cosmic Navigator</h1>
      <p>{message || 'Connecting to the cosmos...'}</p>
    </div>
  )
}

export default App