# 🏗️ LAYOUT PRINCIPAL - DOCUMENTACIÓN

**Creado**: Abril 28, 2026  
**Versión**: 1.0.0  
**Estado**: ✅ Listo para producción

---

## 📦 Componentes de Layout Creados

### 1. **Header** ✅
**Archivo**: `src/components/layout/Header.tsx`

Barra superior con:
- Botón de menú responsivo (visible en móvil)
- Contenido lado izquierdo (búsqueda, etc)
- Contenido lado derecho (notificaciones, perfil)
- Fixed position con z-index 20

**Props**:
```typescript
interface HeaderProps {
  left?: ReactNode;           // Contenido izquierda
  right?: ReactNode;          // Contenido derecha
  onMenuClick?: () => void;   // Callback del botón menú
  showMenuButton?: boolean;   // Mostrar botón menú
}
```

**Uso**:
```tsx
<Header
  left={<SearchBar />}
  right={<NotificationBell />}
  onMenuClick={() => setSidebarOpen(true)}
/>
```

---

### 2. **Sidebar** ✅
**Archivo**: `src/components/layout/Sidebar.tsx`

Navegación lateral con:
- Logo/branding
- Items de navegación con iconos
- Soporte para estado activo
- Footer personalizable
- Responsive (colapsable en móvil)
- Overlay en móvil

**Props**:
```typescript
interface SidebarProps {
  items: SidebarItemProps[];
  footer?: ReactNode;
  collapsed?: boolean;    // Si está abierto en móvil
  onClose?: () => void;   // Callback para cerrar
}

interface SidebarItemProps {
  icon: ReactNode;
  label: string;
  href: string;
  isActive?: boolean;
}
```

**Uso**:
```tsx
<Sidebar
  items={[
    { icon: '📊', label: 'Dashboard', href: '/dashboard', isActive: true },
    { icon: '📚', label: 'Módulos', href: '/modulos' },
  ]}
  footer={<UserMenu />}
  collapsed={sidebarOpen}
  onClose={() => setSidebarOpen(false)}
/>
```

---

### 3. **Footer** ✅
**Archivo**: `src/components/layout/Footer.tsx`

Pie de página con:
- 3 columnas: Acerca de, Enlaces rápidos, Legal
- Copyright
- Links de privacidad, términos, contacto
- Fondo oscuro (gray-900)
- Responsive

**Props**:
```typescript
interface FooterProps {
  children?: ReactNode;  // Contenido personalizado
  sticky?: boolean;      // Fijo al fondo
}
```

**Uso**:
```tsx
<Footer>
  {/* Contenido personalizado */}
</Footer>
```

---

### 4. **MainLayout** ✅
**Archivo**: `src/components/layout/MainLayout.tsx`

Layout principal que orquesta:
- Header
- Sidebar
- Main content
- Footer

**Props**:
```typescript
interface MainLayoutProps {
  children: ReactNode;
  sidebarItems?: SidebarItemProps[];
  headerLeft?: ReactNode;
  headerRight?: ReactNode;
  footerContent?: ReactNode;
  showFooter?: boolean;
  activeItem?: string;
  mainClassName?: string;
}
```

**Uso**:
```tsx
<MainLayout
  sidebarItems={navItems}
  activeItem="/dashboard"
  headerLeft={<SearchBar />}
  headerRight={<UserProfile />}
  showFooter={true}
>
  <YourPageContent />
</MainLayout>
```

---

## 📂 Estructura de Archivos

```
src/components/layout/
├── Header.tsx           ✅ (70 líneas)
├── Sidebar.tsx          ✅ (110 líneas)
├── Footer.tsx           ✅ (100 líneas)
├── MainLayout.tsx       ✅ (130 líneas)
└── index.ts             ✅ (Barrel export)

src/pages/
├── index.tsx            ✅ (Página inicio)
└── dashboard.tsx        ✅ (Página dashboard)
```

---

## 🎨 Características de Diseño

### Responsive Design
- ✅ Mobile: Sidebar colapsado, menú hamburguesa visible
- ✅ Tablet: Sidebar visible, layout ajustado
- ✅ Desktop: Layout completo con sidebar fijo

### Breakpoints
```
Mobile:   320px - 639px   (Sidebar oculto por defecto)
Tablet:   640px - 1023px  (Sidebar visible pequeño)
Desktop: 1024px+          (Sidebar fijo, ancho completo)
```

