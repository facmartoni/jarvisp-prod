import { useEffect, useRef } from 'react'
import './Robot.css'

type AnimationType = 'loading' | 'blinking' | 'winking' | 'scanning' | 'dancing' | 'alert' | 'cycle'

interface RobotProps {
  animation?: AnimationType
  className?: string
}

function Robot({ animation = 'cycle', className = '' }: RobotProps) {
  const robotRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!robotRef.current) return
    
    if (animation === 'cycle') {
      const animations = ['loading', 'blinking', 'winking', 'scanning', 'dancing', 'alert']
      let currentIndex = 0

      function rotateAnimation() {
        if (!robotRef.current) return
        robotRef.current.className = 'robot'
        setTimeout(() => {
          if (!robotRef.current) return
          robotRef.current.classList.add(animations[currentIndex])
          currentIndex = (currentIndex + 1) % animations.length
        }, 100)
      }

      robotRef.current.classList.add('loading')
      const interval = setInterval(rotateAnimation, 3000)

      return () => clearInterval(interval)
    } else {
      robotRef.current.className = `robot ${animation}`
    }
  }, [animation])

  return (
    <div className={`robot-container ${className}`}>
      <div className="robot" ref={robotRef}>
        <div className="signal">
          <div className="wave wave3"></div>
          <div className="wave wave2"></div>
          <div className="wave wave1"></div>
        </div>
        <div className="antenna"></div>
        <div className="head">
          <div className="ear left"></div>
          <div className="ear right"></div>
          <div className="face">
            <div className="eyes">
              <div className="eye left">
                <div className="eyelid"></div>
              </div>
              <div className="eye right">
                <div className="eyelid"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Robot

