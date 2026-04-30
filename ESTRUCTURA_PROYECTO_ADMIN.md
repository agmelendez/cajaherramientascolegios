# ESTRUCTURA DEL PROYECTO: Caja de Herramientas - Admin Platform

```
caja-herramientas-admin/
│
├── .github/
│   ├── workflows/
│   │   └── ci-cd.yml                    # CI/CD pipeline
│   └── SECURITY.md                      # Política de seguridad
│
├── .env.example                         # Variables de entorno de ejemplo
├── .env.local                          # Variables locales (NO COMMITEAR)
├── .gitignore                          # Archivos a ignorar
├── .eslintrc.json                      # Configuración ESLint
├── tsconfig.json                       # Configuración TypeScript
├── next.config.js                      # Configuración Next.js
│
├── public/
│   ├── images/
│   │   ├── logo.svg
│   │   ├── favicon.ico
│   │   └── placeholders/
│   ├── icons/
│   │   ├── module-*.svg
│   │   └── action-*.svg
│   └── fonts/
│       └── inter.woff2
│
├── src/
│   │
│   ├── config/
│   │   ├── security.ts                 # Configuración de seguridad
│   │   ├── auth.ts                     # Configuración autenticación
│   │   └── database.ts                 # Configuración BD
│   │
│   ├── lib/
│   │   ├── auth/
│   │   │   ├── session.ts              # Gestión sesiones
│   │   │   ├── jwt.ts                  # JWT tokens
│   │   │   └── permissions.ts          # Control de permisos
│   │   │
│   │   ├── security/
│   │   │   ├── csrf.ts                 # CSRF protection
│   │   │   ├── rateLimit.ts            # Rate limiting
│   │   │   ├── sanitize.ts             # Input sanitization
│   │   │   └── helmet.ts               # Security headers
│   │   │
│   │   ├── database/
│   │   │   ├── client.ts               # Cliente Prisma
│   │   │   ├── migrations.ts           # Gestión migraciones
│   │   │   └── seed.ts                 # Datos iniciales
│   │   │
│   │   └── utils/
│   │       ├── validators.ts           # Validación de datos
│   │       ├── logger.ts               # Logging
│   │       └── helpers.ts              # Funciones auxiliares
│   │
│   ├── types/
│   │   ├── index.ts                    # Tipos globales
│   │   ├── auth.ts                     # Tipos autenticación
│   │   ├── content.ts                  # Tipos contenido
│   │   └── api.ts                      # Tipos API
│   │
│   ├── middleware/
│   │   ├── auth.ts                     # Middleware autenticación
│   │   ├── roleCheck.ts                # Middleware rol
│   │   ├── rateLimitMiddleware.ts       # Rate limiting middleware
│   │   └── securityHeaders.ts          # Headers de seguridad
│   │
│   ├── components/
│   │   ├── common/
│   │   │   ├── Layout.tsx              # Layout principal
│   │   │   ├── Header.tsx              # Encabezado
│   │   │   ├── Sidebar.tsx             # Barra lateral
│   │   │   ├── Footer.tsx              # Pie de página
│   │   │   └── Button.tsx              # Botón reutilizable
│   │   │
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx           # Formulario login
│   │   │   ├── SignupForm.tsx          # Formulario registro
│   │   │   └── ProtectedRoute.tsx      # Ruta protegida
│   │   │
│   │   ├── dashboard/
│   │   │   ├── ModuleCard.tsx          # Tarjeta módulo
│   │   │   ├── ContentTree.tsx         # Árbol de contenidos
│   │   │   └── StatsPanel.tsx          # Panel estadísticas
│   │   │
│   │   ├── content/
│   │   │   ├── ContentEditor.tsx       # Editor contenido
│   │   │   ├── MediaUploader.tsx       # Cargador archivos
│   │   │   └── PreviewPanel.tsx        # Panel previsualización
│   │   │
│   │   └── forms/
│   │       ├── ModuleForm.tsx          # Formulario módulo
│   │       ├── TopicForm.tsx           # Formulario tema
│   │       └── ResourceForm.tsx        # Formulario recurso
│   │
│   ├── pages/
│   │   ├── _app.tsx                    # App wrapper
│   │   ├── _document.tsx               # Document wrapper
│   │   ├── index.tsx                   # Home
│   │   │
│   │   ├── auth/
│   │   │   ├── login.tsx               # Login
│   │   │   ├── signup.tsx              # Signup
│   │   │   └── logout.tsx              # Logout
│   │   │
│   │   ├── dashboard/
│   │   │   ├── index.tsx               # Dashboard principal
│   │   │   ├── modules/
│   │   │   │   ├── index.tsx           # Lista módulos
│   │   │   │   ├── [moduleId].tsx      # Módulo detalle
│   │   │   │   ├── new.tsx             # Crear módulo
│   │   │   │   └── [moduleId]/edit.tsx # Editar módulo
│   │   │   │
│   │   │   ├── topics/
│   │   │   │   ├── index.tsx           # Lista temas
│   │   │   │   ├── [topicId].tsx       # Tema detalle
│   │   │   │   ├── new.tsx             # Crear tema
│   │   │   │   └── [topicId]/edit.tsx  # Editar tema
│   │   │   │
│   │   │   ├── resources/
│   │   │   │   ├── index.tsx           # Lista recursos
│   │   │   │   ├── [resourceId].tsx    # Recurso detalle
│   │   │   │   ├── new.tsx             # Crear recurso
│   │   │   │   └── [resourceId]/edit.tsx # Editar recurso
│   │   │   │
│   │   │   ├── users/
│   │   │   │   ├── index.tsx           # Gestión usuarios
│   │   │   │   ├── [userId].tsx        # Detalle usuario
│   │   │   │   └── permissions.tsx     # Gestión permisos
│   │   │   │
│   │   │   └── settings.tsx            # Configuración
│   │   │
│   │   └── api/
│   │       ├── auth/
│   │       │   ├── login.ts            # API login
│   │       │   ├── signup.ts           # API signup
│   │       │   ├── logout.ts           # API logout
│   │       │   └── refresh.ts          # API refresh token
│   │       │
│   │       ├── modules/
│   │       │   ├── index.ts            # API GET/POST módulos
│   │       │   ├── [id].ts             # API GET/PUT/DELETE módulo
│   │       │   └── [id]/tree.ts        # API árbol módulo
│   │       │
│   │       ├── topics/
│   │       │   ├── index.ts            # API GET/POST temas
│   │       │   ├── [id].ts             # API GET/PUT/DELETE tema
│   │       │   └── [id]/resources.ts   # API recursos tema
│   │       │
│   │       ├── resources/
│   │       │   ├── index.ts            # API GET/POST recursos
│   │       │   ├── [id].ts             # API GET/PUT/DELETE
│   │       │   └── upload.ts           # API carga archivos
│   │       │
│   │       ├── users/
│   │       │   ├── index.ts            # API usuarios
│   │       │   ├── [id].ts             # API usuario detalle
│   │       │   └── [id]/permissions.ts # API permisos usuario
│   │       │
│   │       └── health.ts               # Health check
│   │
│   ├── styles/
│   │   ├── globals.css                 # Estilos globales
│   │   ├── variables.css               # Variables CSS
│   │   ├── components.css              # Estilos componentes
│   │   └── layout.css                  # Estilos layout
│   │
│   └── hooks/
│       ├── useAuth.ts                  # Hook autenticación
│       ├── useModules.ts               # Hook módulos
│       ├── useTopics.ts                # Hook temas
│       ├── useResources.ts             # Hook recursos
│       └── useFetch.ts                 # Hook fetch genérico
│
├── prisma/
│   ├── schema.prisma                   # Esquema BD
│   └── migrations/                     # Migraciones
│
├── tests/
│   ├── unit/
│   │   ├── auth.test.ts
│   │   ├── security.test.ts
│   │   └── validators.test.ts
│   │
│   └── integration/
│       ├── api.test.ts
│       └── auth.test.ts
│
├── docs/
│   ├── ARCHITECTURE.md                 # Arquitectura proyecto
│   ├── API.md                          # Documentación API
│   ├── SECURITY.md                     # Guía seguridad
│   ├── DEPLOYMENT.md                   # Guía despliegue
│   ├── DATABASE.md                     # Esquema BD
│   └── STYLE_GUIDE.md                  # Guía de estilos
│
├── package.json
├── package-lock.json
├── README.md
└── LICENSE
```

