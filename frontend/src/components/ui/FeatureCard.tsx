interface FeatureCardProps {
  image: string
  imageAlt: string
  title: string
  description: string
  accentColor?: string
}

function FeatureCard({ 
  image, 
  imageAlt, 
  title, 
  description,
  accentColor = 'rgba(59, 130, 246, 0.65)'
}: FeatureCardProps) {
  return (
    <div className="relative rounded-xl overflow-hidden transition-all duration-300 hover:shadow-[0_8px_30px_rgba(255,255,255,0.12)] group backdrop-blur-md sm:h-48">
      {/* Vibrant gradient background with color tint */}
      <div 
        className="absolute inset-0 opacity-100 transition-opacity"
        style={{ 
          background: `linear-gradient(135deg, ${accentColor} 0%, ${accentColor.replace('0.65', '0.5').replace('0.7', '0.55')} 100%)`,
        }}
      />
      
      {/* Glass effect overlay */}
      <div className="absolute inset-0 bg-white/5 backdrop-blur-sm" />
      
      {/* Content container */}
      <div className="relative grid grid-cols-1 sm:grid-cols-3 gap-0 h-full">
        {/* Image Section - 1/3 */}
        <div className="sm:col-span-1 h-48 sm:h-full relative hidden sm:block">
          <div className="absolute inset-0 bg-gradient-to-r from-transparent to-black/20 z-10" />
          <img 
            src={image} 
            alt={imageAlt}
            className="w-full h-full object-cover"
          />
        </div>

        {/* Content Section - 2/3 */}
        <div className="col-span-1 sm:col-span-2 p-6 flex flex-col justify-center gap-2 relative z-10">
          <h3 className="text-white text-xl font-bold">
            {title}
          </h3>
          <p className="text-gray-300 text-sm md:text-base leading-relaxed">
            {description}
          </p>
        </div>
      </div>

      {/* Subtle glass border */}
      <div className="absolute inset-0 rounded-xl border border-white/10 group-hover:border-white/20 transition-colors pointer-events-none z-20 shadow-[inset_0_1px_1px_rgba(255,255,255,0.1)]" />
    </div>
  )
}

export default FeatureCard

