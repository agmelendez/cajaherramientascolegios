# IDENTIDAD GRÁFICA Y GUÍA DE ESTILOS

## 1. Paleta de Colores

```css
/* Primarios - Basados en Guía MEP 2026 */
--color-primary: #0066CC;      /* Azul MEP */
--color-primary-dark: #0052A3;
--color-primary-light: #E6F2FF;

--color-secondary: #00AA44;    /* Verde educación */
--color-secondary-dark: #007A2E;
--color-secondary-light: #E6F9F0;

--color-accent: #FF6B35;       /* Naranja IA */
--color-accent-dark: #E5571B;
--color-accent-light: #FFE6D9;

/* Neutros */
--color-neutral-50: #F9FAFB;
--color-neutral-100: #F3F4F6;
--color-neutral-200: #E5E7EB;
--color-neutral-300: #D1D5DB;
--color-neutral-400: #9CA3AF;
--color-neutral-500: #6B7280;
--color-neutral-600: #4B5563;
--color-neutral-700: #374151;
--color-neutral-800: #1F2937;
--color-neutral-900: #111827;

/* Estados */
--color-success: #10B981;
--color-warning: #FBBF24;
--color-error: #EF4444;
--color-info: #3B82F6;

/* Backgrounds */
--bg-primary: #FFFFFF;
--bg-secondary: #F9FAFB;
--bg-tertiary: #F3F4F6;
```

---

## 2. Tipografía

```css
/* Font Family */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-mono: 'Fira Code', 'Courier New', monospace;

/* Sizes */
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */

/* Line Heights */
--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.625;

/* Font Weights */
--font-regular: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

/* Letter Spacing */
--tracking-tight: -0.02em;
--tracking-normal: 0;
--tracking-wide: 0.02em;
```

---

## 3. Espaciado

```css
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
```

---

## 4. Border Radius

```css
--radius-none: 0;
--radius-sm: 0.25rem;   /* 4px */
--radius-md: 0.5rem;    /* 8px */
--radius-lg: 0.75rem;   /* 12px */
--radius-xl: 1rem;      /* 16px */
--radius-2xl: 1.5rem;   /* 24px */
--radius-full: 9999px;
```

---

## 5. Sombras

```css
--shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
--shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
--shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
--shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1);
--shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
```

---

## 6. Componentes Base

### Botón Primario

```tsx
// Button.tsx
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children,
  isLoading,
  ...props
}) => {
  const baseStyles = `
    font-medium rounded-lg transition-all duration-200
    focus:outline-none focus:ring-2 focus:ring-offset-2
    disabled:opacity-50 disabled:cursor-not-allowed
  `;

  const variants = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
    secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200 focus:ring-gray-500',
    outline: 'border-2 border-blue-600 text-blue-600 hover:bg-blue-50 focus:ring-blue-500',
    ghost: 'text-blue-600 hover:bg-blue-50 focus:ring-blue-500',
  };

  const sizes = {
    sm: 'px-3 py-2 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg',
  };

  return (
    <button
      className={`${baseStyles} ${variants[variant]} ${sizes[size]}`}
      disabled={isLoading || props.disabled}
      {...props}
    >
      {isLoading ? <Spinner /> : children}
    </button>
  );
};
```

### Input

```tsx
// Input.tsx
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helper?: string;
}

export const Input: React.FC<InputProps> = ({
  label,
  error,
  helper,
  ...props
}) => {
  return (
    <div className="flex flex-col gap-1">
      {label && (
        <label className="text-sm font-medium text-gray-700">{label}</label>
      )}
      <input
        className={`
          px-4 py-2 border rounded-lg transition-all
          focus:outline-none focus:ring-2 focus:ring-blue-500
          ${error ? 'border-red-500' : 'border-gray-300'}
          ${error ? 'focus:ring-red-500' : ''}
        `}
        {...props}
      />
      {error && <p className="text-sm text-red-600">{error}</p>}
      {helper && <p className="text-sm text-gray-500">{helper}</p>}
    </div>
  );
};
```

### Card

```tsx
// Card.tsx
export const Card: React.FC<{ children: React.ReactNode; className?: string }> = ({
  children,
  className = '',
}) => {
  return (
    <div
      className={`
        bg-white rounded-lg shadow-md p-6
        border border-gray-100
        ${className}
      `}
    >
      {children}
    </div>
  );
};
```

