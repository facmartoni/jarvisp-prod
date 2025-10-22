import Orb from '@/components/Orb'
import { useScrollAnimation } from '@/hooks/useScrollAnimation'

function Hero() {
  const { ref: textRef, isVisible: textVisible } = useScrollAnimation<HTMLDivElement>()
  const { ref: buttonRef, isVisible: buttonVisible } = useScrollAnimation<HTMLButtonElement>()

  return (
    <section className="flex flex-col items-center justify-center min-h-screen pt-20 gap-8 px-8">
      <div 
        ref={textRef}
        className={`flex flex-col items-center gap-4 transition-all duration-[1.5s] ease-out ${
          textVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
        }`}
      >
        <h1 className="text-white text-6xl font-bold text-center">
          Atención al Cliente con <span className="text-blue-500"><br />Inteligencia Artificial</span> para tu ISP
        </h1>
        <h6 className="text-gray-400 text-lg text-center">
          Te ofrecemos <span className="text-white font-bold">Agentes</span> integrados a tu sistema de gestión, <br />capaces de contestar <strong className="text-white font-bold">llamadas y mensajes de WhatsApp.</strong>
        </h6>
      </div>

      <Orb state="listening" size={128} />

      <button 
        ref={buttonRef}
        type="button" 
        className={`bg-blue-500 text-white text-[0.95rem] font-semibold px-6 py-2.5 rounded-full hover:bg-blue-600 hover:-translate-y-0.5 hover:shadow-[0_4px_12px_rgba(59,130,246,0.4)] active:translate-y-0 transition-all duration-[1.5s] ease-out ${
          buttonVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-5'
        }`}
      >
        Probá uno de nuestros agentes
      </button>
    </section>
  )
}

export default Hero

