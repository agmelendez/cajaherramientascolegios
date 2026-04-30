import React, { ReactNode } from 'react';

interface TabsProps {
  /** Arreglo de tabs */
  tabs: Tab[];
  /** Tab activo por defecto */
  defaultTab?: string;
  /** Callback cuando cambia el tab activo */
  onChange?: (tabId: string) => void;
  /** Clases personalizadas para el contenedor */
  className?: string;
}

interface Tab {
  /** ID único del tab */
  id: string;
  /** Etiqueta del tab */
  label: string;
  /** Contenido del tab */
  content: ReactNode;
  /** Icono opcional */
  icon?: ReactNode;
  /** Si el tab está deshabilitado */
  disabled?: boolean;
}

/**
 * Componente Tabs para organizar contenido en múltiples vistas
 *
 * @example
 * const tabs = [
 *   { id: 'modulos', label: 'Módulos', content: <ModulesList /> },
 *   { id: 'usuarios', label: 'Usuarios', content: <UsersList /> },
 * ];
 * <Tabs tabs={tabs} onChange={(id) => console.log(id)} />
 */
export const Tabs: React.FC<TabsProps> = ({
  tabs,
  defaultTab,
  onChange,
  className,
}) => {
  const [activeTab, setActiveTab] = React.useState<string>(
    defaultTab || tabs[0]?.id || ''
  );

  const handleTabClick = (tabId: string) => {
    if (!tabs.find((t) => t.id === tabId)?.disabled) {
      setActiveTab(tabId);
      onChange?.(tabId);
    }
  };

  const activeTabContent = tabs.find((t) => t.id === activeTab)?.content;

  return (
    <div className={className}>
      {/* Tab buttons */}
      <div className="border-b border-gray-200 bg-white rounded-t-lg overflow-x-auto">
        <div className="flex gap-1 px-1 py-1">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => handleTabClick(tab.id)}
              disabled={tab.disabled}
              className={`
                px-4 py-2.5 text-sm font-medium
                border-b-2 transition-all duration-200
                flex items-center gap-2 whitespace-nowrap
                ${
                  activeTab === tab.id
                    ? 'border-blue-600 text-blue-600'
                    : 'border-transparent text-gray-600 hover:text-gray-900'
                }
                ${
                  tab.disabled
                    ? 'opacity-50 cursor-not-allowed'
                    : 'cursor-pointer'
                }
              `.trim()}
            >
              {tab.icon && <span>{tab.icon}</span>}
              {tab.label}
            </button>
          ))}
        </div>
      </div>

      {/* Tab content */}
      <div className="bg-white rounded-b-lg p-6 animate-fadeIn">
        {activeTabContent}
      </div>
    </div>
  );
};

Tabs.displayName = 'Tabs';

export default Tabs;
