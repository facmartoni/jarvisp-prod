import { Link } from 'react-router-dom'

export default function DataDeletion() {
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
          Instrucciones para Eliminación de Datos
        </h1>
      
        <p className="text-gray-500 italic mb-12 mt-4">
          Última actualización: Noviembre 2025
        </p>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">Tu Derecho a la Eliminación de Datos</h2>
          <p className="text-gray-400 leading-relaxed">
            En Macch respetamos tu privacidad y tu derecho a controlar tus datos personales. 
            Puedes solicitar la eliminación de todos los datos que hemos recopilado sobre ti 
            en cualquier momento.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">¿Qué datos eliminamos?</h2>
          <p className="text-gray-400 leading-relaxed mb-3">Al procesar tu solicitud de eliminación, borraremos:</p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Tu número de teléfono y datos de perfil de WhatsApp</li>
            <li>Historial completo de conversaciones</li>
            <li>Información de consultas y reclamos</li>
            <li>Cualquier dato personal asociado a tu cuenta</li>
            <li>Registros de interacción con el servicio</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">Cómo Solicitar la Eliminación</h2>
          
          <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-6 mb-6">
            <p className="text-white font-semibold mb-4">Opción 1: Por Email</p>
            <ol className="text-gray-400 leading-relaxed space-y-3 list-decimal list-inside">
              <li>Envía un correo electrónico a <a href="mailto:privacidad@macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">privacidad@macch.ai</a></li>
              <li>En el asunto escribe: "Solicitud de Eliminación de Datos"</li>
              <li>Incluye en el mensaje:
                <ul className="ml-6 mt-2 space-y-1 list-disc list-inside">
                  <li>Tu número de teléfono de WhatsApp (con código de país)</li>
                  <li>Nombre de la empresa con la que te comunicaste</li>
                  <li>Confirmación de que deseas eliminar todos tus datos</li>
                </ul>
              </li>
              <li>Recibirás una confirmación de recepción en 48 horas</li>
            </ol>
          </div>

          <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-6">
            <p className="text-white font-semibold mb-4">Opción 2: Por WhatsApp</p>
            <ol className="text-gray-400 leading-relaxed space-y-3 list-decimal list-inside">
              <li>Envía un mensaje al mismo número de WhatsApp donde usaste el servicio</li>
              <li>Escribe: "ELIMINAR MIS DATOS"</li>
              <li>Confirma tu solicitud cuando el sistema te lo pida</li>
            </ol>
          </div>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">Plazos de Procesamiento</h2>
          
          <div className="bg-yellow-500/10 border-l-4 border-yellow-500 p-6 rounded">
            <p className="text-yellow-200 font-semibold mb-3">Tiempos estimados:</p>
            <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
              <li><span className="text-white font-semibold">Confirmación de recepción:</span> 48 horas hábiles</li>
              <li><span className="text-white font-semibold">Procesamiento de eliminación:</span> hasta 30 días</li>
              <li><span className="text-white font-semibold">Confirmación de eliminación:</span> por email una vez completada</li>
            </ul>
          </div>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">Información Importante</h2>
          <p className="text-gray-400 leading-relaxed mb-3">Ten en cuenta que:</p>
          <ul className="text-gray-400 leading-relaxed space-y-3 list-disc list-inside">
            <li>
              <span className="text-white font-semibold">Datos retenidos por obligación legal:</span> Algunos datos pueden ser retenidos 
              por períodos adicionales si es requerido por ley o para proteger nuestros derechos legales.
            </li>
            <li>
              <span className="text-white font-semibold">Datos con tu proveedor:</span> La eliminación de datos en Macch no afecta los datos 
              que tu proveedor de servicios tenga sobre ti. Deberás contactarlos directamente para 
              gestionar esos datos.
            </li>
            <li>
              <span className="text-white font-semibold">Datos anonimizados:</span> Los datos que ya han sido anonimizados y utilizados 
              para análisis agregados no pueden ser eliminados ya que no están vinculados a tu identidad.
            </li>
            <li>
              <span className="text-white font-semibold">Copias de seguridad:</span> Los datos en copias de seguridad se eliminarán 
              en el siguiente ciclo de rotación (máximo 90 días).
            </li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">Verificación de Identidad</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Para proteger tu privacidad, podemos solicitar verificación de identidad antes de procesar 
            tu solicitud. Esto puede incluir:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Confirmación desde el número de WhatsApp registrado</li>
            <li>Respuesta a preguntas de seguridad basadas en tu historial de interacciones</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">Contacto</h2>
          <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6">
            <p className="text-gray-400 leading-relaxed mb-4">
              Para solicitudes de eliminación de datos o consultas relacionadas:
            </p>
            <p className="text-gray-400 leading-relaxed mb-4">
              <span className="text-white font-semibold">Macch</span><br />
              Email: <a href="mailto:privacidad@macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">privacidad@macch.ai</a><br />
              Sitio web: <a href="https://macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">https://macch.ai</a>
            </p>
            <p className="text-gray-400 leading-relaxed">
              Para más información sobre cómo manejamos tus datos, consulta nuestra{' '}
              <Link to="/privacidad" className="text-blue-500 hover:text-blue-400 transition-colors">Política de Privacidad</Link>.
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}


