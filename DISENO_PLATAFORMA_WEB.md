# Diseño de Plataforma: Caja de Herramientas para Docentes en IA

## Documento de Arquitectura Web y UX

**Versión:** 1.0  
**Fecha:** Abril 2026  
**Objetivo:** Definir experiencia, estructura técnica y navegación de la Caja.

---

## 1. Principios de Diseño

### Accesibilidad ante todo
- Funciona en conexión limitada (descargas offline).
- Responsive: móvil, tablet, escritorio.
- Cumple WCAG 2.1 AA (contraste, navegación por teclado).
- Textos en español claro, sin jerga técnica innecesaria.

### Navegación intuitiva
- El docente debe encontrar lo que necesita en **menos de 3 clics**.
- Filtros por: nivel, modalidad, propósito, urgencia.
- Búsqueda rápida (título, palabra clave, prompt).

### Descarga y portabilidad
- Cada ficha se descarga como PDF, Google Doc o ePub.
- Banco de prompts exportable a CSV/JSON.
- Instrumentos en plantilla editable (Google Docs, Word, Sheets).

### Retroalimentación activa
- Formulario simple en cada ficha: "¿Te fue útil?" + comentario.
- Rating visible de contribuciones comunitarias.
- Sección de "lo que funcionó / lo que no funcionó".

---

## 2. Estructura de Navegación Principal

```
┌─────────────────────────────────────────┐
│   CAJA DE HERRAMIENTAS IA MEP 2026     │
│   [Logo] [Buscador] [Mi cuenta]        │
└─────────────────────────────────────────┘
         │
         ├─ 📚 INICIO
         │  ├─ Qué es la Caja
         │  ├─ Cómo usar
         │  ├─ Novedades este trimestre
         │  └─ Comunidad destacada
         │
         ├─ 🎓 MÓDULOS PRINCIPALES
         │  ├─ 1️⃣ Fundamentos
         │  │  ├─ Conceptos clave
         │  │  ├─ Riesgos y límites
         │  │  ├─ Normativa MEP 2026
         │  │  └─ Verificación de info
         │  │
         │  ├─ 2️⃣ Herramientas por Propósito
         │  │  ├─ Generar ideas y borradores
         │  │  ├─ Analizar información
         │  │  ├─ Diseñar materiales
         │  │  ├─ Retroalimentar
         │  │  ├─ Organizar evidencias
         │  │  ├─ Crear adaptaciones
         │  │  └─ Resumir normativa
         │  │
         │  ├─ 3️⃣ Planeamiento y Mediación
         │  │  ├─ Diseño de unidades
         │  │  ├─ Estrategias por nivel
         │  │  ├─ Diferenciación y DUA
         │  │  ├─ Adaptaciones técnicas
         │  │  └─ Ahorros de tiempo
         │  │
         │  ├─ 4️⃣ Evaluación para el Aprendizaje
         │  │  ├─ Diagnóstica
         │  │  ├─ Formativa y realimentación
         │  │  ├─ Autoevaluación
         │  │  ├─ Coevaluación
         │  │  ├─ Instrumentos (rúbricas, bitácoras)
         │  │  ├─ Portafolio de evidencias
         │  │  └─ Demostración de aprendizaje
         │  │
         │  ├─ 5️⃣ Ética, Seguridad y Ciudadanía Digital
         │  │  ├─ Riesgos éticos
         │  │  ├─ Cuidado de datos
         │  │  ├─ Transparencia y honestidad
         │  │  ├─ Sesgos y verificación
         │  │  └─ Salvaguardas de privacidad
         │  │
         │  └─ 6️⃣ Comunidad y Actualización
         │     ├─ Retos mensuales
         │     ├─ Banco de prompts validados
         │     ├─ Casos de aula
         │     ├─ Lo que funcionó / No funcionó
         │     ├─ Novedades trimestrales
         │     ├─ Cápsulas de 10 min
         │     └─ Repositorio de evidencias
         │
         ├─ 🔍 FILTROS Y BÚSQUEDA
         │  ├─ Por nivel (Primaria | Sec. Académica | CTP | IPEC | CINDEA)
         │  ├─ Por propósito (idea, análisis, diseño, retroalimentación, etc.)
         │  ├─ Por trimestre (T1, T2, T3, T4)
         │  ├─ Por tipo (ficha, instrumento, caso, prompt, cápsula)
         │  └─ Por etiqueta (rápido, urgente, inclusivo, ético)
         │
         ├─ 📥 DESCARGAS Y PLANTILLAS
         │  ├─ Banco de prompts (CSV, JSON, PDF)
         │  ├─ Instrumentos editables (Google Docs, Word, Sheets)
         │  ├─ Plantillas de unidad
         │  ├─ Rúbricas
         │  ├─ Bitácoras
         │  └─ Portafolio digital (plantilla)
         │
         ├─ 💬 COMUNIDAD
         │  ├─ Foro de preguntas
         │  ├─ Retos activos
         │  ├─ Galería de casos reales
         │  ├─ Testimonios docentes
         │  ├─ "Lo que funcionó"
         │  └─ Conexión a Slack/Telegram
         │
         ├─ ⚙️ CONFIGURACIÓN
         │  ├─ Mi perfil (nivel, modalidad, intereses)
         │  ├─ Notificaciones
         │  ├─ Descargas favoritas
         │  └─ Historial
         │
         └─ ❓ AYUDA
            ├─ Preguntas frecuentes
            ├─ Guía de primeros pasos
            ├─ Contacto
            └─ Comentarios y sugerencias

```

