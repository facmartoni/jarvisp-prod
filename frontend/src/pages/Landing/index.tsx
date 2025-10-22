import Header from './components/Header'
import Hero from './components/Hero'
import Problem from './components/Problem'
import Solution from './components/Solution'

function Landing() {
  return (
    <div className="bg-black min-h-screen px-6 md:px-12 lg:px-16">
      <Header />
      <Hero />
      <Problem />
      <Solution />
    </div>
  )
}

export default Landing

