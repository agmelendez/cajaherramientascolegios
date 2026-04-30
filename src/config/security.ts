// Archivo: src/config/security.ts
// Configuración de seguridad centralizada

export const SECURITY_CONFIG = {
  // CSRF Protection
  csrf: {
    enabled: true,
    cookieName: '__Host-csrf-token',
    headerName: 'x-csrf-token',
    maxAge: 60 * 60 * 24, // 24 horas
  },

  // Rate Limiting
  rateLimit: {
    enabled: true,
    // Generales
    global: {
      windowMs: 15 * 60 * 1000, // 15 minutos
      max: 100, // 100 requests
    },
    // Login
    login: {
      windowMs: 15 * 60 * 1000,
      max: 5, // 5 intentos
    },
    // API
    api: {
      windowMs: 60 * 1000, // 1 minuto
      max: 30,
    },
  },

  // Sesiones
  session: {
    maxAge: 24 * 60 * 60 * 1000, // 24 horas
    refreshThreshold: 60 * 60 * 1000, // Refresh si quedan <1 hora
    secure: process.env.NODE_ENV === 'production',
    httpOnly: true,
    sameSite: 'strict',
  },

  // JWT
  jwt: {
    algorithm: 'HS256',
    expiresIn: '24h',
    refreshExpiresIn: '7d',
  },

  // Password
  password: {
    minLength: 12,
    requireUppercase: true,
    requireLowercase: true,
    requireNumbers: true,
    requireSpecialChars: true,
  },

  // Headers de seguridad
  headers: {
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Permissions-Policy': 'geolocation=(), microphone=(), camera=()',
  },

  // CORS
  cors: {
    origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
    credentials: true,
    methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization', 'X-CSRF-Token'],
  },

  // Content Security Policy
  csp: {
    directives: {
      defaultSrc: ["'self'"],
      scriptSrc: ["'self'", "'unsafe-inline'", 'https://cdn.jsdelivr.net'],
      styleSrc: ["'self'", "'unsafe-inline'"],
      imgSrc: ["'self'", 'data:', 'https:'],
      connectSrc: ["'self'"],
      fontSrc: ["'self'", 'data:'],
      objectSrc: ["'none'"],
      upgradeInsecureRequests: [],
    },
  },

  // Encriptación
  encryption: {
    algorithm: 'aes-256-gcm',
    keyDerivation: 'pbkdf2',
  },

  // Auditoría
  audit: {
    enabled: true,
    logSensitiveData: false,
    actions: [
      'CREATE',
      'UPDATE',
      'DELETE',
      'LOGIN',
      'LOGOUT',
      'PUBLISH',
    ],
  },
};

export const ROLES_PERMISSIONS = {
  ADMIN: {
    canManageUsers: true,
    canManageRoles: true,
    canPublish: true,
    canDelete: true,
    canViewAudit: true,
    canConfigureSettings: true,
  },
  EDITOR: {
    canManageUsers: false,
    canManageRoles: false,
    canPublish: true,
    canDelete: true,
    canViewAudit: false,
    canConfigureSettings: false,
  },
  CONTRIBUTOR: {
    canManageUsers: false,
    canManageRoles: false,
    canPublish: false,
    canDelete: false,
    canViewAudit: false,
    canConfigureSettings: false,
  },
  VIEWER: {
    canManageUsers: false,
    canManageRoles: false,
    canPublish: false,
    canDelete: false,
    canViewAudit: false,
    canConfigureSettings: false,
  },
};