---

## 3. Flujo de Usuario: Docente Típico

### Escenario 1: Docente nuevo, busca "cómo usar prompts"

```
1. Llega a INICIO
   ↓
2. Lee "Novedades este trimestre" (tiene contexto rápido)
   ↓
3. Usa BUSCADOR: "prompts básicos"
   ↓
4. Ve resultados filtrados por tipo (fichas) y nivel (su especialidad)
   ↓
5. Abre ficha "Estructura de prompts efectivos"
   ↓
6. Lee los 15 apartados, descarga PDF y plantilla
   ↓
7. Vuelve en 1 semana para reportar qué funcionó → COMUNIDAD
```

### Escenario 2: Docente CTP busca "adaptar actividad para estudiante con discapacidad"

```
1. Accede a MÓDULO 3: Planeamiento y Mediación
   ↓
2. Abre "Diferenciación y DUA"
   ↓
3. Filtra por "inclusivo" + "CTP"
   ↓
4. Ve 3 fichas + 1 caso específico de especialidad
   ↓
5. Descarga rúbrica de inclusión (apartado 13 de la plantilla)
   ↓
6. En 2 semanas sube su caso a "Comunidad" con resultado
```

### Escenario 3: Director busca "métricas de impacto de la Caja"

```
1. Accede a INICIO → Sección "Indicadores de uso"
   ↓
2. Ve dashboard: % adopción, recursos más usados, modalidades atendidas
   ↓
3. Descarga reporte trimestral (PDF)
   ↓
4. Comparte con stakeholders
```

---

## 4. Estructura de Carpetas en la Plataforma

### Opción A: Sitio Web Estático (Google Sites / Notion)

