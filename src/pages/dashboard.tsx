import React from 'react';
import { MainLayout } from '@/components/layout';
import { Card, Button, Badge, Input } from '@/components/common';

/**
 * Página de Dashboard - Demo del layout completo
 * Accede en: http://localhost:3000/dashboard
 */
export default function Dashboard() {
  const sidebarItems = [
    { icon: '📊', label: 'Dashboard', href: '/dashboard', isActive: true },
    { icon: '📚', label: 'Módulos', href: '/modulos' },
    { icon: '👥', label: 'Usuarios', href: '/usuarios' },
    { icon: '📋', label: 'Temas', href: '/temas' },
    { icon: '⚙️', label: 'Configuración', href: '/config' },
    { icon: '❓', label: 'Soporte', href: '/soporte' },
  ];

  const headerRight = (
    <div className="flex items-center gap-4">
      <div className="hidden md:flex items-center gap-2 px-3 py-2 bg-gray-100 rounded-lg">
        <span>🔔</span>
        <span className="text-sm text-gray-600">Notificaciones</span>
      </div>
      <div className="flex items-center gap-2 p-2 hover:bg-gray-100 rounded-lg cursor-pointer">
        <img
          src="https://via.placeholder.com/32"
          alt="Avatar"
          className="w-8 h-8 rounded-full"
        />
        <span className="hidden md:block text-sm font-medium">Agustín</span>
      </div>
    </div>
  );

  const headerLeft = (
    <div className="flex items-center gap-2">
      <Input
        type="text"
        placeholder="Buscar módulos..."
        className="w-64"
      />
    </div>
  );

  return (
    <MainLayout
      sidebarItems={sidebarItems}
      activeItem="/dashboard"
      headerLeft={headerLeft}
      headerRight={headerRight}
      showFooter={true}
    >
      <div className="space-y-6">
        {/* Header Section */}
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600 mt-2">
            Bienvenido a la Caja de Herramientas de Autoformación Docente en IA
          </p>
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <Card variant="elevated" padding="md">
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600">12</div>
              <p className="text-gray-600 text-sm mt-2">Módulos Activos</p>
            </div>
          </Card>

          <Card variant="elevated" padding="md">
            <div className="text-center">
              <div className="text-4xl font-bold text-green-600">156</div>
              <p className="text-gray-600 text-sm mt-2">Docentes Registrados</p>
            </div>
          </Card>

          <Card variant="elevated" padding="md">
            <div className="text-center">
              <div className="text-4xl font-bold text-orange-600">89%</div>
              <p className="text-gray-600 text-sm mt-2">Completación Promedio</p>
            </div>
          </Card>

          <Card variant="elevated" padding="md">
            <div className="text-center">
              <div className="text-4xl font-bold text-purple-600">42</div>
              <p className="text-gray-600 text-sm mt-2">Microcontenidos</p>
            </div>
          </Card>
        </div>

        {/* Content Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Main Content */}
          <div className="lg:col-span-2 space-y-4">
            <Card
              variant="elevated"
              title="🚀 Módulos Recientes"
              padding="md"
            >
              <div className="space-y-3">
                {[1, 2, 3].map((i) => (
                  <div key={i} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                    <div>
                      <p className="font-medium text-gray-900">
                        Módulo {i}: IA en Educación
                      </p>
                      <p className="text-sm text-gray-600">
                        4 temas • 42 minutos total
                      </p>
                    </div>
                    <Badge variant="success">Activo</Badge>
                  </div>
                ))}
              </div>
            </Card>

            <Card
              variant="elevated"
              title="📊 Actividad Reciente"
              padding="md"
            >
              <div className="space-y-2">
                <p className="text-sm text-gray-600">
                  ✅ 23 docentes completaron módulo 1
                </p>
                <p className="text-sm text-gray-600">
                  📝 5 nuevas respuestas en foro
                </p>
                <p className="text-sm text-gray-600">
                  🎓 12 certificados emitidos
                </p>
              </div>
            </Card>
          </div>

          {/* Sidebar */}
          <div className="space-y-4">
            <Card
              variant="elevated"
              title="ℹ️ Información"
              padding="md"
            >
              <div className="space-y-3 text-sm text-gray-600">
                <div>
                  <p className="font-medium text-gray-900">Versión</p>
                  <p>1.0.0</p>
                </div>
                <div>
                  <p className="font-medium text-gray-900">Última actualización</p>
                  <p>28 de abril, 2026</p>
                </div>
                <div>
                  <p className="font-medium text-gray-900">Estado</p>
                  <Badge variant="success" size="sm">En línea</Badge>
                </div>
              </div>
            </Card>

            <Card
              variant="elevated"
              title="🎯 Acciones Rápidas"
              padding="md"
              footer={
                <Button size="sm" fullWidth>
                  Ver más acciones
                </Button>
              }
            >
              <div className="space-y-2">
                <Button variant="secondary" size="sm" fullWidth>
                  Crear módulo
                </Button>
                <Button variant="secondary" size="sm" fullWidth>
                  Invitar docente
                </Button>
              </div>
            </Card>

            <Card
              variant="outlined"
              title="📢 Anuncios"
              padding="md"
            >
              <div className="space-y-2 text-sm">
                <p className="text-gray-600">
                  Próxima actualización: Mayo 5, 2026
                </p>
              </div>
            </Card>
          </div>
        </div>
      </div>
    </MainLayout>
  );
}
