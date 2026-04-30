import React, { InputHTMLAttributes, ReactNode } from 'react';

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  /** Etiqueta del input */
  label?: string;
  /** Mensaje de error (muestra el input en rojo) */
  error?: string;
  /** Texto de ayuda debajo del input */
  helper?: string;
  /** Icono a mostrar a la izquierda del input */
  icon?: ReactNode;
  /** Si el campo es requerido */
  required?: boolean;
}

/**
 * Componente Input reutilizable con label, error y helper text
 *
 * @example
 * // Input básico
 * <Input type="text" placeholder="Nombre" />
 *
 * @example
 * // Input con validación
 * <Input
 *   label="Email"
 *   type="email"
 *   error={emailError}
 *   helper="Usamos esto para notificaciones"
 * />
 *
 * @example
 * // Input con icono
 * <Input
 *   label="Búsqueda"
 *   icon={<SearchIcon />}
 *   placeholder="Buscar módulos..."
 * />
 */
export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, helper, icon, required, className, ...props }, ref) => {
    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={props.id}
            className="block text-sm font-medium text-gray-700 mb-2"
          >
            {label}
            {required && <span className="text-red-500 ml-1">*</span>}
          </label>
        )}

        <div className="relative">
          {icon && (
            <span className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">
              {icon}
            </span>
          )}

          <input
            ref={ref}
            className={`
              w-full px-4 py-2.5 text-base border rounded-lg
              ${icon ? 'pl-10' : 'pl-4'}
              font-inter transition-all duration-200
              ${
                error
                  ? 'border-red-500 focus:outline-none focus:ring-2 focus:ring-red-500'
                  : 'border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent'
              }
              disabled:bg-gray-100 disabled:text-gray-500 disabled:cursor-not-allowed
              ${className || ''}
            `.trim()}
            {...props}
          />
        </div>

        {error && <p className="text-sm text-red-600 mt-1">{error}</p>}
        {helper && !error && (
          <p className="text-sm text-gray-500 mt-1">{helper}</p>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';

export default Input;
