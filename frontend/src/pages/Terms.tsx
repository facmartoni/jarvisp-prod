import { Link } from 'react-router-dom'

export default function Terms() {
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
          Términos de Servicio
        </h1>
      
        <p className="text-gray-500 italic mb-12 mt-4">
          Última actualización: Noviembre 2025
        </p>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">1. Aceptación de los Términos</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Estos Términos de Servicio ("Términos") constituyen un acuerdo legal vinculante entre tú ("Usuario", "tú") 
            y Macch ("Macch", "nosotros", "nuestro") que rige tu uso de la plataforma de atención al cliente 
            Macch y todos los servicios relacionados (colectivamente, el "Servicio").
          </p>
          <p className="text-gray-400 leading-relaxed">
            Al acceder o utilizar el Servicio a través de WhatsApp u otras plataformas de mensajería, 
            aceptas estar sujeto a estos Términos. Si no estás de acuerdo con alguna parte de estos Términos, 
            no debes utilizar el Servicio.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">2. Descripción del Servicio</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Macch es una plataforma de atención al cliente basada en inteligencia artificial que permite a los 
            usuarios finales de empresas realizar consultas, reportar problemas técnicos, gestionar sus cuentas 
            y recibir soporte a través de canales de mensajería como WhatsApp.
          </p>
          <p className="text-gray-400 leading-relaxed">
            El Servicio actúa como intermediario entre tú y la empresa de la cual eres cliente, 
            facilitando la comunicación y resolución de consultas mediante tecnología de procesamiento 
            de lenguaje natural e inteligencia artificial.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">3. Elegibilidad</h2>
          <p className="text-gray-400 leading-relaxed mb-3">Para utilizar el Servicio, debes:</p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Tener al menos 18 años de edad</li>
            <li>Ser cliente activo de una empresa que utilice los servicios de Macch</li>
            <li>Tener capacidad legal para celebrar contratos vinculantes</li>
            <li>Proporcionar información veraz y precisa</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">4. Cuenta y Acceso</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            El acceso al Servicio se realiza a través de tu número de WhatsApp. Eres responsable de:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Mantener la seguridad de tu dispositivo y cuenta de WhatsApp</li>
            <li>Todas las actividades que ocurran bajo tu número de teléfono</li>
            <li>Notificarnos inmediatamente sobre cualquier uso no autorizado</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">5. Uso Aceptable</h2>
          <p className="text-gray-400 leading-relaxed mb-3">Al utilizar el Servicio, aceptas NO:</p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Proporcionar información falsa o engañosa</li>
            <li>Hacerte pasar por otra persona o entidad</li>
            <li>Utilizar el Servicio para fines ilegales o no autorizados</li>
            <li>Intentar acceder a información de otros usuarios</li>
            <li>Enviar contenido ofensivo, amenazante, difamatorio o inapropiado</li>
            <li>Interferir con el funcionamiento del Servicio</li>
            <li>Utilizar sistemas automatizados para enviar mensajes masivos (spam)</li>
            <li>Intentar realizar ingeniería inversa o extraer el código fuente</li>
            <li>Evadir o manipular los sistemas de seguridad</li>
            <li>Utilizar el Servicio para acosar o dañar a terceros</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">6. Interacción con Inteligencia Artificial</h2>
          
          <div className="bg-yellow-500/10 border-l-4 border-yellow-500 p-4 mb-4 rounded">
            <p className="text-yellow-200">
              <span className="font-semibold">Importante:</span> Macch utiliza inteligencia artificial para procesar y responder a tus consultas. 
              Aunque nos esforzamos por proporcionar información precisa, las respuestas generadas por IA pueden 
              contener errores o inexactitudes.
            </p>
          </div>

          <p className="text-gray-400 leading-relaxed mb-3">Entiendes y aceptas que:</p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Las respuestas son generadas automáticamente y pueden requerir verificación</li>
            <li>Para asuntos críticos o complejos, puedes solicitar atención humana</li>
            <li>El Servicio puede transferir tu conversación a un agente humano cuando sea necesario</li>
            <li>Tus conversaciones pueden ser utilizadas para mejorar el sistema de IA</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">7. Relación con tu Proveedor de Servicios</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Macch actúa como facilitador de comunicación entre tú y la empresa de la cual eres cliente. 
            Es importante que entiendas que:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Tu relación contractual es directamente con la empresa proveedora del servicio</li>
            <li>Macch no es responsable de los servicios que recibes de dicha empresa</li>
            <li>Las políticas de facturación, precios y servicio son determinadas por tu proveedor</li>
            <li>Las decisiones finales sobre tu cuenta son tomadas por tu proveedor de servicios</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">8. Disponibilidad del Servicio</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Nos esforzamos por mantener el Servicio disponible 24/7, pero no garantizamos disponibilidad 
            ininterrumpida. El Servicio puede estar temporalmente no disponible debido a:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Mantenimiento programado o de emergencia</li>
            <li>Actualizaciones del sistema</li>
            <li>Problemas técnicos con WhatsApp o terceros proveedores</li>
            <li>Causas de fuerza mayor</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">9. Propiedad Intelectual</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Todo el contenido, características y funcionalidad del Servicio, incluyendo pero no limitado a 
            texto, gráficos, logos, algoritmos, software y código, son propiedad exclusiva de Macch 
            o sus licenciantes y están protegidos por leyes de propiedad intelectual.
          </p>
          <p className="text-gray-400 leading-relaxed">
            No adquieres ningún derecho de propiedad sobre el Servicio. Se te otorga únicamente una licencia 
            limitada, no exclusiva, no transferible y revocable para usar el Servicio de acuerdo con estos Términos.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">10. Contenido del Usuario</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Al enviar mensajes o contenido a través del Servicio, nos otorgas una licencia mundial, 
            no exclusiva, libre de regalías para usar, procesar, almacenar y analizar dicho contenido 
            con el fin de:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Proporcionar el Servicio</li>
            <li>Mejorar nuestros sistemas de IA</li>
            <li>Generar análisis agregados</li>
            <li>Cumplir con obligaciones legales</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">11. Privacidad</h2>
          <p className="text-gray-400 leading-relaxed">
            Tu privacidad es importante para nosotros. El uso de tu información personal está regido por 
            nuestra <Link to="/privacidad" className="text-blue-500 hover:text-blue-400 transition-colors">Política de Privacidad</Link>, que forma parte integral de estos Términos.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">12. Exclusión de Garantías</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            EL SERVICIO SE PROPORCIONA "TAL CUAL" Y "SEGÚN DISPONIBILIDAD", SIN GARANTÍAS DE NINGÚN TIPO, 
            YA SEAN EXPRESAS O IMPLÍCITAS.
          </p>
          <p className="text-gray-400 leading-relaxed mb-3">
            En la máxima medida permitida por la ley, Macch no garantiza que:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>El Servicio cumplirá con tus requisitos específicos</li>
            <li>El Servicio será ininterrumpido, oportuno, seguro o libre de errores</li>
            <li>Los resultados obtenidos del uso del Servicio serán precisos o confiables</li>
            <li>Cualquier error en el Servicio será corregido</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">13. Limitación de Responsabilidad</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            EN NINGÚN CASO MACCH, SUS DIRECTORES, EMPLEADOS, SOCIOS, AGENTES O AFILIADOS SERÁN 
            RESPONSABLES POR DAÑOS INDIRECTOS, INCIDENTALES, ESPECIALES, CONSECUENTES O PUNITIVOS, 
            INCLUYENDO PÉRDIDA DE BENEFICIOS, DATOS, USO U OTRAS PÉRDIDAS INTANGIBLES.
          </p>
          <p className="text-gray-400 leading-relaxed">
            La responsabilidad total de Macch por cualquier reclamación relacionada con el Servicio 
            no excederá el monto que hayas pagado a Macch en los últimos doce (12) meses, si corresponde.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">14. Indemnización</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Aceptas defender, indemnizar y mantener indemne a Macch y sus afiliados de cualquier reclamación, 
            daño, obligación, pérdida, responsabilidad, costo o deuda que surja de:
          </p>
          <ul className="text-gray-400 leading-relaxed space-y-2 list-disc list-inside">
            <li>Tu uso del Servicio</li>
            <li>Tu violación de estos Términos</li>
            <li>Tu violación de derechos de terceros</li>
            <li>Cualquier contenido que envíes a través del Servicio</li>
          </ul>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">15. Terminación</h2>
          <p className="text-gray-400 leading-relaxed mb-3">
            Podemos suspender o terminar tu acceso al Servicio inmediatamente, sin previo aviso, por 
            cualquier motivo, incluyendo pero no limitado a:
          </p>
          <ul className="text-gray-400 leading-relaxed mb-4 space-y-2 list-disc list-inside">
            <li>Violación de estos Términos</li>
            <li>Conducta que consideremos perjudicial para otros usuarios o para Macch</li>
            <li>Solicitud de tu proveedor de servicios</li>
            <li>Terminación de la relación con tu proveedor de servicios</li>
          </ul>
          <p className="text-gray-400 leading-relaxed">
            Puedes dejar de utilizar el Servicio en cualquier momento. Las disposiciones que por su 
            naturaleza deban sobrevivir a la terminación, sobrevivirán.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">16. Modificaciones al Servicio</h2>
          <p className="text-gray-400 leading-relaxed">
            Nos reservamos el derecho de modificar, suspender o discontinuar el Servicio (o cualquier 
            parte del mismo) en cualquier momento, con o sin previo aviso. No seremos responsables ante 
            ti ni ante terceros por cualquier modificación, suspensión o discontinuación del Servicio.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">17. Cambios a los Términos</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Nos reservamos el derecho de actualizar estos Términos en cualquier momento. Te notificaremos 
            sobre cambios materiales publicando los nuevos Términos en nuestro sitio web y actualizando 
            la fecha de "última actualización".
          </p>
          <p className="text-gray-400 leading-relaxed">
            El uso continuado del Servicio después de la publicación de cambios constituye tu aceptación 
            de dichos cambios.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">18. Ley Aplicable y Jurisdicción</h2>
          <p className="text-gray-400 leading-relaxed mb-4">
            Estos Términos se regirán e interpretarán de acuerdo con las leyes de la República Argentina, 
            sin consideración a sus disposiciones sobre conflictos de leyes.
          </p>
          <p className="text-gray-400 leading-relaxed">
            Cualquier disputa que surja en relación con estos Términos será sometida a la jurisdicción 
            exclusiva de los tribunales ordinarios de la Ciudad Autónoma de Buenos Aires, Argentina, 
            renunciando a cualquier otro fuero que pudiera corresponder.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">19. Resolución de Disputas</h2>
          <p className="text-gray-400 leading-relaxed">
            Antes de iniciar cualquier procedimiento legal, aceptas intentar resolver cualquier disputa 
            de manera informal contactándonos primero. Si no podemos resolver la disputa informalmente, 
            ambas partes acuerdan someterse a mediación antes de iniciar cualquier litigio.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-6">20. Disposiciones Generales</h2>
          
          <h3 className="text-white text-xl font-semibold mb-3">20.1 Acuerdo Completo</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            Estos Términos, junto con la Política de Privacidad, constituyen el acuerdo completo entre 
            tú y Macch respecto al Servicio.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">20.2 Divisibilidad</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            Si alguna disposición de estos Términos se considera inválida o inaplicable, dicha disposición 
            se modificará en la medida mínima necesaria, y las disposiciones restantes permanecerán en 
            pleno vigor y efecto.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">20.3 Renuncia</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            El hecho de que Macch no ejerza cualquier derecho o disposición de estos Términos no constituirá 
            una renuncia a dicho derecho o disposición.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">20.4 Cesión</h3>
          <p className="text-gray-400 leading-relaxed mb-6">
            No puedes ceder o transferir estos Términos sin nuestro consentimiento previo por escrito. 
            Macch puede ceder estos Términos sin restricción.
          </p>

          <h3 className="text-white text-xl font-semibold mb-3">20.5 Notificaciones</h3>
          <p className="text-gray-400 leading-relaxed">
            Las notificaciones a Macch deben enviarse por correo electrónico a la dirección indicada abajo. 
            Las notificaciones hacia ti se enviarán a través del Servicio o al número de WhatsApp registrado.
          </p>
        </section>

        <section className="mb-12">
          <h2 className="text-white text-2xl md:text-3xl font-bold mb-4">21. Contacto</h2>
          <div className="bg-white/5 backdrop-blur-sm border border-white/10 rounded-lg p-6">
            <p className="text-gray-400 leading-relaxed mb-4">
              Si tienes preguntas sobre estos Términos de Servicio, puedes contactarnos:
            </p>
            <p className="text-gray-400 leading-relaxed">
              <span className="text-white font-semibold">Macch</span><br />
              Email: <a href="mailto:legal@macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">legal@macch.ai</a><br />
              Sitio web: <a href="https://macch.ai" className="text-blue-500 hover:text-blue-400 transition-colors">https://macch.ai</a>
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}