```
caja-herramientas-ia.edu.cr/
│
├─ index.html (INICIO)
│  ├─ Hero: "Espacio vivo de autoformación en IA"
│  ├─ Últimas novedades (3 tarjetas)
│  ├─ Acceso rápido a módulos (6 botones grandes)
│  ├─ Testimonio docente rotativo
│  └─ Llamada a acción: "Accede a Módulos"
│
├─ /modulos/
│  ├─ /1-fundamentos/
│  │  ├─ index.html
│  │  ├─ /fichas/
│  │  │  ├─ 1-qué-es-ia.md + PDF
│  │  │  ├─ 2-riesgos-alucinaciones.md + PDF
│  │  │  ├─ 3-verificación-info.md + PDF
│  │  │  └─ ...
│  │  ├─ /dossier/
│  │  │  └─ T1-2026-Alfabetización-IA.pdf
│  │  ├─ /prompts/
│  │  │  └─ banco-prompts-t1.csv
│  │  └─ /instrumentos/
│  │     ├─ rúbrica-uso-ético.docx
│  │     ├─ checklist-privacidad.xlsx
│  │     └─ ...
│  │
│  ├─ /2-herramientas-por-proposito/
│  │  ├─ index.html
│  │  ├─ /generar-ideas/
│  │  ├─ /analizar-info/
│  │  ├─ /diseñar-materiales/
│  │  ├─ /retroalimentar/
│  │  ├─ /organizar-evidencias/
│  │  ├─ /adaptar/
│  │  └─ /resumir-normativa/
│  │
│  ├─ /3-planeamiento-mediacion/
│  │  ├─ /primaria/
│  │  ├─ /secundaria/
│  │  ├─ /ctp/
│  │  ├─ /ipec-cindea/
│  │  └─ ...
│  │
│  ├─ /4-evaluacion/
│  │  ├─ /diagnostica/
│  │  ├─ /formativa/
│  │  ├─ /autoevaluacion/
│  │  ├─ /coevaluacion/
│  │  ├─ /instrumentos/
│  │  └─ ...
│  │
│  ├─ /5-etica-seguridad/
│  │  ├─ /riesgos-eticos/
│  │  ├─ /privacidad/
│  │  ├─ /honestidad-academica/
│  │  ├─ /sesgos/
│  │  └─ ...
│  │
│  └─ /6-comunidad/
│     ├─ /retos/
│     ├─ /casos-reales/
│     ├─ /lo-que-funciono/
│     ├─ /prompts-validados/
│     ├─ /capsulas/
│     └─ /repositorio-evidencias/
│
├─ /descargas/
│  ├─ banco-prompts-completo.csv
│  ├─ instrumentos/
│  ├─ plantillas/
│  └─ ...
│
├─ /comunidad/
│  ├─ foro.html
│  ├─ retos-activos.html
│  ├─ casos.html
│  ├─ testimonios.html
│  └─ ...
│
├─ /buscar/
│  ├─ search.html (buscador avanzado)
│  └─ filtros.js
│
├─ /perfil/
│  ├─ mi-cuenta.html
│  ├─ mis-descargas.html
│  ├─ historial.html
│  └─ preferencias.html
│
├─ /ayuda/
│  ├─ faq.html
│  ├─ primeros-pasos.html
│  ├─ contacto.html
│  └─ sugerencias.html
│
└─ /admin/
   ├─ dashboard.html (métricas)
   ├─ nuevo-contenido.html
   ├─ validación.html
   └─ reportes.html

```

---

## 5. Experiencia Visual y Diseño

### Paleta de Colores

```
Primario:       #0066CC (azul MEP)
Secundario:     #00AA44 (verde educación)
Acento:         #FF6B35 (naranja IA)
Neutro claro:   #F5F7FA
Neutro oscuro:  #2C3E50
Advertencia:    #FFAA00 (para riesgos éticos)
Éxito:          #22CC88
```

### Tipografía

- **Encabezados:** Inter Bold, 24-32px (legibilidad, modernidad)
- **Cuerpo:** Inter Regular, 16px (accesibilidad)
- **Etiquetas:** Inter Medium, 12-14px

### Componentes UI

#### Tarjeta de Ficha

```
┌─────────────────────────────────────┐
│ 🎓 Estructura de Prompts Efectivos  │  ← Ícono + Título
├─────────────────────────────────────┤
│ Propósito: Crear prompts claros... │  ← Descripción breve (2 líneas)
│                                     │
│ ⏱️ 15 min | 📌 Fácil | 🎯 T1        │  ← Meta información
│ 📚 Fichas | Primaria, Secundaria    │  ← Tipo y niveles
│                                     │
│ [⭐ 4.8] [💬 23] [↓ Descargar PDF]   │  ← Rating, comentarios, acción
└─────────────────────────────────────┘
```

#### Ficha Detallada (15 apartados)

```
┌────────────────────────────────────────────┐
│ ≡ VOLVER | COMPARTIR | ⭐ GUARDAR | ⋯      │
├────────────────────────────────────────────┤
│                                            │
│ # Estructura de Prompts Efectivos         │  Título
│ T1 2026 | Fundamentos | Gemini            │  Meta
│                                            │
│ ─────────────────────────────────────────│
│                                            │
│ 1️⃣  Para qué le sirve al docente         │  Apartados
│    [Texto]                                 │  numerados
│                                            │
│ 2️⃣  ¿Cuándo sí usar IA?                  │
│    [Texto]                                 │
│                                            │
│ ... (apartados 3-15)                      │
│                                            │
│ ─────────────────────────────────────────│
│ [PDF] [Google Docs] [Word] [ePub]        │  Descargas
│ ─────────────────────────────────────────│
│                                            │
│ ¿TE FUE ÚTIL?                             │  Feedback
│ [😊] [😐] [😞]  + Comentario              │
│                                            │
│ ─────────────────────────────────────────│
│ RELACIONADO:                               │  Sugerencias
│ • Prompts básicos (T1)                     │
│ • Verificación de información (T1)         │
│ • Uso responsable (T1)                     │
│                                            │
└────────────────────────────────────────────┘
```

