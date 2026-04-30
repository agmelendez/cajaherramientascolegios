import React, { ReactNode } from 'react';

interface AlertProps {
  /** Tipo de alerta */
  type?: 'success' | 'error' | 'warning' | 'info';
  /** Título de la alerta */
  title?: string;
  /** Mensaje de la alerta */
  message: string;
  /** Icono personalizado */
  icon?: ReactNode;
  /** Si es dismissible (tiene botón de cerrar) */
  dismissible?: boolean;
  /** Callback cuando se cierra */
  onClose?: () => void;
  /** Clases personalizadas */
  className?: string;
}

const typeStyles: Record<string, Record<string, string>> = {
  success: {
    container: 'bg-green-50 border border-green-200',
    text: 'text-green-800',
    title: 'text-green-900 font-semibold',
    icon: 'text-green-600',
    button: 'text-green-600 hover:text-green-800',
  },
  error: {
    container: 'bg-red-50 border border-red-200',
    text: 'text-red-800',
    title: 'text-red-900 font-semibold',
    icon: 'text-red-600',
    button: 'text-red-600 hover:text-red-800',
  },
  warning: {
    container: 'bg-yellow-50 border border-yellow-200',
    text: 'text-yellow-800',
    title: 'text-yellow-900 font-semibold',
    icon: 'text-yellow-600',
    button: 'text-yellow-600 hover:text-yellow-800',
  },
  info: {
    container: 'bg-blue-50 border border-blue-200',
    text: 'text-blue-800',
    title: 'text-blue-900 font-semibold',
    icon: 'text-blue-600',
    button: 'text-blue-600 hover:text-blue-800',
  },
};

const defaultIcons: Record<string, string> = {
  success: '✓',
  error: '✕',
  warning: '⚠',
  info: 'ℹ',
};

/**
 * Componente Alert para mensajes al usuario
 *
 * @example
 * // Alerta de éxito simple
 * <Alert type="success" message="Módulo guardado correctamente" />
 *
 * @example
 * // Alerta con título y cerrable
 * <Alert
 *   type="error"
 *   title="Error al guardar"
 *   message="Verifica que todos los campos sean válidos"
 *   dismissible
 *   onClose={handleClose}
 * />
 */
export const Alert: React.FC<AlertProps> = ({
  type = 'info',
  title,
  message,
  icon,
  dismissible = false,
  onClose,
  className,
}) => {
  const [isVisible, setIsVisible] = React.useState(true);

  const handleClose = () => {
    setIsVisible(false);
    onClose?.();
  };

  if (!isVisible) return null;

  const styles = typeStyles[type];

  return (
    <div
      className={`
        ${styles.container}
        rounded-lg p-4
        ${className || ''}
      `.trim()}
    >
      <div className="flex gap-3">
        {(icon || defaultIcons[type]) && (
          <div className={`flex-shrink-0 text-xl ${styles.icon}`}>
            {icon || defaultIcons[type]}
          </div>
        )}

        <div className="flex-grow">
          {title && <p className={styles.title}>{title}</p>}
          <p className={`text-sm ${styles.text}`}>{message}</p>
        </div>

        {dismissible && (
          <button
            onClick={handleClose}
            className={`
              flex-shrink-0 text-xl
              ${styles.button}
              transition-colors duration-200
            `.trim()}
            aria-label="Cerrar alerta"
          >
            ×
          </button>
        )}
      </div>
    </div>
  );
};

Alert.displayName = 'Alert';

export default Alert;
