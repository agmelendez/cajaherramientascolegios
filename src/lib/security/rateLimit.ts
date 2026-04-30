// Archivo: src/lib/security/rateLimit.ts
// Rate Limiting

import { NextRequest, NextResponse } from 'next/server';

interface RateLimitStore {
  [key: string]: {
    count: number;
    resetTime: number;
  };
}

// Store en memoria (en producción, usar Redis)
const rateLimitStore: RateLimitStore = {};

export interface RateLimitConfig {
  windowMs: number; // Ventana de tiempo en ms
  max: number; // Máximo de requests
}

/**
 * Clave única del cliente (IP + User Agent)
 */
function getClientKey(request: NextRequest, prefix: string): string {
  const ip =
    request.headers.get('x-forwarded-for') ||
    request.headers.get('x-real-ip') ||
    'unknown';
  const ua = request.headers.get('user-agent') || 'unknown';
  
  return `${prefix}:${ip}:${ua}`;
}

/**
 * Verifica rate limit
 */
export function checkRateLimit(
  request: NextRequest,
  config: RateLimitConfig,
  prefix: string = 'global'
): { allowed: boolean; remaining: number; reset: number } {
  const key = getClientKey(request, prefix);
  const now = Date.now();

  // Inicializar si no existe
  if (!rateLimitStore[key]) {
    rateLimitStore[key] = {
      count: 1,
      resetTime: now + config.windowMs,
    };
    return {
      allowed: true,
      remaining: config.max - 1,
      reset: rateLimitStore[key].resetTime,
    };
  }

  const record = rateLimitStore[key];

  // Reset si la ventana pasó
  if (now > record.resetTime) {
    record.count = 1;
    record.resetTime = now + config.windowMs;
    return {
      allowed: true,
      remaining: config.max - 1,
      reset: record.resetTime,
    };
  }

  // Incrementar contador
  record.count++;

  const allowed = record.count <= config.max;
  const remaining = Math.max(0, config.max - record.count);

  return {
    allowed,
    remaining,
    reset: record.resetTime,
  };
}

/**
 * Middleware Rate Limit
 */
export function rateLimitMiddleware(
  request: NextRequest,
  config: RateLimitConfig,
  prefix: string = 'global'
): NextResponse | null {
  const result = checkRateLimit(request, config, prefix);

  if (!result.allowed) {
    const response = new NextResponse('Too many requests', { status: 429 });
    response.headers.set('Retry-After', String(result.reset));
    response.headers.set('X-RateLimit-Limit', String(config.max));
    response.headers.set('X-RateLimit-Remaining', String(result.remaining));
    response.headers.set('X-RateLimit-Reset', String(result.reset));
    return response;
  }

  return null;
}

/**
 * Limpia tokens expirados (ejecutar periódicamente)
 */
export function cleanExpiredTokens(): void {
  const now = Date.now();
  for (const key in rateLimitStore) {
    if (rateLimitStore[key].resetTime < now) {
      delete rateLimitStore[key];
    }
  }
}

// Ejecutar limpieza cada 10 minutos
setInterval(cleanExpiredTokens, 10 * 60 * 1000);