---

## 7. Layouts y Grillas

### Sidebar Layout

```tsx
// Layout.tsx
export const DashboardLayout: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  return (
    <div className="flex h-screen bg-gray-50">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-gray-200 overflow-y-auto">
        <Sidebar />
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-y-auto">
        <Header />
        <div className="p-8">
          {children}
        </div>
      </main>
    </div>
  );
};
```

---

## 8. Estructura de Página Dashboard

```
┌─────────────────────────────────────────────────┐
│         HEADER (Logo, Nav, User Menu)           │
├─────────────────────────────────────────────────┤
│   │                                              │
│   │                                              │
│ S │         MAIN CONTENT AREA                    │
│ I │                                              │
│ D │                                              │
│ E │                                              │
│ B │                                              │
│ A │                                              │
│ R │                                              │
│   │                                              │
│   │                                              │
└─────────────────────────────────────────────────┘
```

---

## 9. Iconografía

Los iconos vienen de:
- **Heroicons** (UI estándar)
- **Lucide Icons** (alternativa moderna)

```tsx
// Uso
import { ChevronDown, Menu, X, Plus, Edit2, Trash2 } from 'lucide-react';

<button>
  <Plus size={20} />
  Nuevo Módulo
</button>
```

---

## 10. Componentes Específicos del Admin

### Module Card

```tsx
interface ModuleCardProps {
  title: string;
  description: string;
  topicsCount: number;
  published: boolean;
  onEdit: () => void;
  onDelete: () => void;
}

export const ModuleCard: React.FC<ModuleCardProps> = ({
  title,
  description,
  topicsCount,
  published,
  onEdit,
  onDelete,
}) => {
  return (
    <Card>
      <div className="flex justify-between items-start">
        <div>
          <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
          <p className="text-sm text-gray-600 mt-1">{description}</p>
        </div>
        <span
          className={`
            px-2 py-1 rounded-full text-xs font-medium
            ${published ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}
          `}
        >
          {published ? 'Publicado' : 'Borrador'}
        </span>
      </div>

      <div className="mt-4 pt-4 border-t border-gray-200 flex justify-between items-center">
        <span className="text-xs text-gray-500">{topicsCount} temas</span>
        <div className="flex gap-2">
          <Button size="sm" variant="outline" onClick={onEdit}>
            Editar
          </Button>
          <Button size="sm" variant="ghost" onClick={onDelete}>
            Eliminar
          </Button>
        </div>
      </div>
    </Card>
  );
};
```

### Content Tree

```tsx
interface TreeNode {
  id: string;
  title: string;
  type: 'module' | 'topic' | 'resource';
  children?: TreeNode[];
}

export const ContentTree: React.FC<{ nodes: TreeNode[] }> = ({ nodes }) => {
  return (
    <div className="space-y-2">
      {nodes.map((node) => (
        <TreeNode key={node.id} node={node} />
      ))}
    </div>
  );
};

const TreeNode: React.FC<{ node: TreeNode }> = ({ node }) => {
  const [expanded, setExpanded] = React.useState(true);

  return (
    <div className="border-l-2 border-gray-200">
      <div className="flex items-center gap-2 px-4 py-2 hover:bg-gray-50">
        {node.children && (
          <button onClick={() => setExpanded(!expanded)}>
            <ChevronDown
              size={16}
              className={`transform ${expanded ? '' : '-rotate-90'}`}
            />
          </button>
        )}
        <span className="text-sm font-medium text-gray-900">{node.title}</span>
      </div>
      {expanded && node.children && (
        <div className="ml-4">
          {node.children.map((child) => (
            <TreeNode key={child.id} node={child} />
          ))}
        </div>
      )}
    </div>
  );
};
```

---

## 11. Estados y Animaciones

```css
/* Transiciones suaves */
.transition-smooth {
  transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1);
}

/* Loading spinner */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}

/* Fade in */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.animate-fadeIn {
  animation: fadeIn 300ms ease-in;
}
```

---

## 12. Responsive Design

```css
/* Breakpoints */
--bp-mobile: 320px;
--bp-sm: 640px;
--bp-md: 768px;
--bp-lg: 1024px;
--bp-xl: 1280px;
--bp-2xl: 1536px;
```