### Colores
- Header/Footer: Gris/Blanco
- Sidebar: Blanco con bordes
- Items activos: Azul MEP (#0066CC)
- Background: Gris claro (#F3F4F6)

### Espaciado
- Header height: 5rem (80px)
- Sidebar width: 16rem (256px)
- Padding main: 1.5rem en desktop, 1rem en móvil

---

## 🚀 Cómo Usar

### 1. Importar Layout

```typescript
import { MainLayout } from '@/components/layout';
```

### 2. Definir Items del Sidebar

```typescript
const sidebarItems = [
  { 
    icon: '📊', 
    label: 'Dashboard', 
    href: '/dashboard',
    isActive: true 
  },
  { 
    icon: '📚', 
    label: 'Módulos', 
    href: '/modulos' 
  },
  { 
    icon: '👥', 
    label: 'Usuarios', 
    href: '/usuarios' 
  },
];
```

### 3. Crear Header Content

```typescript
const headerLeft = (
  <div className="flex items-center gap-2">
    <Input 
      type="text" 
      placeholder="Buscar..." 
    />
  </div>
);

const headerRight = (
  <div className="flex items-center gap-4">
    <BellIcon />
    <UserProfile />
  </div>
);
```

### 4. Usar en Página

```typescript
export default function MiPagina() {
  return (
    <MainLayout
      sidebarItems={sidebarItems}
      activeItem="/dashboard"
      headerLeft={headerLeft}
      headerRight={headerRight}
    >
      <div>
        <h1>Contenido de mi página</h1>
        {/* Contenido aquí */}
      </div>
    </MainLayout>
  );
}
```

---

## 📄 Páginas de Demo

### 1. Página de Inicio
**URL**: `http://localhost:3000/`

- Hero section
- Features grid (3 características)
- Módulos destacados
- Estadísticas
- Call-to-action

### 2. Dashboard
**URL**: `http://localhost:3000/dashboard`

- Stats cards (4 métricas)
- Módulos recientes
- Actividad reciente
- Información y acciones rápidas
- Layout completo con sidebar

---

## 🔧 Customización

### Cambiar Colores

```typescript
// En Header.tsx, Sidebar.tsx, etc.
className={`
  bg-blue-600 hover:bg-blue-700  // Cambiar colores primarios
  text-white
`}
```

### Agregar Más Items al Sidebar

```typescript
const moreItems = [
  ...sidebarItems,
  { icon: '📊', label: 'Reportes', href: '/reportes' },
];
```

### Personalizar Footer

```typescript
<MainLayout
  footerContent={
    <div className="custom-footer">
      Tu contenido aquí
    </div>
  }
>
```

---

## ✅ Checklist de Características

- [x] Header responsivo con menú móvil
- [x] Sidebar con navegación
- [x] Sidebar colapsable en móvil
- [x] Items activos visibles
- [x] Footer con 3 secciones
- [x] MainLayout orquestador
- [x] Página de inicio demo
- [x] Página de dashboard demo
- [x] 100% TypeScript tipado
- [x] Responsive mobile-first
- [x] Accesibilidad ARIA
- [x] Integración con componentes comunes

---

## 📱 Responsive Behavior

### Móvil (< 640px)
```
┌─────────────────────┐
│ ☰  | Contenido    | 🔔
├─────────────────────┤
│                     │
│   Main Content      │
│   (Full Width)      │
│                     │
├─────────────────────┤
│      Footer         │
└─────────────────────┘

Sidebar: Overlay con Z-index
```

### Desktop (≥ 1024px)
```
┌──────────┬─────────────────────┐
│ ☰ Menu │ Buscar    | 🔔 👤   │
├──────────┼─────────────────────┤
│          │                     │
│ Sidebar  │   Main Content      │
│  Items   │                     │
│          │                     │
├──────────┼─────────────────────┤
│          │      Footer         │
└──────────┴─────────────────────┘

Sidebar: Fixed, siempre visible
```

---

## 🎯 Próximos Pasos

1. **Agregar Autenticación**
   - LoginForm en Header
   - Verificación de sesión
   - Redirect si no autenticado

2. **Integrar Notificaciones**
   - Dropdown de notificaciones
   - Badge con contador
   - Histórico

3. **Crear Páginas Adicionales**
   - Página de módulos
   - Página de usuarios
   - Página de configuración

4. **Mejorar Interactividad**
   - Transiciones de sidebar
   - Dark mode
   - Personalización de temas

---

## 💾 Instalación y Ejecución

```bash
# 1. Instalar dependencias
npm install

# 2. Ejecutar en desarrollo
npm run dev

# 3. Acceder a
# http://localhost:3000           (Inicio)
# http://localhost:3000/dashboard (Dashboard)
# http://localhost:3000/components (Componentes)
```

---

## 🔍 Estructura de Carpetas Final

```
src/
├── components/
│   ├── common/           (10 componentes base)
│   └── layout/           (4 componentes layout) ✅
│
└── pages/
    ├── index.tsx         (Página inicio) ✅
    ├── dashboard.tsx     (Dashboard) ✅
    └── components.tsx    (Demo componentes)
```

---

**Layout Principal - Caja de Herramientas Docente en IA**  
**MEP 2026 - Costa Rica**  
**Abril 28, 2026**

