import React, { ReactNode, CSSProperties } from 'react';

type CardVariant = 'default' | 'elevated' | 'outlined';

interface CardProps {
  /** Contenido de la tarjeta */
  children: ReactNode;
  /** Variante visual */
  variant?: CardVariant;
  /** Espaciado interno (padding) */
  padding?: 'sm' | 'md' | 'lg';
  /** Título opcional */
  title?: string;
  /** Subtítulo opcional */
  subtitle?: string;
  /** Mostrar separador entre header y contenido */
  separator?: boolean;
  /** Ancho máximo */
  maxWidth?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
  /** Clases personalizadas */
  className?: string;
  /** Estilos inline */
  style?: CSSProperties;
  /** Footer opcional */
  footer?: ReactNode;
  /** Icono en el header */
  icon?: ReactNode;
}

const variantStyles: Record<CardVariant, string> = {
  default: 'bg-white border border-gray-200 rounded-lg',
  elevated:
    'bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow duration-200',
  outlined: 'bg-transparent border-2 border-blue-200 rounded-lg',
};

const paddingStyles: Record<string, string> = {
  sm: 'p-4',
  md: 'p-6',
  lg: 'p-8',
};

const maxWidthStyles: Record<string, string> = {
  sm: 'max-w-sm',
  md: 'max-w-md',
  lg: 'max-w-lg',
  xl: 'max-w-xl',
  full: 'w-full',
};

/**
 * Componente Card reutilizable para contenedores de contenido
 *
 * @example
 * // Card simple
 * <Card>Contenido aquí</Card>
 *
 * @example
 * // Card con título y elevación
 * <Card variant="elevated" title="Módulos disponibles">
 *   Lista de módulos
 * </Card>
 *
 * @example
 * // Card con footer
 * <Card
 *   title="Crear módulo"
 *   footer={<Button>Guardar</Button>}
 * >
 *   Formulario aquí
 * </Card>
 */
export const Card: React.FC<CardProps> = ({
  children,
  variant = 'default',
  padding = 'md',
  title,
  subtitle,
  separator = true,
  maxWidth = 'full',
  className,
  style,
  footer,
  icon,
}) => {
  return (
    <div
      className={`
        ${variantStyles[variant]}
        ${maxWidthStyles[maxWidth]}
        overflow-hidden
        ${className || ''}
      `.trim()}
      style={style}
    >
      {/* Header */}
      {(title || subtitle || icon) && (
        <div className={`${paddingStyles[padding]} ${separator ? 'pb-4' : ''}`}>
          <div className="flex items-start gap-3">
            {icon && <span className="text-2xl flex-shrink-0">{icon}</span>}
            <div className="flex-grow">
              {title && (
                <h2 className="text-lg font-semibold text-gray-900">
                  {title}
                </h2>
              )}
              {subtitle && (
                <p className="text-sm text-gray-600 mt-1">{subtitle}</p>
              )}
            </div>
          </div>
          {separator && <div className="border-t border-gray-200 mt-4" />}
        </div>
      )}

      {/* Contenido */}
      <div className={separator && !title ? paddingStyles[padding] : ''}>
        {!title && !subtitle && !icon ? (
          <div className={paddingStyles[padding]}>{children}</div>
        ) : (
          <div className={title || subtitle || icon ? '' : ''}>{children}</div>
        )}
      </div>

      {/* Footer */}
      {footer && (
        <div
          className={`
            border-t border-gray-200
            ${paddingStyles[padding]}
            bg-gray-50
          `.trim()}
        >
          {footer}
        </div>
      )}
    </div>
  );
};

Card.displayName = 'Card';

export default Card;
