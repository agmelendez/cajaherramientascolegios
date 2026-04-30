import React, { ReactNode, useState } from 'react';
import Header from './Header';
import Sidebar, { SidebarItemProps } from './Sidebar';
import Footer from './Footer';

interface MainLayoutProps {
  /** Contenido principal de la página */
  children: ReactNode;
  /** Items del sidebar */
  sidebarItems?: SidebarItemProps[];
  /** Contenido del header izquierda */
  headerLeft?: ReactNode;
  /** Contenido del header derecha */
  headerRight?: ReactNode;
  /** Contenido del footer */
  footerContent?: ReactNode;
  /** Si mostrar footer */
  showFooter?: boolean;
  /** Item activo del sidebar */
  activeItem?: string;
  /** Clases personalizadas para el main */
  mainClassName?: string;
}

/**
 * Layout principal de la aplicación
 * Combina Header, Sidebar, Main content y Footer
 *
 * @example
 * <MainLayout
 *   sidebarItems={[
 *     { icon: '📊', label: 'Dashboard', href: '/dashboard', isActive: true },
 *     { icon: '📚', label: 'Módulos', href: '/modulos' },
 *   ]}
 *   headerRight={<UserMenu />}
 * >
 *   <Page content aquí />
 * </MainLayout>
 */
export const MainLayout: React.FC<MainLayoutProps> = ({
  children,
  sidebarItems = [],
  headerLeft,
  headerRight,
  footerContent,
  showFooter = true,
  activeItem,
  mainClassName,
}) => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Marcar items activos
  const itemsWithActive = sidebarItems.map((item) => ({
    ...item,
    isActive: activeItem ? item.href === activeItem : item.isActive,
  }));

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      {/* Header */}
      <Header
        left={headerLeft}
        right={headerRight}
        onMenuClick={() => setSidebarOpen(true)}
        showMenuButton={sidebarItems.length > 0}
      />

      {/* Container flex para main content */}
      <div className="flex flex-1 pt-20">
        {/* Sidebar */}
        {sidebarItems.length > 0 && (
          <Sidebar
            items={itemsWithActive}
            collapsed={sidebarOpen}
            onClose={() => setSidebarOpen(false)}
            footer={
              <div className="text-sm text-gray-600 space-y-2">
                <p className="font-medium">👤 Usuario</p>
                <a
                  href="#"
                  className="block hover:text-gray-900 transition-colors"
                >
                  Perfil
                </a>
                <a
                  href="#"
                  className="block hover:text-gray-900 transition-colors"
                >
                  Configuración
                </a>
                <a
                  href="#"
                  className="block hover:text-gray-900 transition-colors"
                >
                  Cerrar sesión
                </a>
              </div>
            }
          />
        )}

        {/* Main content */}
        <main
          className={`
            flex-1 overflow-y-auto
            ${mainClassName || 'p-4 md:p-6'}
          `.trim()}
        >
          <div className="max-w-7xl mx-auto">{children}</div>
        </main>
      </div>

      {/* Footer */}
      {showFooter && <Footer>{footerContent}</Footer>}
    </div>
  );
};

MainLayout.displayName = 'MainLayout';

export default MainLayout;
