// Archivo: src/lib/security/csrf.ts
// Protección CSRF

import { NextRequest, NextResponse } from 'next/server';
import crypto from 'crypto';

const CSRF_TOKEN_LENGTH = 32;

/**
 * Genera un token CSRF
 */
export function generateCSRFToken(): string {
  return crypto.randomBytes(CSRF_TOKEN_LENGTH).toString('hex');
}

/**
 * Valida un token CSRF
 */
export function validateCSRFToken(
  tokenFromRequest: string,
  tokenFromSession: string
): boolean {
  if (!tokenFromRequest || !tokenFromSession) {
    return false;
  }

  // Usar comparación de tiempo constante para evitar timing attacks
  return crypto.timingSafeEqual(
    Buffer.from(tokenFromRequest),
    Buffer.from(tokenFromSession)
  );
}

/**
 * Middleware CSRF
 */
export function csrfMiddleware(
  request: NextRequest,
  config: any
): NextResponse | null {
  // Skip CSRF para GET, HEAD, OPTIONS
  if (['GET', 'HEAD', 'OPTIONS'].includes(request.method)) {
    return null;
  }

  // Obtener token del header
  const tokenFromHeader = request.headers.get(config.headerName);
  
  // Obtener token de cookie
  const tokenFromCookie = request.cookies.get(config.cookieName)?.value;

  if (!tokenFromHeader || !tokenFromCookie) {
    return new NextResponse('Missing CSRF token', { status: 403 });
  }

  // Validar
  try {
    if (!validateCSRFToken(tokenFromHeader, tokenFromCookie)) {
      return new NextResponse('Invalid CSRF token', { status: 403 });
    }
  } catch (error) {
    return new NextResponse('CSRF validation error', { status: 403 });
  }

  return null;
}
