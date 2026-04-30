# Caja de Herramientas Docente - Plataforma Administrativa

[![GitHub](https://img.shields.io/badge/github-caja--herramientas-blue)](https://github.com/tu-usuario/caja-herramientas-admin)
[![License](https://img.shields.io/badge/license-MIT-green)](#license)
[![Node.js Version](https://img.shields.io/badge/node-%3E%3D18.0.0-green)](#requirements)

Plataforma administrativa para gestionar contenidos educativos sobre IA en Costa Rica, alineada con la Guía MEP 2026.

---

## 🎯 Características

- ✅ **Gestión de Contenidos**: Módulos, temas, recursos (infografías, videos, quizzes)
- ✅ **Control de Usuarios**: Roles y permisos granulares (Admin, Editor, Contributor, Viewer)
- ✅ **Autenticación Segura**: JWT + Sesiones + CSRF Protection
- ✅ **Rate Limiting**: Protección contra brute force y DDoS
- ✅ **Auditoría**: Registro de todas las acciones críticas
- ✅ **Validación**: Sanitización de inputs, validación de datos
- ✅ **Base de Datos**: Prisma + PostgreSQL
- ✅ **Interfaz Moderna**: Next.js + React + Tailwind CSS
- ✅ **Mobile-Ready**: Responsive design
- ✅ **Compliance**: RGPD, OWASP Top 10

---

## 📋 Requisitos

- Node.js >= 18.0.0
- npm >= 9.0.0
- PostgreSQL >= 13
- Git

---

## 🚀 Instalación Rápida

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/caja-herramientas-admin.git
cd caja-herramientas-admin
```

### 2. Instalar dependencias

```bash
npm install
```

### 3. Configurar variables de entorno

```bash
cp .env.example .env.local
# Editar .env.local con tus valores
```

### 4. Configurar base de datos

```bash
# Crear base de datos
createdb caja_herramientas

# Ejecutar migraciones
npm run db:migrate

# Cargar datos iniciales (opcional)
npm run db:seed
```

### 5. Ejecutar en desarrollo

```bash
npm run dev
```

Acceder a: `http://localhost:3000`

---

## 📁 Estructura del Proyecto

```
caja-herramientas-admin/
├── src/
│   ├── components/        # Componentes React reutilizables
│   ├── pages/             # Páginas Next.js
│   ├── api/               # Rutas API
│   ├── lib/               # Lógica de negocio
│   │   ├── auth/          # Autenticación
│   │   ├── security/      # Seguridad (CSRF, rate limit, sanitize)
│   │   └── database/      # Conexión BD
│   ├── types/             # Tipos TypeScript
│   ├── middleware/        # Middleware
│   ├── config/            # Configuración
│   └── styles/            # Estilos CSS
├── prisma/
│   └── schema.prisma      # Esquema de base de datos
├── .github/
│   ├── workflows/         # CI/CD
│   └── SECURITY.md        # Política de seguridad
├── tests/                 # Tests
├── docs/                  # Documentación
├── package.json
├── tsconfig.json
├── next.config.js
└── README.md
```

---

## 🔐 Seguridad

### Medidas Implementadas

- ✅ **Autenticación**: JWT + Refresh tokens
- ✅ **CSRF Protection**: Tokens únicos por sesión
- ✅ **Rate Limiting**: Límites por IP y endpoint
- ✅ **Sanitización**: DOMPurify + validación de inputs
- ✅ **HTTPS Obligatorio**: En producción
- ✅ **Headers de Seguridad**: Helmet + Custom headers
- ✅ **Auditoría**: Logging de acciones críticas
- ✅ **Encriptación**: Passwords hashed (bcrypt), datos encriptados

### Reportar Vulnerabilidades

Ver [.github/SECURITY.md](.github/SECURITY.md) para instrucciones completas.

Email: **seguridad@cajaherramientas.edu.cr**

---

## 🏗️ Arquitectura

### Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js 14 + React 18 + TypeScript |
| UI | Tailwind CSS + Lucide Icons |
| Backend | Next.js API Routes |
| Base de Datos | PostgreSQL + Prisma ORM |
| Autenticación | JWT + bcrypt |
| Validación | Zod / JSON Schema |
| Testing | Jest + React Testing Library |

### Flujo de Datos

```
Cliente (Browser)
    ↓
Next.js Frontend (TSX)
    ↓ (HTTP/HTTPS)
API Routes (/api/*)
    ↓ (Middleware: Auth, CSRF, RateLimit)
Business Logic (Services)
    ↓
Prisma ORM
    ↓
PostgreSQL
```

---

## 📖 Documentación

- [ARCHITECTURE.md](docs/ARCHITECTURE.md) - Arquitectura técnica
- [API.md](docs/API.md) - Documentación de endpoints
- [DATABASE.md](docs/DATABASE.md) - Esquema de base de datos
- [SECURITY.md](docs/SECURITY.md) - Guía de seguridad
- [DEPLOYMENT.md](docs/DEPLOYMENT.md) - Despliegue en producción
- [STYLE_GUIDE.md](docs/STYLE_GUIDE.md) - Guía de código

---

## 🧪 Testing

```bash
# Unit tests
npm run test

# Watch mode
npm run test:watch

# Coverage
npm run test:coverage

# Security tests
npm run test:security
```

---

## 📦 Build y Despliegue

### Compilar para producción

```bash
npm run build
```

### Iniciar servidor de producción

```bash
npm start
```

### Desplegar en Vercel

```bash
# Conectar repo a Vercel dashboard
# O usar CLI
npm install -g vercel
vercel
```

Ver [DEPLOYMENT.md](docs/DEPLOYMENT.md) para opciones detalladas.

---

## 🔧 Comandos Útiles

```bash
# Development
npm run dev                # Iniciar en modo desarrollo
npm run build             # Compilar para producción
npm start                 # Ejecutar servidor de producción

# Linting y Formato
npm run lint              # Ejecutar ESLint
npm run lint:fix          # Arreglar errores
npm run format            # Formatear código con Prettier
npm run format:check      # Verificar formato

# Database
npm run db:generate       # Generar Prisma Client
npm run db:migrate        # Ejecutar migraciones
npm run db:seed           # Cargar datos iniciales
npm run db:studio         # Abrir Prisma Studio

# Testing
npm run test              # Ejecutar tests
npm run test:watch        # Tests en watch mode
npm run test:coverage     # Cobertura de tests
npm run test:security     # Security audit

# Type Checking
npm run type-check        # Verificar tipos TypeScript
```

---

## 👥 Roles y Permisos

### Roles Disponibles

| Rol | Módulos | Temas | Recursos | Usuarios | Settings |
|-----|---------|-------|----------|----------|----------|
| **Admin** | ✅ Full | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| **Editor** | ✅ Full | ✅ Full | ✅ Full | ❌ | ❌ |
| **Contributor** | ❌ | ❌ | ✅ Full | ❌ | ❌ |
| **Viewer** | 🔍 Solo lectura | 🔍 Solo lectura | 🔍 Solo lectura | ❌ | ❌ |

---

## 📊 Base de Datos

### Entidades Principales

- **User**: Usuarios del sistema
- **Module**: Módulos educativos (ej: "Fundamentos de IA")
- **Topic**: Temas/Microtemas dentro de módulos
- **Resource**: Recursos (infografías, videos, documentos)
- **Quiz**: Cuestionarios de autoevaluación
- **AuditLog**: Registro de auditoría

Ver [ARCHITECTURE.md](docs/ARCHITECTURE.md) para diagrama completo.

---

## 🎨 Identidad Gráfica

- **Primario**: Azul MEP (#0066CC)
- **Secundario**: Verde educación (#00AA44)
- **Acento**: Naranja IA (#FF6B35)
- **Tipografía**: Inter (sans-serif)
- **Border Radius**: Mediano (0.5rem - 1rem)

Ver [GUIA_ESTILOS_VISUAL.md](GUIA_ESTILOS_VISUAL.md) para detalles completos.

---

## 🤝 Contribuir

1. Fork el repositorio
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

Ver [CONTRIBUTING.md](CONTRIBUTING.md) para guidelines.

---

## 📜 License

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para detalles.

---

## 📞 Contacto

- **Email**: contacto@cajaherramientas.edu.cr
- **Seguridad**: seguridad@cajaherramientas.edu.cr
- **GitHub Issues**: [Reportar un problema](https://github.com/tu-usuario/caja-herramientas-admin/issues)

---

## 🙏 Agradecimientos

Desarrollado para el Ministerio de Educación Pública (MEP) de Costa Rica, en alineación con la Guía Docente de IA 2026.

---

**Última actualización**: Abril 2026

