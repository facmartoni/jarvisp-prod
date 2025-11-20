import { Link } from 'react-router-dom'
import Robot from '@/components/Robot'

function Footer() {
  return (
    <footer className="bg-black/80 backdrop-blur-lg border-t border-white/10 mt-20">
      <div className="max-w-[1400px] mx-auto px-8 py-12">
        
        {/* Main footer content */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-8">
          
          {/* Logo and description */}
          <div className="flex flex-col gap-4">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 flex items-center justify-center scale-[0.2] origin-center mt-[-10px]">
                <Robot />
              </div>
              <span className="text-2xl font-bold text-white tracking-tight">Macch</span>
            </div>
            <p className="text-gray-400 text-sm leading-relaxed">
              Atención al cliente con inteligencia artificial para proveedores de internet.
            </p>
          </div>

          {/* Links */}
          <div>
            <h3 className="text-white font-semibold mb-4">Empresa</h3>
            <nav className="flex flex-col gap-3">
              <a href="#pricing" className="text-sm text-gray-400 hover:text-white transition-colors duration-200 cursor-pointer">
                Probar
              </a>
              <a href="#press-kit" className="text-sm text-gray-400 hover:text-white transition-colors duration-200 cursor-pointer">
                Contactanos
              </a>
              <a href="#support" className="text-sm text-gray-400 hover:text-white transition-colors duration-200 cursor-pointer">
                Precios
              </a>
            </nav>
          </div>

          {/* Legal */}
          <div>
            <h3 className="text-white font-semibold mb-4">Legal</h3>
            <nav className="flex flex-col gap-3">
              <Link to="/privacidad" target="_blank" rel="noopener noreferrer" className="text-sm text-gray-400 hover:text-white transition-colors duration-200">
                Política de Privacidad
              </Link>
              <Link to="/terminos" target="_blank" rel="noopener noreferrer" className="text-sm text-gray-400 hover:text-white transition-colors duration-200">
                Términos de Servicio
              </Link>
              <Link to="/eliminacion-datos" target="_blank" rel="noopener noreferrer" className="text-sm text-gray-400 hover:text-white transition-colors duration-200">
                Eliminación de Datos
              </Link>
            </nav>
          </div>
        </div>

        {/* Bottom bar */}
        <div className="pt-8 border-t border-white/10 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-gray-500 text-sm">
            © {new Date().getFullYear()} Macch AI. Todos los derechos reservados.
          </p>
          <div className="flex items-center gap-6">
            <a 
              href="mailto:privacidad@macch.ai" 
              className="text-sm text-gray-400 hover:text-white transition-colors duration-200"
            >
              privacidad@macch.ai
            </a>
            <a 
              href="https://macch.ai" 
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-gray-400 hover:text-white transition-colors duration-200"
            >
              macch.ai
            </a>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer

