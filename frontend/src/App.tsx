import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Landing from '@/pages/Landing'
import Privacy from '@/pages/Privacy'
import Terms from '@/pages/Terms'
import DataDeletion from '@/pages/DataDeletion'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/privacidad" element={<Privacy />} />
        <Route path="/terminos" element={<Terms />} />
        <Route path="/eliminacion-datos" element={<DataDeletion />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
