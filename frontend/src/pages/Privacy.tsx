import { Link } from 'react-router-dom'

export default function Privacy() {
  return (
    <div className="bg-black min-h-screen px-6 md:px-12 lg:px-16 py-20">
      <div className="max-w-4xl mx-auto">
        {/* Back button */}
        <Link 
          to="/" 
          className="inline-flex items-center gap-2 text-gray-400 hover:text-white transition-colors duration-200 mb-8"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
          </svg>
          Volver al inicio
        </Link>

        <h1 className="text-white text-4xl md:text-5xl font-bold mb-2 border-b border-blue-500 pb-4">
          Política de Privacidad
        </h1>
      
        <p className="text-gray-500 italic mb-12 mt-4">
          Última actualización: Noviembre 2025
        </p>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">1. Introducción</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Bienvenido a Macch ("nosotros", "nuestro" o "la Plataforma"). Macch es una solución de atención al cliente 
            basada en inteligencia artificial, operada por Macch. Esta Política de Privacidad describe cómo 
            recopilamos, usamos, almacenamos y protegemos la información personal cuando utilizas nuestros servicios 
            a través de WhatsApp y otras plataformas de mensajería.
          </p>
          <p className="text-gray-400 leading-relaxed">
            Al utilizar nuestros servicios, aceptas las prácticas descritas en esta Política de Privacidad. 
            Si no estás de acuerdo con estas prácticas, te pedimos que no utilices nuestros servicios.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-6">2. Información que Recopilamos</h2>
          
          <h3 className="text-white text-xl font-semibold mb-3">2.1 Información proporcionada directamente</h3>
          <p className="text-gray-400 leading-relaxed mb-3">Cuando interactúas con Macch, podemos recopilar:</p>
          <ul className="text-gray-400 leading-relaxed mb-6 space-y-2 list-disc list-inside">
            <li>Número de teléfono de WhatsApp</li>
            <li>Nombre de perfil de WhatsApp</li>
            <li>Contenido de los mensajes enviados a través de la plataforma</li>
            <li>Información relacionada con consultas de servicio (número de cliente, dirección de servicio, etc.)</li>
          </ul>

          <h3 className="text-white text-xl font-semibold mb-3">2.2 Información recopilada automáticamente</h3>
          <p className="text-gray-400 leading-relaxed mb-3">Durante el uso del servicio, recopilamos automáticamente:</p>
          <ul className="text-gray-400 leading-relaxed mb-6 space-y-2 list-disc list-inside">
            <li>Fecha y hora de las interacciones</li>
            <li>Metadatos de mensajes</li>
            <li>Información técnica de la sesión</li>
            <li>Registros de conversación para mejora del servicio</li>
          </ul>

          <h3 className="text-white text-xl font-semibold mb-3">2.3 Información de terceros</h3>
          <p className="text-gray-400 leading-relaxed">
            Podemos recibir información adicional de la empresa de la cual eres cliente para poder 
            atender tus consultas, como estado de cuenta, información técnica de tu servicio y datos relacionados.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">3. Uso de la Información</h2>
          <p className="text-gray-400 leading-relaxed mb-3">Utilizamos la información recopilada para:</p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Proporcionar y mantener nuestros servicios de atención al cliente</li>
            <li>Responder a tus consultas y solicitudes de soporte</li>
            <li>Mejorar y personalizar la experiencia del usuario</li>
            <li>Entrenar y mejorar nuestros modelos de inteligencia artificial</li>
            <li>Generar análisis y reportes agregados para nuestros clientes empresariales</li>
            <li>Cumplir con obligaciones legales y regulatorias</li>
            <li>Detectar y prevenir fraudes o abusos del servicio</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-6">4. Compartición de Información</h2>
          <p className="text-gray-400 leading-relaxed mb-6">Podemos compartir tu información con:</p>
          
          <h3 className="text-white text-xl font-semibold mb-3">4.1 Empresas proveedoras de servicios</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            Compartimos información relevante de tus consultas con la empresa de la cual eres cliente para que puedan 
            atender tus solicitudes de servicio.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">4.2 Proveedores de servicios</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            Trabajamos con terceros que nos ayudan a operar nuestra plataforma, incluyendo servicios de 
            hosting, procesamiento de lenguaje natural y análisis de datos. Estos proveedores están 
            obligados contractualmente a proteger tu información.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">4.3 Meta/WhatsApp</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            Nuestro servicio opera a través de la API de WhatsApp Business. El uso de WhatsApp está sujeto 
            a los <a href="https://www.whatsapp.com/legal/terms-of-service" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:text-blue-400 transition-colors">Términos de Servicio</a>{' '}
            y la <a href="https://www.whatsapp.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:text-blue-400 transition-colors">Política de Privacidad de WhatsApp</a>.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">4.4 Requerimientos legales</h3>
          <p className="text-gray-400 leading-relaxed">
            Podemos divulgar información cuando sea requerido por ley, orden judicial, o cuando sea necesario 
            para proteger nuestros derechos legales.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">5. Retención de Datos</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Conservamos tu información personal durante el tiempo necesario para cumplir con los fines 
            descritos en esta política, a menos que la ley requiera o permita un período de retención más largo.
          </p>
          <p className="text-gray-400 leading-relaxed">
            Los registros de conversación se conservan por un período de [12 meses] para fines de mejora 
            del servicio y resolución de disputas, después del cual son eliminados o anonimizados.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">6. Seguridad de los Datos</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Implementamos medidas de seguridad técnicas y organizativas apropiadas para proteger tu información 
            personal contra acceso no autorizado, alteración, divulgación o destrucción. Estas medidas incluyen:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Encriptación de datos en tránsito y en reposo</li>
            <li>Controles de acceso basados en roles</li>
            <li>Monitoreo continuo de seguridad</li>
            <li>Auditorías de seguridad periódicas</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">7. Tus Derechos</h2>
          <p className="text-gray-400 leading-relaxed mb-3">Dependiendo de tu ubicación, puedes tener derecho a:</p>
          <ul className="text-gray-400 leading-relaxed mb-4 space-y-2 list-disc list-inside">
            <li><span className="text-white font-semibold">Acceso:</span> Solicitar una copia de la información personal que tenemos sobre ti</li>
            <li><span className="text-white font-semibold">Rectificación:</span> Corregir información inexacta o incompleta</li>
            <li><span className="text-white font-semibold">Eliminación:</span> Solicitar la eliminación de tu información personal</li>
            <li><span className="text-white font-semibold">Portabilidad:</span> Recibir tus datos en un formato estructurado y legible</li>
            <li><span className="text-white font-semibold">Oposición:</span> Oponerte al procesamiento de tus datos personales</li>
            <li><span className="text-white font-semibold">Retiro del consentimiento:</span> Retirar tu consentimiento en cualquier momento</li>
          </ul>
          <p className="text-gray-400 leading-relaxed">
            Para ejercer estos derechos, contáctanos usando la información proporcionada al final de esta política.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">8. Transferencias Internacionales</h2>
          <p className="text-gray-400 leading-relaxed">
            Tu información puede ser transferida y procesada en servidores ubicados fuera de tu país de residencia. 
            Nos aseguramos de que dichas transferencias cumplan con las leyes aplicables de protección de datos 
            y que se implementen las salvaguardas apropiadas.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">9. Uso de Inteligencia Artificial</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Macch utiliza tecnologías de inteligencia artificial y procesamiento de lenguaje natural para:
          </p>
          <ul className="text-gray-400 leading-relaxed mb-4 space-y-2 list-disc list-inside">
            <li>Comprender y responder a tus consultas</li>
            <li>Clasificar y dirigir solicitudes al área correspondiente</li>
            <li>Mejorar la calidad de las respuestas automatizadas</li>
          </ul>
          <p className="text-gray-400 leading-relaxed">
            Los datos de conversación pueden ser utilizados para entrenar y mejorar nuestros modelos de IA, 
            siempre de manera que proteja tu privacidad y, cuando sea posible, utilizando datos anonimizados.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">10. Menores de Edad</h2>
          <p className="text-gray-400 leading-relaxed">
            Nuestros servicios no están dirigidos a menores de 18 años. No recopilamos intencionalmente 
            información personal de menores. Si descubrimos que hemos recopilado información de un menor, 
            tomaremos medidas para eliminarla.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">11. Cambios a esta Política</h2>
          <p className="text-gray-400 leading-relaxed">
            Podemos actualizar esta Política de Privacidad periódicamente. Te notificaremos sobre cambios 
            significativos publicando la nueva política en nuestro sitio web y actualizando la fecha de 
            "última actualización". Te recomendamos revisar esta política regularmente.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">12. Contacto</h2>
          <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6">
            <p className="text-gray-400 leading-relaxed mb-4">
              Si tienes preguntas sobre esta Política de Privacidad o sobre cómo manejamos tu información personal, puedes contactarnos:
            </p>
            <p className="text-gray-400 leading-relaxed">
              <span className="text-white font-semibold">Macch AI</span><br />
              Email: <a href="mailto:privacidad@macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">privacidad@macch.ai</a><br />
              Sitio web: <a href="https://macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">https://macch.ai</a>
            </p>
          </div>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">13. Autoridad de Control</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Si consideras que el tratamiento de tus datos personales infringe la normativa aplicable, 
            tienes derecho a presentar una reclamación ante la autoridad de protección de datos de tu país.
          </p>
          <p className="text-gray-400 leading-relaxed">
            En Argentina, puedes contactar a la Agencia de Acceso a la Información Pública (AAIP): 
            <a href="https://www.argentina.gob.ar/aaip" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:text-blue-400 transition-colors"> www.argentina.gob.ar/aaip</a>
          </p>
        </section>
      </div>
    </div>
  );
}

