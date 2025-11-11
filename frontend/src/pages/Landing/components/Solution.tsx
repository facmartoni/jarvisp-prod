import FeatureCard from '@/components/ui/FeatureCard'
import { useScrollAnimation } from '@/hooks/useScrollAnimation'

function Solution() {
  const { ref: headlineRef, isVisible: headlineVisible } = useScrollAnimation<HTMLDivElement>()
  const { ref: card1Ref, isVisible: card1Visible } = useScrollAnimation<HTMLDivElement>()
  const { ref: card2Ref, isVisible: card2Visible } = useScrollAnimation<HTMLDivElement>()
  const { ref: card3Ref, isVisible: card3Visible } = useScrollAnimation<HTMLDivElement>()
  const { ref: card4Ref, isVisible: card4Visible } = useScrollAnimation<HTMLDivElement>()

  const features = [
    {
      image: '/paralellism.png',
      imageAlt: 'Agentes 24/7',
      title: 'Agentes IA en Paralelo 24/7',
      description: 'Olvidate del horario laboral. Agentes con voz hiperrealista contestarán tus mensajes y llamadas durante todo el día todos los días. Sí, los feriados también.',
      accentColor: 'rgba(59, 130, 246, 0.65)', // Blue - reliability, technology
    },
    {
      image: '/elasticity.png',
      imageAlt: 'Elasticidad en Picos',
      title: 'Elasticidad en Picos',
      description: '¿No alcanzan las manos para contestar en un corte general? Nuestros agentes se prenden y se apagan según la cantidad de mensajes y llamadas del momento, para que no pagués ni de más ni de menos por la atención al cliente.',
      accentColor: 'rgba(34, 197, 94, 0.65)', // Green - scalability, flexibility
    },
    {
      image: '/training.png',
      imageAlt: 'Entrenamiento Rápido',
      title: 'Entrenamiento en Horas',
      description: 'Nos das la información y los flujos de tu empresa una vez, y se terminó. No hay tiempo de adaptación. Retenemos el 100% de la información que resuelve los problemas de tus clientes.',
      accentColor: 'rgba(168, 85, 247, 0.65)', // Purple - innovation, speed
    },
    {
      image: '/sentiment_analysis.png',
      imageAlt: 'Análisis de Sentimiento',
      title: 'Análisis de Sentimiento',
      description: 'Interpretamos las emociones de tus clientes durante toda la llamada con el agente y las incorporamos en un resumen a tu sistema de gestión. Así sabés a quién hay que retener antes de perderlo.',
      accentColor: 'rgba(249, 115, 22, 0.65)', // Orange - emotion, empathy, warmth
    },
  ]

  return (
    <section className="flex flex-col items-center px-8 py-20 gap-12">
      {/* Headline */}
      <div 
        ref={headlineRef}
        className={`flex flex-col items-center gap-6 max-w-3xl transition-all duration-[1.5s] ease-out ${
          headlineVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
        }`}
      >
        <h2 className="text-white text-5xl font-bold text-center">
          Por eso creamos a Macch.
        </h2>
      </div>

      {/* Feature Cards Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-7xl w-full">
        <div
          ref={card1Ref}
          className={`transition-all duration-[1.5s] ease-out ${
            card1Visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
          }`}
        >
          <FeatureCard
            image={features[0].image}
            imageAlt={features[0].imageAlt}
            title={features[0].title}
            description={features[0].description}
            accentColor={features[0].accentColor}
          />
        </div>

        <div
          ref={card2Ref}
          className={`transition-all duration-[1.5s] ease-out ${
            card2Visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
          }`}
          style={{ transitionDelay: '150ms' }}
        >
          <FeatureCard
            image={features[1].image}
            imageAlt={features[1].imageAlt}
            title={features[1].title}
            description={features[1].description}
            accentColor={features[1].accentColor}
          />
        </div>

        <div
          ref={card3Ref}
          className={`transition-all duration-[1.5s] ease-out ${
            card3Visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
          }`}
          style={{ transitionDelay: '300ms' }}
        >
          <FeatureCard
            image={features[2].image}
            imageAlt={features[2].imageAlt}
            title={features[2].title}
            description={features[2].description}
            accentColor={features[2].accentColor}
          />
        </div>

        <div
          ref={card4Ref}
          className={`transition-all duration-[1.5s] ease-out ${
            card4Visible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
          }`}
          style={{ transitionDelay: '450ms' }}
        >
          <FeatureCard
            image={features[3].image}
            imageAlt={features[3].imageAlt}
            title={features[3].title}
            description={features[3].description}
            accentColor={features[3].accentColor}
          />
        </div>
      </div>
    </section>
  )
}

export default Solution

