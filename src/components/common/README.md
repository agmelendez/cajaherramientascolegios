# 📦 COMPONENTES REACT - GUÍA DE USO

**Creado**: Abril 28, 2026  
**Versión**: 1.0.0  
**Estado**: ✅ Listo para producción

---

## 🎯 Resumen

Se han creado **10 componentes React reutilizables** con TypeScript, siguiendo la identidad gráfica de la Caja de Herramientas y mejores prácticas de accesibilidad.

### ✅ Componentes Creados

| Componente | Uso | Archivo |
|-----------|-----|---------|
| **Button** | Botones de acción primarios, secundarios, éxito, peligro | `Button.tsx` |
| **Input** | Campos de texto con label, error, helper text | `Input.tsx` |
| **Card** | Contenedores de contenido con variantes | `Card.tsx` |
| **Alert** | Mensajes de estado (éxito, error, warning, info) | `Alert.tsx` |
| **Badge** | Etiquetas y estados | `Badge.tsx` |
| **Tabs** | Navegación entre pestañas | `Tabs.tsx` |
| **Modal** | Diálogos y ventanas modales | `Modal.tsx` |
| **Pagination** | Navegación entre páginas | `Pagination.tsx` |
| **Skeleton** | Placeholder de carga | `Skeleton.tsx` |
| **Loader** | Indicadores de carga | `Loader.tsx` |

---

## 📂 Estructura de Archivos

```
src/components/common/
├── Button.tsx           ✅
├── Input.tsx            ✅
├── Card.tsx             ✅
├── Alert.tsx            ✅
├── Badge.tsx            ✅
├── Tabs.tsx             ✅
├── Modal.tsx            ✅
├── Pagination.tsx       ✅
├── Skeleton.tsx         ✅
├── Loader.tsx           ✅
├── index.ts             ✅ (Barrel export)
└── README.md            ← Este archivo

src/pages/
└── components.tsx       ✅ (Página de demostración)
```

---

## 🚀 Cómo Usar

### 1. Importar Componentes

```typescript
// Importar múltiples componentes
import { Button, Input, Card, Alert } from '@/components/common';

// O importar uno específico
import Button from '@/components/common/Button';
```

### 2. Button

```typescript
// Básico
<Button>Guardar</Button>

// Con variantes
<Button variant="primary">Primario</Button>
<Button variant="secondary">Secundario</Button>
<Button variant="success">Éxito</Button>
<Button variant="danger">Peligro</Button>

// Con tamaños
<Button size="sm">Pequeño</Button>
<Button size="md">Mediano</Button>
<Button size="lg">Grande</Button>

// Con estado de carga
<Button isLoading={loading}>Guardando...</Button>

// Con icono
<Button icon={<SaveIcon />}>Guardar</Button>
<Button icon={<SaveIcon />} iconPosition="right">Guardar</Button>

// Ancho completo
<Button fullWidth>Enviar</Button>

// Deshabilitado
<Button disabled>Deshabilitado</Button>
```

### 3. Input

```typescript
// Básico
<Input placeholder="Escribe algo..." />

// Con label
<Input label="Nombre" placeholder="Juan Pérez" />

// Con validación
<Input 
  label="Email" 
  type="email"
  error="Email inválido" 
/>

// Con helper text
<Input 
  label="Contraseña"
  type="password"
  helper="Mínimo 8 caracteres"
  required
/>

// Con icono
<Input 
  label="Búsqueda"
  icon={<SearchIcon />}
  placeholder="Buscar..."
/>
```

### 4. Card

```typescript
// Básico
<Card>Contenido</Card>

// Con título
<Card title="Mi Tarjeta">
  Contenido aquí
</Card>

// Con variantes
<Card variant="default">Default</Card>
<Card variant="elevated">Elevada</Card>
<Card variant="outlined">Con borde</Card>

// Con padding
<Card padding="sm">Pequeño</Card>
<Card padding="md">Mediano</Card>
<Card padding="lg">Grande</Card>

// Con footer
<Card 
  title="Crear módulo"
  footer={<Button>Guardar</Button>}
>
  Formulario aquí
</Card>

// Con icono en header
<Card 
  title="Estadísticas"
  icon={<ChartIcon />}
>
  Contenido
</Card>
```

### 5. Alert

```typescript
// Tipos
<Alert type="success" message="¡Guardado!" />
<Alert type="error" message="Error al guardar" />
<Alert type="warning" message="Advertencia" />
<Alert type="info" message="Información" />

// Con título
<Alert 
  type="error"
  title="Error"
  message="Algo salió mal"
/>

// Cerrable
<Alert 
  message="Mensaje"
  dismissible
  onClose={() => console.log('closed')}
/>

// Con icono personalizado
<Alert 
  type="success"
  message="Completado"
  icon={<CheckIcon />}
/>
```

### 6. Badge

