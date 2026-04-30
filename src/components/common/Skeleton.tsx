import React, { ReactNode } from 'react';

interface SkeletonProps {
  /** Tipo de esqueleto */
  type?: 'text' | 'circle' | 'rect' | 'card';
  /** Número de líneas (para text) */
  lines?: number;
  /** Altura personalizada */
  height?: string;
  /** Ancho personalizado */
  width?: string;
  /** Clases personalizadas */
  className?: string;
  /** Si debe ocupar todo el ancho disponible */
  fullWidth?: boolean;
}

/**
 * Componente Skeleton para estados de carga
 *
 * @example
 * // Texto en carga
 * <Skeleton type="text" lines={3} />
 *
 * @example
 * // Card en carga
 * <Skeleton type="card" />
 *
 * @example
 * // Avatar en carga
 * <Skeleton type="circle" height="48px" width="48px" />
 */
export const Skeleton: React.FC<SkeletonProps> = ({
  type = 'rect',
  lines = 1,
  height,
  width,
  className,
  fullWidth = false,
}) => {
  const baseClasses = 'bg-gray-200 animate-pulse rounded';

  const getSkeletonStyle = (): React.CSSProperties => {
    switch (type) {
      case 'circle':
        return {
          borderRadius: '9999px',
          height: height || '48px',
          width: width || '48px',
        };
      case 'rect':
        return {
          height: height || '16px',
          width: width || (fullWidth ? '100%' : '100%'),
        };
      case 'text':
        return {
          height: height || '16px',
          width: width || (fullWidth ? '100%' : '100%'),
        };
      case 'card':
        return {
          height: height || '200px',
          width: width || (fullWidth ? '100%' : '100%'),
          borderRadius: '8px',
        };
      default:
        return {};
    }
  };

  if (type === 'text') {
    return (
      <div className="space-y-2">
        {Array.from({ length: lines }).map((_, i) => (
          <div
            key={i}
            className={`${baseClasses} ${className || ''}`}
            style={{
              ...getSkeletonStyle(),
              opacity: i === lines - 1 ? 0.6 : 1,
            }}
          />
        ))}
      </div>
    );
  }

  return (
    <div
      className={`${baseClasses} ${className || ''}`}
      style={getSkeletonStyle()}
    />
  );
};

Skeleton.displayName = 'Skeleton';

export default Skeleton;
