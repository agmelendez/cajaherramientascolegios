import React from 'react';
import { MainLayout } from '@/components/layout';
import { Card, Button } from '@/components/common';

/**
 * Página de Inicio
 * Accede en: http://localhost:3000/
 */
export default function Home() {
  const sidebarItems = [
    { icon: '📊', label: 'Dashboard', href: '/dashboard' },
    { icon: '📚', label: 'Módulos', href: '/modulos' },
    { icon: '👥', label: 'Usuarios', href: '/usuarios' },
    { icon: '⚙️', label: 'Configuración', href: '/config' },
  ];

  return (
    <MainLayout
      sidebarItems={sidebarItems}
      activeItem="/dashboard"
      showFooter={true}
    >
      <div className="space-y-8">
        {/* Hero Section */}
        <div className="text-center py-12">
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            🎓 Caja de Herramientas
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            Plataforma de Autoformación Docente en IA
          </p>
          <p className="text-gray-500 max-w-2xl mx-auto">
            Alineada con Guía MEP 2026, REAC 2026 y Lineamientos 2026.
            Microcontenidos autogestionados de máximo 27 minutos.
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card variant="elevated" padding="lg">
            <div className="text-center">
              <div className="text-4xl mb-3">🧠</div>
              <h3 className="text-lg font-semibold mb-2">IA en Educación</h3>
              <p className="text-gray-600 text-sm">
                Aprende los fundamentos de la Inteligencia Artificial aplicada
                al aula
              </p>
            </div>
          </Card>

          <Card variant="elevated" padding="lg">
            <div className="text-center">
              <div className="text-4xl mb-3">🔒</div>
              <h3 className="text-lg font-semibold mb-2">Privacidad y Ética</h3>
              <p className="text-gray-600 text-sm">
                Protege los datos de tus estudiantes y entiende las
                implicaciones éticas
              </p>
            </div>
          </Card>

          <Card variant="elevated" padding="lg">
            <div className="text-center">
              <div className="text-4xl mb-3">💬</div>
              <h3 className="text-lg font-semibold mb-2">Prompts Efectivos</h3>
              <p className="text-gray-600 text-sm">
                Domina el arte de comunicarte con herramientas de IA
              </p>
            </div>
          </Card>
        </div>

        {/* Main Content */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2">
            <Card variant="elevated" title="🚀 Comenzar Ahora" padding="lg">
              <div className="space-y-4">
                <p className="text-gray-700">
                  Elige un módulo para comenzar tu autoformación:
                </p>
                <div className="space-y-3">
                  <div className="p-4 border-l-4 border-blue-600 bg-blue-50 rounded">
                    <h4 className="font-semibold text-gray-900">
                      Módulo 1: Fundamentos de IA
                    </h4>
                    <p className="text-sm text-gray-600 mt-1">
                      Duración: 18 minutos • Nivel: Principiante
                    </p>
                  </div>
                  <div className="p-4 border-l-4 border-green-600 bg-green-50 rounded">
                    <h4 className="font-semibold text-gray-900">
                      Módulo 2: Herramientas Prácticas
                    </h4>
                    <p className="text-sm text-gray-600 mt-1">
                      Duración: 22 minutos • Nivel: Intermedio
                    </p>
                  </div>
                  <div className="p-4 border-l-4 border-orange-600 bg-orange-50 rounded">
                    <h4 className="font-semibold text-gray-900">
                      Módulo 3: Aplicaciones en Aula
                    </h4>
                    <p className="text-sm text-gray-600 mt-1">
                      Duración: 27 minutos • Nivel: Avanzado
                    </p>
                  </div>
                </div>
              </div>
            </Card>
          </div>

          <div className="space-y-4">
            <Card variant="elevated" title="📈 Estadísticas" padding="lg">
              <div className="space-y-3 text-sm">
                <div className="flex justify-between">
                  <span className="text-gray-600">Docentes Activos:</span>
                  <span className="font-semibold text-gray-900">156</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Módulos:</span>
                  <span className="font-semibold text-gray-900">12</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Microcontenidos:</span>
                  <span className="font-semibold text-gray-900">42</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Completación Avg:</span>
                  <span className="font-semibold text-green-600">89%</span>
                </div>
              </div>
            </Card>

            <Card
              variant="elevated"
              title="🎯 Siguiente Paso"
              padding="lg"
              footer={<Button fullWidth>Ir al Dashboard</Button>}
            >
              <p className="text-sm text-gray-600">
                Inicia sesión con tu cuenta MEP para acceder al dashboard
                completo y tu progreso personalizado.
              </p>
            </Card>
          </div>
        </div>

        {/* Info Section */}
        <Card variant="outlined" title="ℹ️ Información del Proyecto" padding="lg">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 text-sm text-gray-700">
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Versión</h4>
              <p>1.0.0 - Alpha</p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Estado</h4>
              <p>🟢 En desarrollo activo</p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Organización</h4>
              <p>Ministerio de Educación Pública (MEP) - Costa Rica</p>
            </div>
            <div>
              <h4 className="font-semibold text-gray-900 mb-2">Última actualización</h4>
              <p>28 de abril, 2026</p>
            </div>
          </div>
        </Card>
      </div>
    </MainLayout>
  );
}
