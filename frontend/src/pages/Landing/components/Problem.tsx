import { useScrollAnimation } from '@/hooks/useScrollAnimation'

function Problem() {
  const { ref: firstRef, isVisible: firstVisible } = useScrollAnimation<HTMLDivElement>()
  const { ref: secondRef, isVisible: secondVisible } = useScrollAnimation<HTMLDivElement>()
  const { ref: imageRef, isVisible: imageVisible } = useScrollAnimation<HTMLDivElement>()

  return (
    <section className="flex flex-col items-center justify-center px-8 py-20 gap-20">
      {/* First subsection - centered */}
      <div 
        ref={firstRef}
        className={`flex flex-col items-center gap-6 max-w-3xl transition-all duration-[1.5s] ease-out ${
          firstVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
        }`}
      >
        <h2 className="text-white text-4xl font-bold text-center">
          No te quedés atrás.
        </h2>
        <p className="text-gray-400 text-xl text-center leading-relaxed">
          La era de la Inteligencia Artificial ya comenzó, y nosotros tenemos una hipótesis: <strong>la única manera de competir con las grandes telcos es brindando un servicio exclusivo y personalizado</strong> (¿no es acaso eso lo que siempre distinguió al PyME ISP?).
        </p>
      </div>

      {/* Second subsection - two columns */}
      <div className="max-w-7xl w-full grid grid-cols-1 lg:grid-cols-3 gap-12 items-center">
        <div 
          ref={secondRef}
          className={`lg:col-span-2 flex flex-col gap-6 transition-all duration-[1.5s] ease-out ${
            secondVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
          }`}
        >
          <h2 className="text-white text-4xl font-bold">
            Pero ojo: entendemos que no es escalable
          </h2>
          <p className="text-gray-400 text-xl leading-relaxed">
            Atender a los primeros clientes sin intermediarios puede ser fácil, pero una vez superado cierto número de conexiones, resulta inevitable delegar. ¿El problema? Cada empleado extra es una inversión de tiempo, capacitación y gestión enormes, y al chatbot genérico, doña Rosa no lo entiende y termina siendo un número más en nuestro CHURN.
          </p>
        </div>

        {/* Image */}
        <div 
          ref={imageRef}
          className={`lg:col-span-1 flex items-center justify-center transition-all duration-[1.5s] ease-out ${
            imageVisible ? 'opacity-100 translate-x-0' : 'opacity-0 translate-x-10'
          }`}
        >
          <img 
            src="/donarosablue.png" 
            alt="Doña Rosa"
            className="w-full h-auto rounded-lg"
          />
        </div>
      </div>
    </section>
  )
}

export default Problem

