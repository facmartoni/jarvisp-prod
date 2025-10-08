import { useQuery, gql } from '@apollo/client'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const HELLO_QUERY = gql`
  query {
    hello
  }
`

function App() {
  const { loading, error, data } = useQuery(HELLO_QUERY)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Jarvis P - Full Stack App</h1>
      <div className="card">
        <p>Django + GraphQL + React + TypeScript</p>
        {loading && <p>Loading...</p>}
        {error && <p>Error: {error.message}</p>}
        {data && <p>GraphQL Response: {data.hello}</p>}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
