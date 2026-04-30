import React, { ReactNode } from 'react';

interface SidebarItemProps {
  /** Icono del item */
  icon: ReactNode;
  /** Etiqueta del item */
  label: string;
  /** URL del item */
  href: string;
  /** Si está activo */
  isActive?: boolean;
}

/**
 * Item individual del sidebar
 */
export const SidebarItem: React.FC<SidebarItemProps> = ({
  icon,
  label,
  href,
  isActive = false,
}) => {
  return (
    <a
      href={href}
      className={`
        flex items-center gap-3 px-4 py-3 rounded-lg
        transition-all duration-200 text-sm font-medium
        ${
          isActive
            ? 'bg-blue-100 text-blue-600'
            : 'text-gray-700 hover:bg-gray-100'
        }
      `.trim()}
    >
      <span className="text-lg flex-shrink-0">{icon}</span>
      <span>{label}</span>
    </a>
  );
};

interface SidebarProps {
  /** Items del sidebar */
  items: SidebarItemProps[];
  /** Contenido adicional en el footer del sidebar */
  footer?: ReactNode;
  /** Si el sidebar está colapsado (móvil) */
  collapsed?: boolean;
  /** Callback para cerrar sidebar en móvil */
  onClose?: () => void;
}

/**
 * Componente Sidebar con navegación principal
 */
export const Sidebar: React.FC<SidebarProps> = ({
  items,
  footer,
  collapsed = false,
  onClose,
}) => {
  return (
    <>
      {/* Overlay en móvil */}
      {collapsed && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-30 md:hidden"
          onClick={onClose}
        />
      )}

      {/* Sidebar */}
      <aside
        className={`
          fixed left-0 top-0 h-full bg-white border-r border-gray-200
          transform transition-transform duration-300
          ${collapsed ? 'translate-x-0 z-40' : '-translate-x-full md:translate-x-0'}
          md:static md:w-64 flex flex-col
          pt-20 md:pt-0
        `.trim()}
      >
        {/* Logo/Branding */}
        <div className="px-6 py-4 border-b border-gray-200">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold">
              🎓
            </div>
            <h1 className="text-lg font-bold text-gray-900">Caja Tools</h1>
          </div>
        </div>

        {/* Items */}
        <nav className="flex-1 px-3 py-4 space-y-1 overflow-y-auto">
          {items.map((item, idx) => (
            <SidebarItem key={idx} {...item} />
          ))}
        </nav>

        {/* Footer */}
        {footer && (
          <div className="px-3 py-4 border-t border-gray-200">
            {footer}
          </div>
        )}
      </aside>
    </>
  );
};

Sidebar.displayName = 'Sidebar';

export default Sidebar;
