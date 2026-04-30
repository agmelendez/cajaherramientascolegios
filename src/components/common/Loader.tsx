import React, { ReactNode } from 'react';

interface LoaderProps {
  /** Texto a mostrar debajo del spinner */
  message?: string;
  /** Tamaño del loader */
  size?: 'sm' | 'md' | 'lg';
  /** Tipo de animación */
  type?: 'spinner' | 'dots' | 'pulse';
  /** Si debe ocupar toda la pantalla */
  fullscreen?: boolean;
  /** Clases personalizadas */
  className?: string;
}

const sizeStyles: Record<string, string> = {
  sm: 'w-6 h-6',
  md: 'w-12 h-12',
  lg: 'w-16 h-16',
};

/**
 * Componente Loader para estados de carga
 *
 * @example
 * // Loader simple
 * <Loader message="Cargando..." />
 *
 * @example
 * // Loader fullscreen
 * <Loader fullscreen message="Inicializando aplicación" />
 */
export const Loader: React.FC<LoaderProps> = ({
  message,
  size = 'md',
  type = 'spinner',
  fullscreen = false,
  className,
}) => {
  const renderLoader = () => {
    switch (type) {
      case 'dots':
        return (
          <div className={`flex gap-1 justify-center ${sizeStyles[size]}`}>
            {[0, 1, 2].map((i) => (
              <div
                key={i}
                className="bg-blue-600 rounded-full animate-bounce"
                style={{
                  animation: `bounce 1.4s infinite both`,
                  animationDelay: `${i * 0.16}s`,
                  width: '8px',
                  height: '8px',
                }}
              />
            ))}
          </div>
        );

      case 'pulse':
        return (
          <div
            className={`
              ${sizeStyles[size]}
              bg-blue-600 rounded-full
              animate-pulse
            `.trim()}
          />
        );

      case 'spinner':
      default:
        return (
          <div
            className={`
              ${sizeStyles[size]}
              border-4 border-blue-200 border-t-blue-600
              rounded-full
              animate-spin
            `.trim()}
          />
        );
    }
  };

  const content = (
    <div className="flex flex-col items-center justify-center gap-4">
      {renderLoader()}
      {message && <p className="text-gray-600 text-sm font-medium">{message}</p>}
    </div>
  );

  if (fullscreen) {
    return (
      <div
        className={`
          fixed inset-0 bg-white bg-opacity-90
          flex items-center justify-center
          z-40
          ${className || ''}
        `.trim()}
      >
        {content}
      </div>
    );
  }

  return <div className={className}>{content}</div>;
};

Loader.displayName = 'Loader';

export default Loader;