#### Módulo (Índice)

```
┌────────────────────────────────────────────┐
│ 1️⃣ FUNDAMENTOS                             │  Título
│ Qué es IA, riesgos, normativa             │  Descripción
├────────────────────────────────────────────┤
│                                            │
│ 🎯 CONTENIDOS ESTE TRIMESTRE (T1 2026)    │
│                                            │
│ DOSSIER:                                   │
│ ┌──────────────────────────────────────┐  │
│ │ 📘 Alfabetización Docente en IA      │  │
│ │ 20-25 págs | Síntesis profunda       │  │
│ │ [↓ PDF]                              │  │
│ └──────────────────────────────────────┘  │
│                                            │
│ FICHAS PRÁCTICAS:                         │
│ ┌──────────────────────────────────────┐  │
│ │ 🎓 Qué es IA y qué no es             │  │
│ │ [⭐ 4.9] [💬 45] [↓]                  │  │
│ └──────────────────────────────────────┘  │
│ ┌──────────────────────────────────────┐  │
│ │ 🎓 Alucinaciones y sesgos             │  │
│ │ [⭐ 4.7] [💬 32] [↓]                  │  │
│ └──────────────────────────────────────┘  │
│ ... (más fichas)                          │
│                                            │
│ BANCO DE PROMPTS:                         │
│ ┌──────────────────────────────────────┐  │
│ │ 📋 20 prompts validados T1           │  │
│ │ [↓ CSV] [↓ JSON] [↓ PDF]             │  │
│ └──────────────────────────────────────┘  │
│                                            │
│ INSTRUMENTOS:                              │
│ ┌──────────────────────────────────────┐  │
│ │ 📊 Rúbrica: Uso ético de IA         │  │
│ │ [↓ Google Docs] [↓ Word]             │  │
│ └──────────────────────────────────────┘  │
│ ...                                        │
│                                            │
│ ALERTAS:                                   │
│ ┌──────────────────────────────────────┐  │
│ │ ⚠️ ALERTA: Riesgos de alucinaciones  │  │
│ │ Cómo verificar antes de usar         │  │
│ │ [→ Leer más]                         │  │
│ └──────────────────────────────────────┘  │
│                                            │
│ CASOS REALES:                              │
│ ┌──────────────────────────────────────┐  │
│ │ 🏫 Primaria: ChatGPT en el aula      │  │
│ │ [→ Leer]                             │  │
│ └──────────────────────────────────────┘  │
│                                            │
└────────────────────────────────────────────┘
```

---

## 6. Buscador y Filtros

### Búsqueda Avanzada

```
┌─────────────────────────────────────┐
│ 🔍 Buscar en la Caja                │
├─────────────────────────────────────┤
│                                     │
│ [____________________________]       │  Campo texto
│ Ej: "prompts", "evaluación"        │
│                                     │
│ 🎯 FILTROS:                         │
│                                     │
│ Nivel:                              │
│ ☐ Primaria                          │
│ ☐ Secundaria Académica              │
│ ☐ CTP                               │
│ ☐ IPEC/CINDEA                       │
│                                     │
│ Propósito:                          │
│ ☐ Generar ideas                     │
│ ☐ Analizar información              │
│ ☐ Diseñar materiales                │
│ ☐ Retroalimentar                    │
│ ☐ Organizar evidencias              │
│ ☐ Crear adaptaciones                │
│ ☐ Resumir normativa                 │
│                                     │
│ Trimestre:                          │
│ ☐ T1 2026 ☐ T2 2026 ☐ T3 2026 ☐ T4│
│                                     │
│ Tipo:                               │
│ ☐ Fichas  ☐ Dossier  ☐ Prompts     │
│ ☐ Instrumentos  ☐ Cápsulas          │
│                                     │
│ Etiquetas:                          │
│ ☐ Rápido (< 15 min)                │
│ ☐ Urgente                           │
│ ☐ Inclusivo (DUA)                   │
│ ☐ Ético                             │
│                                     │
│ [BUSCAR] [LIMPIAR FILTROS]          │
│                                     │
└─────────────────────────────────────┘
```

---

## 7. Sección Comunidad

### Estructura