```typescript
// Variantes
<Badge>Primario</Badge>
<Badge variant="secondary">Secundario</Badge>
<Badge variant="success">Éxito</Badge>
<Badge variant="warning">Advertencia</Badge>
<Badge variant="error">Error</Badge>
<Badge variant="info">Info</Badge>

// Tamaños
<Badge size="sm">Pequeño</Badge>
<Badge size="md">Mediano</Badge>
<Badge size="lg">Grande</Badge>

// Con icono
<Badge icon={<CheckIcon />}>Completado</Badge>

// Removible
<Badge 
  removable 
  onRemove={() => console.log('removed')}
>
  Removible
</Badge>
```

### 7. Tabs

```typescript
const tabs = [
  { 
    id: 'modulos', 
    label: 'Módulos', 
    content: <ModulesList /> 
  },
  { 
    id: 'usuarios', 
    label: 'Usuarios', 
    content: <UsersList /> 
  },
];

<Tabs 
  tabs={tabs}
  defaultTab="modulos"
  onChange={(id) => console.log('Changed to:', id)}
/>

// Con iconos
const tabsWithIcons = [
  { 
    id: 'home', 
    label: 'Inicio', 
    icon: <HomeIcon />,
    content: <Home /> 
  },
];
```

### 8. Modal

```typescript
const [isOpen, setIsOpen] = useState(false);

<>
  <Button onClick={() => setIsOpen(true)}>Abrir</Button>
  
  <Modal
    isOpen={isOpen}
    title="Confirmar"
    onClose={() => setIsOpen(false)}
    closable={true}
    size="md"
    actions={
      <div className="flex gap-2">
        <Button variant="secondary" onClick={() => setIsOpen(false)}>
          Cancelar
        </Button>
        <Button onClick={() => setIsOpen(false)}>
          Confirmar
        </Button>
      </div>
    }
  >
    ¿Estás seguro?
  </Modal>
</>
```

### 9. Pagination

```typescript
const [page, setPage] = useState(1);

<Pagination
  currentPage={page}
  totalPages={10}
  onChange={setPage}
  siblingCount={1}
/>
```

### 10. Skeleton & Loader

```typescript
// Skeleton - Para estados de carga
<Skeleton type="text" lines={3} />
<Skeleton type="circle" height="48px" width="48px" />
<Skeleton type="rect" height="200px" />
<Skeleton type="card" />

// Loader - Indicador de carga
<Loader message="Cargando..." />
<Loader type="dots" message="Procesando..." />
<Loader type="pulse" message="Sincronizando..." />
<Loader fullscreen message="Inicializando app..." />
```

---

## 🎨 Colores y Estilos

Los componentes usan automáticamente los colores de la Caja de Herramientas:

- **Azul MEP**: `#0066CC` - Acciones principales
- **Verde**: `#00AA44` - Éxito y confirmación
- **Naranja**: `#FF6B35` - Acentos e IA
- **Rojo**: `#EF4444` - Errores y peligro
- **Amarillo**: `#FBBF24` - Advertencias

---

## 🔒 Accesibilidad

Todos los componentes incluyen:

- ✅ Atributos ARIA apropiados
- ✅ Navegación por teclado
- ✅ Contraste de colores accesible
- ✅ Iconos con labels descriptivos
- ✅ Estados disabled y error claros

---

## 📱 Responsive

Todos los componentes son **100% responsive**:

- ✅ Mobile-first design
- ✅ Breakpoints: 320px, 640px, 768px, 1024px, 1280px, 1536px
- ✅ Ajustes automáticos en tablets y desktop

---

## 🧪 Testing

```typescript
// Ejemplo con React Testing Library
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import Button from '@/components/common/Button';

test('Button renders and is clickable', () => {
  const handleClick = jest.fn();
  render(<Button onClick={handleClick}>Click</Button>);
  
  const button = screen.getByRole('button', { name: /click/i });
  userEvent.click(button);
  
  expect(handleClick).toHaveBeenCalled();
});
```

---

## 📄 Página de Demostración

Accede a `http://localhost:3000/components` para ver todos los componentes en acción.

---

## 🛠️ Customización

Todos los componentes aceptan `className` personalizado:

```typescript
<Button className="custom-class">
  Personalizado
</Button>

// Tailwind CSS sobrescribe estilos
<Button className="bg-purple-600 hover:bg-purple-700">
  Púrpura
</Button>
```

---

## 📦 Exports desde index.ts

```typescript
// Importar todo en un objeto
import * as Components from '@/components/common';

<Components.Button>Click</Components.Button>
```

---

## 🚀 Próximos Pasos

1. **Crear componentes de layout**
   - Header
   - Sidebar
   - Footer
   - Layout principal

2. **Crear componentes de dominio**
   - ModuleCard (módulos)
   - TopicForm (formulario de temas)
   - QuizComponent (quizzes)
   - ContentTree (árbol de contenidos)

3. **Páginas de ejemplo**
   - Dashboard
   - Módulos
   - Usuarios
   - Configuración

---

## 📞 Soporte

Si encuentras problemas o tienes sugerencias de mejora, crea un issue en GitHub o contacta al equipo de desarrollo.

---

**Caja de Herramientas Docente en IA - MEP 2026**

