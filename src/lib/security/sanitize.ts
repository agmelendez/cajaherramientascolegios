// Archivo: src/lib/security/sanitize.ts
// Sanitización de inputs

import { JSDOM } from 'jsdom';
import DOMPurify from 'isomorphic-dompurify';

/**
 * Sanitiza HTML para evitar XSS
 */
export function sanitizeHtml(html: string): string {
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: [
      'b',
      'i',
      'em',
      'strong',
      'a',
      'p',
      'br',
      'ul',
      'ol',
      'li',
      'h1',
      'h2',
      'h3',
      'code',
      'pre',
    ],
    ALLOWED_ATTR: ['href', 'target', 'rel'],
    KEEP_CONTENT: true,
  });
}

/**
 * Sanitiza strings simples
 */
export function sanitizeString(str: string): string {
  if (!str) return '';
  
  return str
    .trim()
    .replace(/[<>]/g, '') // Eliminar < y >
    .replace(/javascript:/gi, '') // Bloquear javascript:
    .replace(/on\w+=/gi, ''); // Bloquear event handlers
}

/**
 * Valida email
 */
export function validateEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

/**
 * Valida URL
 */
export function validateURL(url: string): boolean {
  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}

/**
 * Escapa caracteres especiales
 */
export function escapeHtml(text: string): string {
  const map: { [key: string]: string } = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;',
  };
  return text.replace(/[&<>"']/g, (m) => map[m]);
}

/**
 * Valida slug
 */
export function isValidSlug(slug: string): boolean {
  const slugRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
  return slugRegex.test(slug);
}

/**
 * Valida contraseña fuerte
 */
export function isStrongPassword(password: string): {
  strong: boolean;
  errors: string[];
} {
  const errors: string[] = [];

  if (password.length < 12) {
    errors.push('La contraseña debe tener mínimo 12 caracteres');
  }
  if (!/[A-Z]/.test(password)) {
    errors.push('Debe incluir al menos una mayúscula');
  }
  if (!/[a-z]/.test(password)) {
    errors.push('Debe incluir al menos una minúscula');
  }
  if (!/[0-9]/.test(password)) {
    errors.push('Debe incluir al menos un número');
  }
  if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
    errors.push('Debe incluir al menos un carácter especial');
  }

  return {
    strong: errors.length === 0,
    errors,
  };
}

/**
 * Sanitiza objeto completo
 */
export function sanitizeObject(obj: any): any {
  if (obj === null || obj === undefined) return obj;

  if (typeof obj === 'string') {
    return sanitizeString(obj);
  }

  if (typeof obj === 'object') {
    if (Array.isArray(obj)) {
      return obj.map((item) => sanitizeObject(item));
    }

    const sanitized: any = {};
    for (const key in obj) {
      if (obj.hasOwnProperty(key)) {
        sanitized[key] = sanitizeObject(obj[key]);
      }
    }
    return sanitized;
  }

  return obj;
}
