import React, { useState, useEffect, useRef } from 'react';
import { Phone } from 'lucide-react';

interface OrbProps {
  state?: 'idle' | 'connecting' | 'listening' | 'thinking' | 'speaking';
  size?: number;
}

const Orb: React.FC<OrbProps> = ({ 
  state = 'idle',
  size = 256
}) => {
  const [pulseIntensity, setPulseIntensity] = useState(1);
  const animationRef = useRef<number | null>(null);

  useEffect(() => {
    if (state === 'speaking' || state === 'listening') {
      const animate = () => {
        const time = Date.now() * 0.003;
        const intensity = 1 + Math.sin(time) * 0.3 + Math.sin(time * 1.5) * 0.2;
        setPulseIntensity(intensity);
        animationRef.current = requestAnimationFrame(animate);
      };
      animate();
    } else if (state === 'thinking') {
      const animate = () => {
        const time = Date.now() * 0.005;
        const intensity = 1 + Math.sin(time) * 0.15;
        setPulseIntensity(intensity);
        animationRef.current = requestAnimationFrame(animate);
      };
      animate();
    } else if (state === 'connecting') {
      const animate = () => {
        const time = Date.now() * 0.002;
        const intensity = 1 + Math.sin(time) * 0.1;
        setPulseIntensity(intensity);
        animationRef.current = requestAnimationFrame(animate);
      };
      animate();
    } else {
      setPulseIntensity(1);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    }
    return () => {
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [state]);

  const getOrbColors = () => {
    switch (state) {
      case 'connecting':
        return 'from-blue-500 via-blue-400 to-blue-500';
      case 'listening':
        return 'from-blue-400 via-blue-300 to-blue-400';
      case 'thinking':
        return 'from-blue-600 via-blue-500 to-blue-600';
      case 'speaking':
        return 'from-blue-500 via-blue-400 to-cyan-400';
      default:
        return 'from-slate-700 via-slate-600 to-slate-700';
    }
  };

  const isActive = state !== 'idle';
  const glowSize = size * 1.5;
  const innerSize1 = size * 0.875;
  const innerSize2 = size * 0.75;
  const iconSize = size * 0.25;

  return (
    <div className="relative flex items-center justify-center" style={{ width: size, height: size }}>
      {/* Outer glow rings */}
      <div 
        className={`absolute rounded-full bg-gradient-to-r ${getOrbColors()} blur-3xl transition-opacity duration-700 ${
          isActive ? 'opacity-10' : 'opacity-0'
        }`}
        style={{ 
          width: glowSize,
          height: glowSize,
          transform: `scale(${isActive ? pulseIntensity : 1})`,
          transition: 'transform 0.15s ease-out, opacity 0.7s ease-out'
        }}
      />
      <div 
        className={`absolute rounded-full bg-gradient-to-r ${getOrbColors()} blur-2xl transition-opacity duration-500 ${
          isActive ? 'opacity-20' : 'opacity-0'
        }`}
        style={{ 
          width: glowSize * 0.833,
          height: glowSize * 0.833,
          transform: `scale(${isActive ? pulseIntensity * 0.9 : 1})`,
          transition: 'transform 0.15s ease-out, opacity 0.5s ease-out'
        }}
      />
      
      {/* Main Orb */}
      <div 
        className={`relative rounded-full bg-gradient-to-r ${getOrbColors()} flex items-center justify-center transition-all duration-500`}
        style={{ 
          width: size,
          height: size,
          transform: `scale(${isActive ? pulseIntensity : 1})`,
          boxShadow: isActive 
            ? '0 0 60px rgba(59, 130, 246, 0.4), 0 0 100px rgba(59, 130, 246, 0.2)' 
            : '0 10px 40px rgba(0, 0, 0, 0.3)'
        }}
      >
        {/* Inner orb layers */}
        <div 
          className={`rounded-full backdrop-blur-sm flex items-center justify-center transition-all duration-500 ${
            isActive ? 'bg-white/20' : 'bg-white/5'
          }`}
          style={{ width: innerSize1, height: innerSize1 }}
        >
          <div 
            className={`rounded-full backdrop-blur-md flex items-center justify-center transition-all duration-500 ${
              isActive ? 'bg-white/30' : 'bg-white/10'
            }`}
            style={{ width: innerSize2, height: innerSize2 }}
          >
            {/* Idle state */}
            {state === 'idle' && (
              <Phone className="text-white transition-opacity duration-300" style={{ width: iconSize, height: iconSize }} />
            )}
            
            {/* Connecting state */}
            {state === 'connecting' && (
              <div 
                className="border-4 border-white/50 border-t-white rounded-full animate-spin"
                style={{ width: iconSize * 0.75, height: iconSize * 0.75 }}
              />
            )}
            
            {/* Active states - pulsing rings */}
            {state !== 'idle' && state !== 'connecting' && (
              <div className="relative" style={{ width: iconSize * 1.25, height: iconSize * 1.25 }}>
                {[...Array(3)].map((_, i) => (
                  <div
                    key={i}
                    className="absolute inset-0 rounded-full border-2 border-white/50"
                    style={{
                      transform: `scale(${1 + i * 0.3})`,
                      opacity: 1 - i * 0.3,
                      animation: `ping 2s cubic-bezier(0, 0, 0.2, 1) infinite ${i * 0.3}s`
                    }}
                  />
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Orb;