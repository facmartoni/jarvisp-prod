import type { Meta, StoryObj } from '@storybook/react-vite'
import FeatureCard from '@/components/ui/FeatureCard'

const FeatureCardGrid = () => {
  const features = [
    {
      image: '/donarosablue.png',
      imageAlt: 'Agente de Voz',
      title: 'Agente de Voz',
      description: 'Nuestros agentes pueden atender llamadas telefónicas 24/7, responder consultas de clientes y procesar reclamos.',
      accentColor: 'rgba(59, 130, 246, 0.7)',
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'WhatsApp Business',
      title: 'Integración con WhatsApp',
      description: 'Conectá tu sistema con WhatsApp Business y permití que tus clientes se comuniquen por el canal que prefieren.',
      accentColor: 'rgba(168, 85, 247, 0.65)',
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'Personalización',
      title: 'Personalización Total',
      description: 'Cada agente se adapta a tu sistema de gestión y conoce a tus clientes por nombre.',
      accentColor: 'rgba(34, 197, 94, 0.65)',
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'Analytics',
      title: 'Reportes y Analytics',
      description: 'Obtené insights detallados sobre las interacciones con tus clientes e identifica problemas recurrentes.',
      accentColor: 'rgba(249, 115, 22, 0.65)',
    },
  ]

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-7xl p-8">
      {features.map((feature) => (
        <FeatureCard
          key={feature.title}
          image={feature.image}
          imageAlt={feature.imageAlt}
          title={feature.title}
          description={feature.description}
          accentColor={feature.accentColor}
        />
      ))}
    </div>
  )
}

const BlueMonochromaticGrid = () => {
  const features = [
    {
      image: '/donarosablue.png',
      imageAlt: 'Agente de Voz',
      title: 'Agente de Voz',
      description: 'Nuestros agentes pueden atender llamadas telefónicas 24/7, responder consultas de clientes y procesar reclamos.',
      accentColor: 'rgba(37, 99, 235, 0.7)', // blue-600
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'WhatsApp Business',
      title: 'Integración con WhatsApp',
      description: 'Conectá tu sistema con WhatsApp Business y permití que tus clientes se comuniquen por el canal que prefieren.',
      accentColor: 'rgba(59, 130, 246, 0.7)', // blue-500
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'Personalización',
      title: 'Personalización Total',
      description: 'Cada agente se adapta a tu sistema de gestión y conoce a tus clientes por nombre.',
      accentColor: 'rgba(96, 165, 250, 0.65)', // blue-400
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'Analytics',
      title: 'Reportes y Analytics',
      description: 'Obtené insights detallados sobre las interacciones con tus clientes e identifica problemas recurrentes.',
      accentColor: 'rgba(147, 197, 253, 0.65)', // blue-300
    },
    {
      image: '/donarosablue.png',
      imageAlt: 'Soporte 24/7',
      title: 'Soporte 24/7',
      description: 'Nuestro equipo de agentes está disponible en todo momento para brindar asistencia inmediata.',
      accentColor: 'rgba(30, 64, 175, 0.7)', // blue-800
    },
  ]

  return (
    <div className="flex items-center justify-center w-full h-full">
      <div className="scale-50">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-7xl p-8">
          {features.map((feature) => (
            <FeatureCard
              key={feature.title}
              image={feature.image}
              imageAlt={feature.imageAlt}
              title={feature.title}
              description={feature.description}
              accentColor={feature.accentColor}
            />
          ))}
        </div>
      </div>
    </div>
  )
}

const meta = {
  title: 'Components/FeatureCardGrid',
  component: FeatureCardGrid,
  parameters: {
    layout: 'fullscreen',
  },
  tags: ['autodocs'],
} satisfies Meta<typeof FeatureCardGrid>

export default meta
type Story = StoryObj<typeof meta>

export const TwoPerRow: Story = {}

export const BlueMonochromatic: StoryObj<typeof BlueMonochromaticGrid> = {
  render: () => <BlueMonochromaticGrid />,
  parameters: {
    layout: 'padded',
  },
}

