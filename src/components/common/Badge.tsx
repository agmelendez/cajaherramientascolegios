import React, { ReactNode } from 'react';

interface BadgeProps {
  /** Contenido del badge */
  children: ReactNode;
  /** Variante visual */
  variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'error' | 'info';
  /** Tamaño del badge */
  size?: 'sm' | 'md' | 'lg';
  /** Si es removible */
  removable?: boolean;
  /** Callback cuando se remueve */
  onRemove?: () => void;
  /** Icono opcional */
  icon?: ReactNode;
  /** Clases personalizadas */
  className?: string;
}

const variantStyles: Record<string, string> = {
  primary: 'bg-blue-100 text-blue-800',
  secondary: 'bg-gray-100 text-gray-800',
  success: 'bg-green-100 text-green-800',
  warning: 'bg-yellow-100 text-yellow-800',
  error: 'bg-red-100 text-red-800',
  info: 'bg-indigo-100 text-indigo-800',
};

const sizeStyles: Record<string, string> = {
  sm: 'px-2.5 py-0.5 text-xs',
  md: 'px-3 py-1 text-sm',
  lg: 'px-4 py-1.5 text-base',
};

/**
 * Componente Badge para etiquetas y estados
 *
 * @example
 * // Badge simple
 * <Badge>Activo</Badge>
 *
 * @example
 * // Badge removible con icono
 * <Badge variant="success" icon={<CheckIcon />} removable onRemove={handleRemove}>
 *   Completado
 * </Badge>
 */
export const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  removable = false,
  onRemove,
  icon,
  className,
}) => {
  return (
    <span
      className={`
        inline-flex items-center gap-1.5
        rounded-full font-medium
        ${variantStyles[variant]}
        ${sizeStyles[size]}
        ${className || ''}
      `.trim()}
    >
      {icon && <span>{icon}</span>}
      {children}
      {removable && (
        <button
          onClick={onRemove}
          className="ml-1 hover:opacity-70 transition-opacity"
          aria-label="Remover"
        >
          ×
        </button>
      )}
    </span>
  );
};

Badge.displayName = 'Badge';

export default Badge;
