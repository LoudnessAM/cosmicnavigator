import { useState, useEffect } from 'react'

function App() {
  // Voruebergehend any, da die genaue Struktur der Daten von der Flask-API noch nicht definiert ist
  const [moon, setMoon] = useState<any>(null)

  // Fetch greeting from Flask backend on the first render 
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/lunar')
    .then(res => res.json())
    .then(data => setMoon(data))
  }, [])

  return (
    <div style={{ textAlign : 'center', marginTop: '100px' }}>
      <h1>Welcome to The Cosmic Navigator</h1>
      {moon ? (
        <div>
          <p>Phase: {moon.lunar_phase_name}</p>
          <p>Sign: {moon.lunar_sign}</p>
          <p>Illumination: {moon.lunar_illumination}%</p>
        </div>
      ) : (
      <p>Connecting to the cosmos...</p>
      )}
    </div>
  )
}

export default App