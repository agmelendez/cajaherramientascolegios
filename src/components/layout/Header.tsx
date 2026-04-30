import React, { ReactNode } from 'react';

interface HeaderProps {
  /** Contenido del lado izquierdo (usuario, búsqueda, etc) */
  left?: ReactNode;
  /** Contenido del lado derecho (notificaciones, perfil, etc) */
  right?: ReactNode;
  /** Callback para abrir sidebar en móvil */
  onMenuClick?: () => void;
  /** Si mostrar el botón de menú */
  showMenuButton?: boolean;
}

/**
 * Componente Header/Navbar de la aplicación
 * Responsivo, con soporte para móvil
 */
export const Header: React.FC<HeaderProps> = ({
  left,
  right,
  onMenuClick,
  showMenuButton = true,
}) => {
  return (
    <header
      className={`
        fixed top-0 left-0 right-0 h-20
        bg-white border-b border-gray-200
        z-20
      `.trim()}
    >
      <div className="h-full px-4 md:px-6 flex items-center justify-between">
        {/* Izquierda */}
        <div className="flex items-center gap-4">
          {/* Botón de menú en móvil */}
          {showMenuButton && (
            <button
              onClick={onMenuClick}
              className={`
                md:hidden p-2 hover:bg-gray-100
                rounded-lg transition-colors
              `.trim()}
              aria-label="Abrir menú"
            >
              ☰
            </button>
          )}

          {/* Contenido izquierdo */}
          <div className="hidden md:block">{left}</div>
        </div>

        {/* Derecha */}
        <div className="flex items-center gap-4">{right}</div>
      </div>
    </header>
  );
};

Header.displayName = 'Header';

export default Header;
