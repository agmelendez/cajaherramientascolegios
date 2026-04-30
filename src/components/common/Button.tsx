import React, { ButtonHTMLAttributes, ReactNode } from 'react';

/**
 * Variantes de botón
 * - primary: Azul MEP (#0066CC) - Acciones principales
 * - secondary: Gris neutro - Acciones secundarias
 * - success: Verde (#00AA44) - Confirmación, guardar
 * - danger: Rojo (#EF4444) - Eliminar, acciones críticas
 */
type ButtonVariant = 'primary' | 'secondary' | 'success' | 'danger';

/**
 * Tamaños del botón
 * - sm: pequeño (8px padding vertical)
 * - md: mediano (10px padding vertical)
 * - lg: grande (12px padding vertical)
 */
type ButtonSize = 'sm' | 'md' | 'lg';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Variante visual del botón */
  variant?: ButtonVariant;
  /** Tamaño del botón */
  size?: ButtonSize;
  /** Si el botón está en estado de carga */
  isLoading?: boolean;
  /** Contenido del botón */
  children: ReactNode;
  /** Ancho completo del contenedor */
  fullWidth?: boolean;
  /** Icono a mostrar (opcional) */
  icon?: ReactNode;
  /** Posición del icono respecto al texto */
  iconPosition?: 'left' | 'right';
}

const variantStyles: Record<ButtonVariant, string> = {
  primary:
    'bg-blue-600 hover:bg-blue-700 text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2',
  secondary:
    'bg-gray-200 hover:bg-gray-300 text-gray-900 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2',
  success:
    'bg-green-600 hover:bg-green-700 text-white focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2',
  danger:
    'bg-red-600 hover:bg-red-700 text-white focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2',
};

const sizeStyles: Record<ButtonSize, string> = {
  sm: 'px-3 py-2 text-sm font-medium',
  md: 'px-4 py-2.5 text-base font-medium',
  lg: 'px-6 py-3 text-lg font-semibold',
};

/**
 * Componente Button reutilizable
 *
 * @example
 * // Botón primario básico
 * <Button>Guardar</Button>
 *
 * @example
 * // Botón con icono y carga
 * <Button variant="success" isLoading={loading} icon={<SaveIcon />}>
 *   Guardar cambios
 * </Button>
 *
 * @example
 * // Botón peligroso de ancho completo
 * <Button variant="danger" fullWidth>
 *   Eliminar módulo
 * </Button>
 */
export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = 'primary',
      size = 'md',
      isLoading = false,
      fullWidth = false,
      icon,
      iconPosition = 'left',
      disabled,
      className,
      children,
      ...props
    },
    ref
  ) => {
    const baseStyles =
      'inline-flex items-center justify-center gap-2 rounded-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed font-inter';

    const fullWidthStyle = fullWidth ? 'w-full' : '';

    const combinedClassName = `
      ${baseStyles}
      ${variantStyles[variant]}
      ${sizeStyles[size]}
      ${fullWidthStyle}
      ${className || ''}
    `.trim();

    return (
      <button
        ref={ref}
        disabled={disabled || isLoading}
        className={combinedClassName}
        {...props}
      >
        {isLoading ? (
          <>
            <span className="animate-spin inline-block">⏳</span>
            {children}
          </>
        ) : (
          <>
            {icon && iconPosition === 'left' && <span>{icon}</span>}
            {children}
            {icon && iconPosition === 'right' && <span>{icon}</span>}
          </>
        )}
      </button>
    );
  }
);

Button.displayName = 'Button';

export default Button;
