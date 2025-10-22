import type { Meta, StoryObj } from '@storybook/react-vite'
import FeatureCard from '@/components/ui/FeatureCard'

const meta = {
  title: 'Components/FeatureCard',
  component: FeatureCard,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    accentColor: {
      control: 'color',
    },
  },
} satisfies Meta<typeof FeatureCard>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Agente de Voz',
    description: 'Nuestros agentes pueden atender llamadas telefónicas 24/7, responder consultas de clientes, procesar reclamos y brindar soporte técnico en tiempo real.',
    accentColor: 'rgba(59, 130, 246, 0.65)',
  },
}

export const VibrantBlue: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Integración con WhatsApp',
    description: 'Conectá tu sistema con WhatsApp Business y permití que tus clientes se comuniquen por el canal que prefieren, con respuestas automáticas e inteligentes.',
    accentColor: 'rgba(59, 130, 246, 0.7)',
  },
}

export const VibrantPurple: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Personalización Total',
    description: 'Cada agente se adapta a tu sistema de gestión, conoce a tus clientes por nombre y puede acceder a su información de cuenta para brindar un servicio personalizado.',
    accentColor: 'rgba(168, 85, 247, 0.65)',
  },
}

export const VibrantGreen: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Reportes y Analytics',
    description: 'Obtené insights detallados sobre las interacciones con tus clientes, identifica problemas recurrentes y mejora continuamente tu servicio.',
    accentColor: 'rgba(34, 197, 94, 0.65)',
  },
}

export const VibrantOrange: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Soporte 24/7',
    description: 'Nuestro equipo está disponible las 24 horas del día, los 7 días de la semana para ayudarte con cualquier consulta o problema.',
    accentColor: 'rgba(249, 115, 22, 0.65)',
  },
}

export const VibrantPink: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Experiencia Premium',
    description: 'Ofrecemos una experiencia de cliente premium que supera las expectativas y fideliza a tus usuarios.',
    accentColor: 'rgba(236, 72, 153, 0.65)',
  },
}

export const LongContent: Story = {
  args: {
    image: '/donarosablue.png',
    imageAlt: 'Feature illustration',
    title: 'Título Muy Largo Para Probar El Layout',
    description: 'Esta es una descripción extremadamente larga para probar cómo se comporta el componente con mucho contenido. Incluye múltiples líneas de texto, detalles extensos sobre la funcionalidad, y permite verificar que el diseño se mantiene coherente incluso con cantidades significativas de texto. El componente debe manejar esto de manera elegante.',
  },
}