---

## ESTRUCTURA DE DATOS (Prisma Schema)

Archivo: `prisma/schema.prisma`

```prisma
// Configuración general
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// ==================== USUARIOS ====================

model User {
  id            String     @id @default(cuid())
  email         String     @unique
  password      String     // Hashed
  name          String
  role          UserRole   @default(VIEWER)
  
  // Relaciones
  modules       Module[]   @relation("UserModules")
  topics        Topic[]    @relation("UserTopics")
  resources     Resource[] @relation("UserResources")
  sessions      Session[]
  auditLogs     AuditLog[]
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
  deletedAt     DateTime?
  
  @@index([email])
  @@index([role])
}

model Session {
  id            String     @id @default(cuid())
  userId        String
  user          User       @relation(fields: [userId], references: [id], onDelete: Cascade)
  
  token         String     @unique
  refreshToken  String     @unique
  expiresAt     DateTime
  ipAddress     String?
  userAgent     String?
  revokedAt     DateTime?
  
  createdAt     DateTime   @default(now())
  
  @@index([userId])
  @@index([token])
}

// ==================== MÓDULOS ====================

model Module {
  id            String     @id @default(cuid())
  title         String
  description   String?    @db.Text
  slug          String     @unique
  order         Int        @default(0)
  published     Boolean    @default(false)
  
  // Propietario y permisos
  createdById   String
  createdBy     User       @relation("UserModules", fields: [createdById], references: [id])
  
  // Relaciones
  topics        Topic[]    @relation("ModuleTopics")
  
  metadata      ModuleMetadata?
  seo           SEOData?
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
  deletedAt     DateTime?
  
  @@index([createdById])
  @@index([published])
  @@index([slug])
}

model ModuleMetadata {
  id            String     @id @default(cuid())
  moduleId      String     @unique
  module        Module     @relation(fields: [moduleId], references: [id], onDelete: Cascade)
  
  icon          String?
  color         String?
  estimatedTime Int?       // en minutos
  level         String?    // beginner, intermediate, advanced
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
}

// ==================== TEMAS / MICROTEMAS ====================

model Topic {
  id            String     @id @default(cuid())
  title         String
  description   String?    @db.Text
  slug          String     @unique
  
  moduleId      String
  module        Module     @relation("ModuleTopics", fields: [moduleId], references: [id], onDelete: Cascade)
  
  createdById   String
  createdBy     User       @relation("UserTopics", fields: [createdById], references: [id])
  
  order         Int        @default(0)
  published     Boolean    @default(false)
  estimatedTime Int?       // en minutos
  
  // Relaciones
  resources     Resource[] @relation("TopicResources")
  
  seo           SEOData?
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
  deletedAt     DateTime?
  
  @@unique([moduleId, slug])
  @@index([moduleId])
  @@index([createdById])
  @@index([published])
}

// ==================== RECURSOS ====================

model Resource {
  id            String     @id @default(cuid())
  title         String
  description   String?    @db.Text
  type          ResourceType  // infographic, video, quiz, document
  
  topicId       String
  topic         Topic      @relation("TopicResources", fields: [topicId], references: [id], onDelete: Cascade)
  
  createdById   String
  createdBy     User       @relation("UserResources", fields: [createdById], references: [id])
  
  order         Int        @default(0)
  published     Boolean    @default(false)
  
  // Contenido
  content       String?    @db.Text
  mediaUrl      String?
  mediaType     String?    // image, video, pdf
  duration      Int?       // en segundos
  
  // Quiz
  quiz          Quiz?
  
  // Metadata
  tags          String[]
  views         Int        @default(0)
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
  deletedAt     DateTime?
  
  @@index([topicId])
  @@index([createdById])
  @@index([type])
  @@index([published])
}

// ==================== CUESTIONARIOS ====================

model Quiz {
  id            String     @id @default(cuid())
  resourceId    String     @unique
  resource      Resource   @relation(fields: [resourceId], references: [id], onDelete: Cascade)
  
  title         String
  passScore     Int        @default(80)  // Porcentaje
  attemptsLimit Int?       // null = ilimitados
  showFeedback  Boolean    @default(true)
  
  questions     Question[]
  responses     QuizResponse[]
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
}

model Question {
  id            String     @id @default(cuid())
  quizId        String
  quiz          Quiz       @relation(fields: [quizId], references: [id], onDelete: Cascade)
  
  order         Int
  type          QuestionType  // multiple_choice, true_false, short_answer
  question      String     @db.Text
  
  // Opciones (para multiple choice y true/false)
  options       Option[]
  
  answers       Answer[]
  
  createdAt     DateTime   @default(now())
  updatedAt     DateTime   @updatedAt
}

model Option {
  id            String     @id @default(cuid())
  questionId    String
  question      Question   @relation(fields: [questionId], references: [id], onDelete: Cascade)
  
  order         Int
  text          String     @db.Text
  isCorrect     Boolean
  feedback      String?    @db.Text
  
  answers       Answer[]
}

model Answer {
  id            String     @id @default(cuid())
  questionId    String
  question      Question   @relation(fields: [questionId], references: [id], onDelete: Cascade)
  
  optionId      String?
  option        Option?    @relation(fields: [optionId], references: [id], onDelete: SetNull)
  
  text          String?    @db.Text // Para respuestas abiertas
  
  createdAt     DateTime   @default(now())
}

model QuizResponse {
  id            String     @id @default(cuid())
  quizId        String
  quiz          Quiz       @relation(fields: [quizId], references: [id], onDelete: Cascade)
  
  userId        String?    // null = usuario anónimo
  email         String?    // Para tracking de anónimos
  
  score         Float
  passed        Boolean
  answers       Answer[]
  
  startedAt     DateTime
  completedAt   DateTime?
  
  @@index([quizId])
  @@index([userId])
}

// ==================== SEO Y METADATA ====================

model SEOData {
  id            String     @id @default(cuid())
  
  moduleId      String?    @unique
  module        Module?    @relation(fields: [moduleId], references: [id], onDelete: Cascade)
  
  topicId       String?    @unique
  topic         Topic?     @relation(fields: [topicId], references: [id], onDelete: Cascade)
  
  title         String?
  description   String?
  keywords      String[]
  ogImage       String?
  ogTitle       String?
  ogDescription String?
  canonical     String?
}

// ==================== AUDITORÍA ====================

model AuditLog {
  id            String     @id @default(cuid())
  userId        String
  user          User       @relation(fields: [userId], references: [id], onDelete: Cascade)
  
  action        AuditAction
  entityType    String     // Module, Topic, Resource, User
  entityId      String
  
  before        Json?
  after         Json?
  
  ipAddress     String?
  userAgent     String?
  
  createdAt     DateTime   @default(now())
  
  @@index([userId])
  @@index([action])
  @@index([createdAt])
}

// ==================== ENUMS ====================

enum UserRole {
  ADMIN
  EDITOR
  CONTRIBUTOR
  VIEWER
}

enum ResourceType {
  INFOGRAPHIC
  VIDEO
  QUIZ
  DOCUMENT
  INTERACTIVE
}

enum QuestionType {
  MULTIPLE_CHOICE
  TRUE_FALSE
  SHORT_ANSWER
  CASE_STUDY
}

enum AuditAction {
  CREATE
  UPDATE
  DELETE
  PUBLISH
  UNPUBLISH
  LOGIN
  LOGOUT
}
```