```
┌─────────────────────────────────────────────────────┐
│ 💬 COMUNIDAD Y TRANSFERENCIA AL AULA               │
├─────────────────────────────────────────────────────┤
│                                                     │
│ RETOS ACTIVOS ESTE MES                             │
│ ┌──────────────────────────────────────────────┐   │
│ │ 🎯 Reto 1: Diseña una evaluación diagnóstica │   │
│ │ con IA en tu especialidad                    │   │
│ │ Plazo: hasta 30 de abril | 47 participantes │   │
│ │ [↑ Participa]                                │   │
│ └──────────────────────────────────────────────┘   │
│ ┌──────────────────────────────────────────────┐   │
│ │ 🎯 Reto 2: Crea un prompt mejorado usando... │   │
│ │ Plazo: hasta 7 de mayo | 23 participantes   │   │
│ │ [↑ Participa]                                │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ LO QUE FUNCIONÓ ESTA SEMANA                        │
│ ┌──────────────────────────────────────────────┐   │
│ │ 👨‍🏫 Docente: María González (Primaria)        │   │
│ │ "Usé ChatGPT para generar 5 formas diferentes│   │
│ │  de explicar fracción. Los estudiantes      │   │
│ │  eligieron su favorita. ¡Excelente!"        │   │
│ │ 📌 Etiquetas: #diferenciación #primaria     │   │
│ │ [❤️ 127] [💬 12] [→ Ver más]                 │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ GALERÍA DE CASOS REALES                            │
│ ┌──────────────────────────────────────────────┐   │
│ │ 🏫 Secundaria: Proyecto ABP + IA             │   │
│ │ Docente: Roberto Martínez (Siquirres)        │   │
│ │ "Estudiantes usaron Gemini para analizar...  │   │
│ │ [↓ PDF con case study completo] [↓ Video]   │   │
│ │ [❤️ 234] [💬 28]                             │   │
│ └──────────────────────────────────────────────┘   │
│ ┌──────────────────────────────────────────────┐   │
│ │ 🏭 CTP: Automatización + Ética                │   │
│ │ Docente: Carlos Rojas (San José)             │   │
│ │ "En programación, enseñamos a estudiantes... │   │
│ │ [↓ Código fuente] [↓ Rúbrica]                │   │
│ │ [❤️ 189] [💬 15]                             │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ FORO DE PREGUNTAS                                  │
│ ┌──────────────────────────────────────────────┐   │
│ │ ❓ ¿Cómo verifico que ChatGPT no plagia?    │   │
│ │ 👤 Preguntado hace 2 horas | 8 respuestas   │   │
│ │ [→ Ver]                                      │   │
│ └──────────────────────────────────────────────┘   │
│ ┌──────────────────────────────────────────────┐   │
│ │ ❓ ¿Puedo usar NotebookLM con fuentes...?    │   │
│ │ 👤 Preguntado hace 1 día | 5 respuestas      │   │
│ │ [→ Ver]                                      │   │
│ └──────────────────────────────────────────────┘   │
│                                                     │
│ [+ Hacer una pregunta] [+ Compartir caso]         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 8. Dashboard de Admin / Coordinador

```
┌─────────────────────────────────────────┐
│ 📊 PANEL DE COORDINACIÓN                │
├─────────────────────────────────────────┤
│                                         │
│ MÉTRICAS EN VIVO (T1 2026)              │
│                                         │
│ 👥 Docentes registrados: 1,247         │
│ 📥 Descargas este trimestre: 3,456     │
│ 💬 Casos subidos: 47                    │
│ 💭 Comentarios: 892                     │
│ ⭐ Rating promedio: 4.7/5.0             │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ ADOPCIÓN POR MODALIDAD:                 │
│ Primaria:           ████████░░ 87%     │
│ Secundaria Acad:    ████████░░ 82%     │
│ CTP:                ██████░░░░ 61%     │
│ IPEC/CINDEA:        ████░░░░░░ 42%     │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ CONTENIDO MÁS DESCARGADO:              │
│ 1. Banco prompts T1       ↓ 456        │
│ 2. Rúbrica evaluación     ↓ 323        │
│ 3. Caso secundaria        ↓ 289        │
│ 4. Ficha DUA              ↓ 234        │
│ 5. Dossier T1             ↓ 198        │
│                                         │
│ ─────────────────────────────────────  │
│                                         │
│ TAREAS PENDIENTES:                      │
│ □ Validar 3 casos comunitarios         │
│ □ Actualizar herramientas (Gemini)     │
│ □ Publicar ficha de privacidad         │
│ □ Revisar 5 comentarios flagged        │
│                                         │
│ [CREAR NUEVO CONTENIDO]                │
│ [GENERAR REPORTE TRIMESTRAL]           │
│ [EXPORTAR DATOS]                       │
│                                         │
└─────────────────────────────────────────┘
```

---

## 9. Tecnología Recomendada

### Opción 1: Solución Ligera (Recomendada para inicio)

**Stack:** Google Workspace + Notion + Netlify

| Componente | Herramienta | Razón |
|-----------|-----------|-------|
| Contenido y CMS | Notion Database | Fácil de gestionar, sin código |
| Hosting web | Google Sites / Netlify | Rápido, gratuito o bajo costo |
| Buscador | Algolia (free tier) | Rápido, escalable |
| Formularios | Google Forms | Integrado con Workspace |
| Descargas | Google Drive + enlaces públicos | Seguro, con control de acceso |
| Analítica | Google Analytics + Looker Studio | Integrado |
| Comunidad | Google Groups + Slack gratuito | Centralizado |

**Ventajas:**
- Bajo costo (~$0-50/mes)
- No requiere mantenimiento técnico
- Los docentes ya conocen Google
- Escalable rápidamente

**Tiempo de setup:** 2-3 semanas

---

### Opción 2: Solución Robusta (Escalabilidad futura)

**Stack:** Next.js + Supabase + Vercel

| Componente | Herramienta | Razón |
|-----------|-----------|-------|
| Frontend | Next.js + React | Moderno, SEO, performance |
| Backend | Supabase (PostgreSQL) | Base de datos confiable |
| Hosting | Vercel | Despliegue automático |
| Almacenamiento | Cloudinary / Supabase Storage | Imágenes, PDFs |
| Autenticación | Auth0 / Supabase Auth | Seguro, OAuth |
| Búsqueda avanzada | Elasticsearch / Typesense | Poderoso |
| Email | SendGrid | Notificaciones |

**Ventajas:**
- Altamente customizable
- Rendimiento óptimo
- Comunidad activa

**Tiempo de setup:** 4-6 semanas
**Costo:** $50-200/mes

---

### Opción 3: Plataforma Existente (Máxima rapidez)

**Opciones:**
- **Moodle con tema personalizado** (si ya existe infraestructura MEP)
- **Teachable / Kajabi** (LMS educativo)
- **WordPress + plugin** (p. ej., LearnDash)

**Ventajas:**
- Funcionalidad educativa integrada
- Comunidad de usuarios grande

**Desventaja:**
- Menos flexible
- Puede ser costoso

---

## 10. Estructura de Datos en Base de Datos

### Modelo Notion/Supabase

```
TABLA: Fichas
├── ID (único)
├── Título
├── Módulo (1-6)
├── Tema
├── Descripción breve
├── Apartado 1-15 (JSONB)
├── Nivel (array: primaria, secundaria, ctp, ipec, cindea)
├── Propósito (array: idea, análisis, diseño, etc.)
├── Trimestre (T1, T2, T3, T4, 2026)
├── Autor
├── Fecha creación
├── Fecha actualización
├── Estado (publicada, borrador, validación)
├── Rating (promedio)
├── Descargas (count)
├── Etiquetas (array: rápido, inclusivo, ético, etc.)
├── URL a PDF/Docs/DOCX
└── Comentarios (relación)

