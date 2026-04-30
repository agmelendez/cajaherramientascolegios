import React from 'react';
import { Button, Input, Card, Alert, Badge, Tabs, Modal, Pagination } from '@/components/common';

/**
 * Página de demostración de componentes
 * Muestra ejemplos de uso de todos los componentes disponibles
 *
 * Accede en: http://localhost:3000/components
 */
export default function ComponentsDemo() {
  const [modal, setModal] = React.useState(false);
  const [page, setPage] = React.useState(1);
  const [inputValue, setInputValue] = React.useState('');
  const [alerts, setAlerts] = React.useState<string[]>(['success', 'error']);

  const tabs = [
    {
      id: 'modulos',
      label: 'Módulos',
      content: <p>Contenido de módulos aquí</p>,
    },
    {
      id: 'usuarios',
      label: 'Usuarios',
      content: <p>Contenido de usuarios aquí</p>,
    },
  ];

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4">
      <div className="max-w-6xl mx-auto space-y-12">
        {/* Header */}
        <div className="mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Componentes de Diseño
          </h1>
          <p className="text-gray-600">
            Demostración de los componentes reutilizables de la Caja de
            Herramientas
          </p>
        </div>

        {/* Buttons */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Botones</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <Button>Primario</Button>
            <Button variant="secondary">Secundario</Button>
            <Button variant="success">Éxito</Button>
            <Button variant="danger">Peligro</Button>
            <Button size="sm">Pequeño</Button>
            <Button size="md">Mediano</Button>
            <Button size="lg">Grande</Button>
            <Button disabled>Deshabilitado</Button>
          </div>
        </section>

        {/* Inputs */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Inputs</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Input
              label="Nombre completo"
              placeholder="Juan Pérez"
              required
            />
            <Input
              label="Email"
              type="email"
              placeholder="juan@ejemplo.com"
              helper="Usamos esto para notificaciones"
            />
            <Input
              label="Contraseña"
              type="password"
              placeholder="••••••••"
              required
            />
            <Input
              label="Campo con error"
              error="Este campo es requerido"
              placeholder="Intenta escribir algo"
            />
          </div>
        </section>

        {/* Cards */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Tarjetas</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card title="Tarjeta simple">
              <p>Contenido de ejemplo en una tarjeta básica</p>
            </Card>

            <Card variant="elevated" title="Tarjeta elevada">
              <p>Esta tarjeta tiene una sombra y efecto hover</p>
            </Card>

            <Card
              title="Tarjeta con footer"
              footer={<Button size="sm">Guardar</Button>}
            >
              <p>Esta tarjeta tiene un footer con botón</p>
            </Card>
          </div>
        </section>

        {/* Alerts */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Alertas</h2>
          <div className="space-y-3">
            {alerts.includes('success') && (
              <Alert
                type="success"
                title="¡Éxito!"
                message="La operación se completó correctamente"
                dismissible
                onClose={() => setAlerts(alerts.filter((a) => a !== 'success'))}
              />
            )}
            {alerts.includes('error') && (
              <Alert
                type="error"
                title="Error"
                message="Algo salió mal. Por favor intenta de nuevo"
                dismissible
                onClose={() => setAlerts(alerts.filter((a) => a !== 'error'))}
              />
            )}
            <Alert
              type="warning"
              message="Esto es un mensaje de advertencia"
            />
            <Alert
              type="info"
              title="Información"
              message="Aquí va información adicional"
            />
          </div>
        </section>

        {/* Badges */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Insignias</h2>
          <div className="flex flex-wrap gap-3">
            <Badge>Primario</Badge>
            <Badge variant="secondary">Secundario</Badge>
            <Badge variant="success">Completado</Badge>
            <Badge variant="warning">Pendiente</Badge>
            <Badge variant="error">Error</Badge>
            <Badge size="sm">Pequeño</Badge>
            <Badge size="lg">Grande</Badge>
            <Badge removable>Removible</Badge>
          </div>
        </section>

        {/* Tabs */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Pestañas</h2>
          <Tabs tabs={tabs} onChange={(id) => console.log('Tab:', id)} />
        </section>

        {/* Modal */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Modal</h2>
          <Button onClick={() => setModal(true)}>Abrir Modal</Button>
          <Modal
            isOpen={modal}
            title="Ejemplo de Modal"
            onClose={() => setModal(false)}
            actions={
              <div className="flex gap-2">
                <Button
                  variant="secondary"
                  size="sm"
                  onClick={() => setModal(false)}
                >
                  Cancelar
                </Button>
                <Button size="sm" onClick={() => setModal(false)}>
                  Confirmar
                </Button>
              </div>
            }
          >
            <p>
              Este es un ejemplo de modal. Puedes hacer clic afuera o en
              cancelar para cerrarlo.
            </p>
          </Modal>
        </section>

        {/* Pagination */}
        <section>
          <h2 className="text-2xl font-bold mb-6">Paginación</h2>
          <div className="flex justify-center">
            <Pagination
              currentPage={page}
              totalPages={10}
              onChange={setPage}
            />
          </div>
        </section>

        {/* Footer */}
        <section className="border-t border-gray-200 pt-12 mt-12">
          <p className="text-gray-600 text-center">
            Estos componentes están listos para usarse en toda la plataforma.
            Importalos desde <code>@/components/common</code>
          </p>
        </section>
      </div>
    </div>
  );
}
