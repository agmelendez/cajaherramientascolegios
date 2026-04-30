import React, { ReactNode } from 'react';

interface ModalProps {
  /** Si el modal está abierto */
  isOpen: boolean;
  /** Título del modal */
  title: string;
  /** Contenido del modal */
  children: ReactNode;
  /** Callback para cerrar el modal */
  onClose: () => void;
  /** Botones de acción en el footer */
  actions?: ReactNode;
  /** Si el modal es grande */
  size?: 'sm' | 'md' | 'lg';
  /** Si permite cerrar clickeando afuera */
  closable?: boolean;
  /** Icono en el header */
  icon?: ReactNode;
  /** Clases personalizadas */
  className?: string;
}

const sizeStyles: Record<string, string> = {
  sm: 'max-w-sm',
  md: 'max-w-md',
  lg: 'max-w-lg',
};

/**
 * Componente Modal para diálogos
 *
 * @example
 * const [isOpen, setIsOpen] = useState(false);
 * return (
 *   <>
 *     <button onClick={() => setIsOpen(true)}>Abrir</button>
 *     <Modal
 *       isOpen={isOpen}
 *       title="Confirmar acción"
 *       onClose={() => setIsOpen(false)}
 *       actions={
 *         <div className="flex gap-2">
 *           <Button variant="secondary">Cancelar</Button>
 *           <Button>Confirmar</Button>
 *         </div>
 *       }
 *     >
 *       ¿Estás seguro?
 *     </Modal>
 *   </>
 * );
 */
export const Modal: React.FC<ModalProps> = ({
  isOpen,
  title,
  children,
  onClose,
  actions,
  size = 'md',
  closable = true,
  icon,
  className,
}) => {
  React.useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }

    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={closable ? onClose : undefined}
      />

      {/* Modal */}
      <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
        <div
          className={`
            ${sizeStyles[size]}
            w-full bg-white rounded-lg shadow-2xl
            transform transition-all
            ${className || ''}
          `.trim()}
        >
          {/* Header */}
          <div className="flex items-center justify-between p-6 border-b border-gray-200">
            <div className="flex items-center gap-3">
              {icon && <span className="text-2xl">{icon}</span>}
              <h2 className="text-xl font-semibold text-gray-900">{title}</h2>
            </div>
            {closable && (
              <button
                onClick={onClose}
                className="text-gray-500 hover:text-gray-700 transition-colors"
                aria-label="Cerrar"
              >
                ✕
              </button>
            )}
          </div>

          {/* Content */}
          <div className="p-6 max-h-96 overflow-y-auto">{children}</div>

          {/* Footer */}
          {actions && (
            <div className="p-6 border-t border-gray-200 bg-gray-50 rounded-b-lg">
              {actions}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

Modal.displayName = 'Modal';

export default Modal;
