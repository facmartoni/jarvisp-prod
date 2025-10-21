import Orb from '@/components/Orb'

function Hero() {
  return (
    <section className="flex flex-col items-center justify-center min-h-screen pt-20 gap-8">
      <div className="flex flex-col items-center gap-4">
        <h1 className="text-white text-6xl font-bold text-center px-8 animate-fade-in">
          Atención al Cliente con <span className="text-blue-500"><br />Inteligencia Artificial</span> para tu ISP
        </h1>
        <h2 className="text-gray-400 text-lg text-center px-8 animate-fade-in">
          Te ofrecemos <span className="text-white font-bold">Agentes</span> integrados a tu sistema de gestión, <br />capaces de contestar <strong className="text-white font-bold">llamadas y mensajes de WhatsApp.</strong>
        </h2>
      </div>

      <Orb state="listening" size={128} />

      <button className="bg-white text-black text-[0.95rem] font-semibold px-6 py-2.5 rounded-full hover:bg-gray-200 hover:-translate-y-0.5 hover:shadow-[0_4px_12px_rgba(255,255,255,0.2)] active:translate-y-0 transition-all duration-200">
        Probá uno de nuestros agentes
      </button>
    </section>
  )
}

export default Hero