TABLA: Comentarios
├── ID
├── Ficha ID (FK)
├── Autor
├── Texto
├── Útil (emoji: 😊, 😐, 😞)
├── Fecha
└── Reportado (flag para moderación)

TABLA: Casos Reales
├── ID
├── Título
├── Descripción
├── Modalidad
├── Docente
├── Foto/Video
├── Resultados
├── URL a descarga
├── Rating
├── Relacionado con Fichas (array)
└── Fecha

TABLA: Prompts Validados
├── ID
├── Nombre
├── Prompts base + mejorado
├── Herramienta
├── Propósito
├── Resultado esperado
├── Trimestre
└── Validado por

TABLA: Usuarios
├── ID
├── Email
├── Nombre
├── Modalidad (primaria, secundaria, ctp, etc.)
├── Nivel (directivo, docente, docente-investigador)
├── Intereses (array de temas)
├── Descargas favoritas
├── Fecha registro
└── Notificaciones (ON/OFF)
```

---

## 11. Flujo de Acceso (Público vs. Autenticado)

### Acceso Público

- ✅ Ver módulos principales
- ✅ Leer fichas (primeros 3 apartados)
- ✅ Ver títulos y descriptions
- ✅ Búsqueda básica
- ❌ Descargar recursos
- ❌ Comentar
- ❌ Participar en retos

### Acceso Autenticado (Docente registrado)

- ✅ Leer fichas completas (15 apartados)
- ✅ Descargar en múltiples formatos
- ✅ Comentar y hacer preguntas
- ✅ Guardar favoritos
- ✅ Participar en retos
- ✅ Subir casos
- ✅ Ver historial de descargas

### Acceso Admin

- ✅ Todo lo anterior +
- ✅ Crear y editar contenido
- ✅ Validar casos comunitarios
- ✅ Moderar comentarios
- ✅ Ver dashboard de métricas
- ✅ Generar reportes

---

## 12. Mantenimiento y Actualización

### Ciclo de Vida de Contenido

```
SEMANA 1-2: RASTREO
│
├─ Antigravity rastrea cambios en Guía MEP, REAC
├─ Google Alerts en normativa nueva
├─ Recopila dudas del foro
│
↓ SEMANA 2: CURADURÍA
│
├─ Prioriza 6 contenidos nuevos/actualizados
├─ Asigna propietarios
│
↓ SEMANA 3: PRODUCCIÓN
│
├─ Antigravity genera borradores
├─ Gemini crea variantes
├─ NotebookLM resume fuentes
├─ Este GPT normaliza estructura
├─ Se guardan en Notion (estado: "Borrador")
│
↓ SEMANA 4: VALIDACIÓN
│
├─ Revisor ética ✓
├─ Revisor pedagógico ✓
├─ Revisor inclusión ✓
├─ Revisor coherencia evaluativa ✓
├─ Estado → "Validada"
│
↓ SEMANA 5: PUBLICACIÓN
│
├─ Exporta desde Notion a MD + PDF
├─ Sube a Google Drive / Netlify
├─ Publica en plataforma
├─ Notifica a docentes: "Novedades T2"
├─ Activa reto mensual
└─ Estado → "Publicada"
```

---

## 13. Checklist de Lanzamiento

- [ ] Definir nombre de dominio
- [ ] Elegir plataforma (recomendación: Opción 1 para inicio rápido)
- [ ] Crear mockups/wireframes finales
- [ ] Configurar hosting
- [ ] Importar contenido T1 a CMS
- [ ] Configurar buscador y filtros
- [ ] Diseñar interfaz gráfica (aplicar paleta de colores)
- [ ] Desarrollar módulos (6 secciones principales)
- [ ] Integrar Google Forms para feedback
- [ ] Configurar Google Analytics
- [ ] Crear landing page atractiva
- [ ] Testing: accesibilidad, responsive, velocidad
- [ ] Capacitar a coordinadores en CMS
- [ ] Lanzamiento soft (usuarios piloto)
- [ ] Comunicación a docentes
- [ ] Recopilación de feedback inicial
- [ ] Ajustes rápidos
- [ ] Lanzamiento público oficial

---

## 14. Roadmap: Primeros 3 Meses

### Mes 1 (Abril 2026): Setup y Prototipo

**Semana 1-2:**
- Elegir plataforma
- Crear estructura de carpetas
- Diseñar mockups

**Semana 3-4:**
- Configurar hosting
- Importar contenido T1
- Diseñar interfaz gráfica

### Mes 2 (Mayo 2026): Alpha y Piloto

- Lanzamiento a grupo piloto de 50 docentes
- Recopilación intensiva de feedback
- Ajustes rápidos

### Mes 3 (Junio 2026): Beta y Escalado

- Lanzamiento público oficial
- Activación de comunidad (retos, casos)
- Inicio de producción T2

---

## 15. Matriz de Decisión: ¿Cuál Plataforma Elegir?

| Criterio | Opción 1 (Ligera) | Opción 2 (Robusta) | Opción 3 (Existente) |
|----------|------------------|-------------------|------------------|
| **Costo** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Rapidez de setup** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Facilidad de uso** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Escalabilidad** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Customización** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Soporte técnico** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

**Recomendación:** **Opción 1 (Google Sites + Notion)** para lanzamiento rápido. Migrar a Opción 2 en T3-T4 2026 si crece la demanda.

---

**Documento compilado: Abril 2026**  
**Próxima revisión: Julio 2026**

