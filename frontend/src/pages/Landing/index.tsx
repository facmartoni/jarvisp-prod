import Header from './components/Header'
import Hero from './components/Hero'
import Problem from './components/Problem'
import Solution from './components/Solution'
import Footer from './components/Footer'

function Landing() {
  return (
    <div className="bg-black min-h-screen px-6 md:px-12 lg:px-16">
      <Header />
      <Hero />
      <Problem />
      <Solution />
      <Footer />
    </div>
  )
}

export default Landing

