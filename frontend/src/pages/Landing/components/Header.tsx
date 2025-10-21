import Robot from '@/components/Robot'

function Header() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-black/80 backdrop-blur-lg border-b border-white/10">
      <div className="max-w-[1400px] mx-auto px-8 py-4 flex items-center justify-between">
        
        {/* Logo section with Robot */}
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 flex items-center justify-center scale-[0.2] origin-center mt-[-10px]">
            <Robot />
          </div>
          <span className="text-2xl font-bold text-white tracking-tight">JarvISP</span>
        </div>

        {/* Navigation menu */}
        <nav className="hidden md:flex items-center gap-8">
          <a href="#pricing" className="text-[0.95rem] font-medium text-gray-400 hover:text-white transition-colors duration-200 cursor-pointer">
            Pricing
          </a>
          <a href="#press-kit" className="text-[0.95rem] font-medium text-gray-400 hover:text-white transition-colors duration-200 cursor-pointer">
            Press Kit
          </a>
          <a href="#support" className="text-[0.95rem] font-medium text-gray-400 hover:text-white transition-colors duration-200 cursor-pointer">
            Support
          </a>
        </nav>

        {/* CTA Button */}
        <div className="flex items-center">
          <button className="bg-white text-black text-[0.95rem] font-semibold px-6 py-2.5 rounded-full hover:bg-gray-200 hover:-translate-y-0.5 hover:shadow-[0_4px_12px_rgba(255,255,255,0.2)] active:translate-y-0 transition-all duration-200">
            Agendá una Demo
          </button>
        </div>
      </div>
    </header>
  )
}

export default Header

