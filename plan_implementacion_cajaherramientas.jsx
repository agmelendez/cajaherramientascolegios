import { useState } from "react";

const SPRINTS = [
  {
    id: 1,
    code: "S1",
    label: "Corrección conceptual y teórica",
    color: "coral",
    hex50: "#FAECE7", hex200: "#F0997B", hex600: "#993C1D", hex800: "#712B13",
    priority: "Crítica",
    duration: "2–3 días",
    issues: [
      "TPACK presentado como modelo lineal (debe ser integrador/interseccional)",
      "SAMR desconectado de lo disciplinar y pedagógico",
      "Ausencia total del rol docente en la era IA como eje articulador",
      "Sin fundamentación en teorías del aprendizaje ni en la didáctica"
    ],
    tasks: [
      {
        id: "S1-T1",
        title: "Rediseñar la representación del modelo TPACK",
        file: "modulo-1.html (y donde aparezca TPACK)",
        detail: "Reemplazar cualquier presentación lineal o secuencial de TPACK por el diagrama de tres círculos superpuestos (Mishra & Koehler, 2006). Destacar que el centro de intersección (TPACK) no es alcanzable sin la simultánea integración de conocimiento tecnológico, pedagógico y de contenido. Agregar nota explicativa que los tres dominios se co-determinan: no existe adopción tecnológica pedagógicamente neutra.",
        deliverable: "Componente SVG reutilizable + texto explicativo con referencia a Mishra, P., & Koehler, M. J. (2006). Technological pedagogical content knowledge. Teachers College Record, 108(6), 1017–1054."
      },
      {
        id: "S1-T2",
        title: "Revisar la presentación del modelo SAMR",
        file: "Módulos 1–3 y cualquier infografía SAMR",
        detail: "SAMR (Puentedura, 2006) no es un modelo de adopción tecnológica independiente de lo disciplinar. Cada nivel (Substitution, Augmentation, Modification, Redefinition) debe presentarse con ejemplos que mantengan el objetivo de aprendizaje como punto de partida, no la herramienta. Añadir la crítica académica: SAMR tiende al determinismo tecnológico si no se ancla en la intención pedagógica. Citar: Hamilton, E. R., Rosenberg, J. M., & Akcaoglu, M. (2016). The substitution augmentation modification redefinition (SAMR) model. TechTrends, 60(5), 433–441.",
        deliverable: "Infografía corregida con eje pedagógico explícito + texto crítico + referencia completa"
      },
      {
        id: "S1-T3",
        title: "Incorporar sección transversal: 'El rol docente en la era de la IA'",
        file: "Nueva página: rol-docente-ia.html + enlace desde todos los módulos",
        detail: "Desarrollar sección que responda: (1) ¿Para qué se incorpora la IA al trabajo docente? (2) ¿Desde qué concepción del aprendizaje? (3) ¿Qué es irreemplazable en el quehacer profesional del docente? (4) ¿Cómo cambia el rol docente, no la herramienta? Referenciar: Selwyn, N. (2019). Should Robots Replace Teachers? Polity; Williamson, B., Eynon, R., & Potter, J. (2020). Pandemic politics, pedagogies and practices. Learning, Media and Technology, 45(2), 107–114.",
        deliverable: "Página HTML nueva con 4 secciones, tono reflexivo y preguntas detonadoras por sección"
      },
      {
        id: "S1-T4",
        title: "Agregar mapa de la IA en las etapas didácticas",
        file: "Nueva sección en modulo-1.html o rol-docente-ia.html",
        detail: "Construir una tabla/infografía que mapee las etapas de la planificación didáctica (objetivo de aprendizaje → selección de contenido → estrategia didáctica → instrumentos de evaluación → retroalimentación) con los momentos en que la IA puede apoyar y los momentos en que el juicio profesional docente es irreemplazable. Cada fila debe tener: etapa / qué hace el docente / qué puede hacer la IA / riesgo si se delega sin criterio.",
        deliverable: "Tabla HTML interactiva con tooltips + nota sobre la irreductibilidad del juicio docente"
      }
    ]
  },
  {
    id: 2,
    code: "S2",
    label: "Citación y rigor bibliográfico",
    color: "amber",
    hex50: "#FAEEDA", hex200: "#EF9F27", hex600: "#854F0B", hex800: "#633806",
    priority: "Alta",
    duration: "1–2 días",
    issues: [
      "Infografías sin fuentes bibliográficas visibles",
      "Contenido del módulo IA en Educación citado solo como un video de YouTube (insuficiente)",
      "Ausencia de referencias pedagógicas (todo el contenido tiene sesgo tecnológico)"
    ],
    tasks: [
      {
        id: "S2-T1",
        title: "Agregar pie de fuente a cada infografía",
        file: "Todas las infografías en /Infografías/",
        detail: "Cada infografía debe incluir en su parte inferior (fuente legible ≥ 10pt): la referencia en formato APA 7.ª ed. de donde se tomó el contenido. Si es elaboración propia, indicar 'Elaboración propia, UCR-CIOdD, 2026' con base en las referencias que fundamentaron el contenido. Si la infografía proviene de un video o charla, citar como fuente primaria el documento académico que respalda la afirmación, no el video.",
        deliverable: "Versiones actualizadas de todas las infografías con pie de fuente + archivo de referencias maestro en /docs/referencias.md"
      },
      {
        id: "S2-T2",
        title: "Sustituir o complementar la fuente del módulo IA en Educación",
        file: "ia-educacion.html",
        detail: "La fuente actual (video de YouTube) no es citable académicamente para una plataforma UCR. Mantenerlo como recurso de acceso, pero agregar mínimo 3–5 referencias académicas que respalden cada afirmación del módulo. Propuestas: Floridi, L. et al. (2020). An ethical framework for a good AI society. Minds and Machines; Luckin, R. (2017). Towards Artificial Intelligence-Based Assessment Systems. Nature Human Behaviour; Holmes, W. et al. (2022). Ethics of AI in Education. Journal of AI in Education.",
        deliverable: "Sección 'Fuentes y lectura complementaria' al final de ia-educacion.html con 5+ referencias en APA"
      },
      {
        id: "S2-T3",
        title: "Construir biblioteca de referencias pedagógicas del proyecto",
        file: "Nueva página: /docs/referencias.html",
        detail: "Crear una página de referencias bibliográficas organizadas por tema: (a) Fundamentos técnicos de IA, (b) IA en educación, (c) Marcos pedagógicos (TPACK, SAMR, DUA), (d) Ética y crítica tecnológica, (e) Normativa costarricense (MEP, REACOSU). Esta página debe ser enlazada desde el footer y desde cada módulo.",
        deliverable: "Página HTML de referencias con filtros por categoría, ~25 fuentes iniciales"
      }
    ]
  },
  {
    id: 3,
    code: "S3",
    label: "Alfabetización terminológica para principiantes",
    color: "teal",
    hex50: "#E1F5EE", hex200: "#5DCAA5", hex600: "#0F6E56", hex800: "#085041",
    priority: "Alta",
    duration: "1–2 días",
    issues: [
      "Términos técnicos sin glosar para nivel principiante: IA simbólica, parámetros, red neuronal, token, arquitectura Transformer",
      "El módulo IA en Educación usa lenguaje de divulgación tecnológica, no pedagógica",
      "El perfil 'Ninguna experiencia' recibe el mismo contenido que perfiles intermedios"
    ],
    tasks: [
      {
        id: "S3-T1",
        title: "Implementar sistema de glosario inline con tooltips",
        file: "ia-educacion.html, modulo-1.html y todos los módulos con tecnicismos",
        detail: "Envolver cada término técnico en un componente <abbr> o <span class='glosario'> que al hover/tap despliegue una definición en lenguaje cotidiano (máximo 2 oraciones) adaptada al nivel del usuario. El tooltip debe incluir: definición simple, analogía cotidiana y (opcionalmente) enlace al glosario completo. La detección del nivel debe venir del perfil seleccionado en el onboarding; si el usuario es 'Ninguna experiencia', el tooltip debe mostrarse automáticamente la primera vez sin requerir hover.",
        deliverable: "CSS + JS para sistema de tooltips accesible (WCAG AA) + diccionario JSON con ~20 términos clave"
      },
      {
        id: "S3-T2",
        title: "Reescribir secciones con tecnicismos no explicados para nivel principiante",
        file: "ia-educacion.html — secciones 2, 3 y 4",
        detail: "Las secciones '¿Cómo funcionan los LLMs?', 'El poder de la escala' y 'Capacidades Emergentes' usan lenguaje no apto para principiantes (tokens, redes neuronales, arquitectura Transformer, cadenas de pensamiento) sin contexto pedagógico suficiente. Reescribir estas secciones en versión 'A' (principiante, analogías cotidianas) y 'B' (intermedio/avanzado, lenguaje técnico). El contenido mostrado debe corresponder al nivel seleccionado en el onboarding.",
        deliverable: "Dos versiones de contenido por sección (data-level='beginner' / data-level='advanced') con JS que alterna según perfil guardado en localStorage"
      },
      {
        id: "S3-T3",
        title: "Crear glosario completo de IA para docentes",
        file: "Nueva página: glosario.html",
        detail: "Desarrollar glosario de términos de IA adaptado explícitamente a docentes sin formación técnica. Cada entrada: término → definición técnica (1 oración) → analogía pedagógica/cotidiana (1–2 oraciones) → ejemplo en el aula (1 oración). Términos mínimos: LLM, token, parámetros, red neuronal, IA generativa, IA simbólica, prompt, alucinación, modelo, entrenamiento, sesgo algorítmico, datos de entrenamiento. Ordenado alfabéticamente, con función de búsqueda.",
        deliverable: "Página HTML de glosario con ~25 términos + buscador en JS + enlace desde footer y módulos"
      }
    ]
  },
  {
    id: 4,
    code: "S4",
    label: "Perspectiva crítica y enfoque no solucionista",
    color: "purple",
    hex50: "#EEEDFE", hex200: "#AFA9EC", hex600: "#534AB7", hex800: "#3C3489",
    priority: "Alta",
    duration: "2 días",
    issues: [
      "El contenido actual tiene sesgo de solucionismo tecnológico",
      "No hay invitación explícita a la reflexión crítica sobre qué aporta y qué no aporta la IA",
      "Falta perspectiva sobre procesos profesionales irreemplazables del docente"
    ],
    tasks: [
      {
        id: "S4-T1",
        title: "Agregar sección de pensamiento crítico en cada módulo",
        file: "modulo-1.html, modulo-2.html, modulo-3.html",
        detail: "Al final de cada módulo agregar una sección '¿Qué sigue siendo tuyo?' que invite al docente a reflexionar sobre lo que la IA no puede sustituir en ese tema específico. Ejemplo para módulo 1: '¿Puede la IA decidir el objetivo de aprendizaje de TU grupo, en TU contexto, con lo que TÚ sabes de esos estudiantes?' Usar preguntas detonadoras, no afirmaciones. Fundamentar en: Biesta, G. (2017). The rediscovery of teaching. Routledge.",
        deliverable: "Sección HTML 'Reflexión crítica' con 3–4 preguntas por módulo + referencia de apoyo"
      },
      {
        id: "S4-T2",
        title: "Reencuadrar el tono de los módulos: de 'usar IA' a 'pensar con IA'",
        file: "Revisión editorial de todos los módulos",
        detail: "Realizar una revisión de tono en todo el contenido para desplazarlo de un registro prescriptivo ('use la IA para...') hacia uno reflexivo-crítico ('piense si la IA aporta en este momento'). Señales de solucionismo a corregir: listas de 'cuándo sí usar IA' sin contrapeso crítico, ejemplos que posicionan a la IA como eficiencia per se, ausencia de voz estudiantil o del aprendizaje como centro. Propuesta de Marco alternativo: la IA como 'interlocutor' en el diseño didáctico, no como atajo.",
        deliverable: "Guía de tono editorial para el proyecto (1 página) + versiones revisadas de secciones 1, 2 y 3 de modulo-1.html"
      },
      {
        id: "S4-T3",
        title: "Agregar panel 'Lo que siempre comienza en ti' en la página de inicio",
        file: "index.html",
        detail: "Añadir un panel visible en la página de inicio que establezca el encuadre crítico de la plataforma antes de que el usuario entre a los módulos. Mensaje central: el proceso didáctico siempre comienza con el objetivo de aprendizaje, no con la herramienta. La IA puede apoyar; el docente decide. El panel debe tener 3–4 ítems visuales que representen los procesos profesionales irreductibles: (1) definir el objetivo, (2) conocer al estudiante, (3) diseñar la evaluación, (4) retroalimentar con criterio humano.",
        deliverable: "Componente HTML nuevo en index.html (panel tipo 'manifiesto pedagógico') con íconos y texto breve"
      }
    ]
  },
  {
    id: 5,
    code: "S5",
    label: "Adaptación real por nivel y andamiaje de navegación",
    color: "blue",
    hex50: "#E6F1FB", hex200: "#85B7EB", hex600: "#185FA5", hex800: "#0C447C",
    priority: "Media-Alta",
    duration: "3–4 días",
    issues: [
      "El sistema de selección de nivel no se refleja en el contenido (misma info para todos)",
      "Riesgo de navegación fragmentada sin andamiaje: un usuario puede saltar de módulo a módulo sin secuencia",
      "No hay indicador de prerrequisitos entre secciones"
    ],
    tasks: [
      {
        id: "S5-T1",
        title: "Implementar diferenciación de contenido real según nivel seleccionado",
        file: "Todos los módulos + sistema de perfil",
        detail: "El perfil del usuario (Ninguna/Básica/Intermedia) debe traducirse en: (a) densidad del texto (principiante: máx. 150 palabras por sección; avanzado: hasta 300), (b) tecnicismos activados/desactivados, (c) ejemplos diferenciados por nivel, (d) microretos de distinta complejidad. Implementar con data attributes en HTML (data-level='beginner|intermediate|advanced') + función JS setLevelContent() que lee el perfil de localStorage y activa el contenido correspondiente. Si el usuario no completó el onboarding, mostrar siempre nivel básico por defecto.",
        deliverable: "Sistema JS de perfiles completo + contenido en 2 niveles para módulo 1 como prueba piloto"
      },
      {
        id: "S5-T2",
        title: "Diseñar sistema de prerrequisitos y andamiaje entre módulos",
        file: "modulos.html + todos los módulos",
        detail: "Implementar una barra de progreso con indicadores de prerrequisito: antes de ingresar al módulo N, el sistema sugiere (no bloquea) completar los módulos previos relevantes. Cada módulo debe incluir al inicio: '¿Qué deberías conocer antes?' con enlaces a contenidos anteriores. Añadir un 'mapa de ruta de aprendizaje' visual en modulos.html que muestre las dependencias conceptuales entre módulos (no una secuencia lineal rígida, sino una red de dependencias navegable).",
        deliverable: "Mapa de ruta SVG/HTML interactivo + sistema de sugerencias de prerrequisitos en modulos.html"
      },
      {
        id: "S5-T3",
        title: "Agregar anclajes de recuperación al final de cada sección",
        file: "Todos los módulos",
        detail: "Al final de cada sección dentro de un módulo (no solo al final del módulo completo), agregar un ancla de 2–3 preguntas de verificación de comprensión tipo 'check rápido' antes de avanzar. Para nivel principiante: preguntas de selección múltiple sencillas. Para nivel avanzado: preguntas de aplicación o reflexión. Esto reduce la fragmentación: el usuario no puede avanzar sin confirmar que asimiló lo básico, pero el sistema es sugerente, no punitivo.",
        deliverable: "Componente HTML reutilizable 'VerificationCheck' + implementación en módulo 1 como piloto"
      },
      {
        id: "S5-T4",
        title: "Revisar el sistema de recomendación del onboarding",
        file: "index.html (sección ¿Por dónde empiezo?)",
        detail: "Actualmente el sistema de 3 preguntas no vincula efectivamente el perfil con una ruta de aprendizaje coherente. Rediseñar: (1) la pregunta 2 ('¿Qué le interesa más aprender?') debe mapearse a los módulos concretos, (2) el resultado de la recomendación debe mostrar una ruta completa (3 módulos en secuencia), no solo 'ir al módulo X', (3) guardar el perfil completo en localStorage incluyendo nivel educativo para personalización de ejemplos.",
        deliverable: "Lógica JS revisada del onboarding + visualización de ruta de 3 pasos al recibir la recomendación"
      }
    ]
  }
];

const PRIORITY_COLORS = {
  "Crítica": { bg: "#FAECE7", text: "#993C1D", border: "#F0997B" },
  "Alta": { bg: "#FAEEDA", text: "#854F0B", border: "#EF9F27" },
  "Media-Alta": { bg: "#E6F1FB", text: "#185FA5", border: "#85B7EB" }
};

const EFFORT_COLORS = {
  "2–3 días": "#EEEDFE",
  "1–2 días": "#E1F5EE",
  "3–4 días": "#E6F1FB",
  "2 días": "#FAEEDA"
};

export default function ImplementationPlan() {
  const [activeSprint, setActiveSprint] = useState(null);
  const [activeTask, setActiveTask] = useState(null);
  const [view, setView] = useState("overview");

  const totalTasks = SPRINTS.reduce((a, s) => a + s.tasks.length, 0);

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", maxWidth: 900, margin: "0 auto", padding: "2rem 1.5rem", color: "var(--color-text-primary, #1a1a1a)", background: "var(--color-background-primary, #fff)" }}>
      
      {/* Header */}
      <div style={{ borderBottom: "0.5px solid var(--color-border-tertiary, #e0e0e0)", paddingBottom: "1.5rem", marginBottom: "2rem" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 6 }}>
          <span style={{ fontSize: 11, letterSpacing: "0.08em", color: "var(--color-text-secondary, #666)", textTransform: "uppercase", fontWeight: 500 }}>UCR · CIOdD · Proyecto ED-3698</span>
        </div>
        <h1 style={{ fontSize: 26, fontWeight: 500, margin: "0 0 8px", lineHeight: 1.25 }}>
          Plan de implementación — Caja de Herramientas Docente
        </h1>
        <p style={{ fontSize: 14, color: "var(--color-text-secondary, #666)", margin: 0, lineHeight: 1.6 }}>
          Revisión crítica y mejora pedagógica de{" "}
          <a href="https://agmelendez.github.io/cajaherramientascolegios/" target="_blank" rel="noreferrer"
            style={{ color: "inherit", textDecoration: "underline" }}>
            agmelendez.github.io/cajaherramientascolegios
          </a>
          {" "}· {SPRINTS.length} sprints · {totalTasks} tareas · Basado en evaluación experta externa
        </p>
      </div>

      {/* View toggle */}
      <div style={{ display: "flex", gap: 8, marginBottom: "1.5rem" }}>
        {[["overview", "Vista general"], ["detail", "Detalle por sprint"], ["issues", "Hallazgos evaluadores"]].map(([key, label]) => (
          <button key={key} onClick={() => setView(key)}
            style={{ padding: "6px 14px", fontSize: 13, fontWeight: view === key ? 500 : 400, cursor: "pointer", borderRadius: 6, border: view === key ? "1.5px solid var(--color-border-primary, #aaa)" : "0.5px solid var(--color-border-tertiary, #e0e0e0)", background: view === key ? "var(--color-background-secondary, #f5f5f5)" : "transparent", color: "var(--color-text-primary, #1a1a1a)" }}>
            {label}
          </button>
        ))}
      </div>

      {/* OVERVIEW */}
      {view === "overview" && (
        <>
          {/* Summary stats */}
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(130px, 1fr))", gap: 10, marginBottom: "2rem" }}>
            {[
              ["5", "Sprints"],
              [totalTasks.toString(), "Tareas totales"],
              ["3", "Prioridad crítica/alta"],
              ["~9–14 días", "Estimado total"]
            ].map(([val, lab]) => (
              <div key={lab} style={{ background: "var(--color-background-secondary, #f8f8f8)", borderRadius: 10, padding: "14px 16px" }}>
                <div style={{ fontSize: 22, fontWeight: 500, lineHeight: 1 }}>{val}</div>
                <div style={{ fontSize: 12, color: "var(--color-text-secondary, #888)", marginTop: 4 }}>{lab}</div>
              </div>
            ))}
          </div>

          {/* Sprint cards */}
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {SPRINTS.map(sprint => {
              const pc = PRIORITY_COLORS[sprint.priority];
              return (
                <div key={sprint.id}
                  onClick={() => { setActiveSprint(activeSprint === sprint.id ? null : sprint.id); setView("detail"); }}
                  style={{ border: "0.5px solid var(--color-border-tertiary, #e0e0e0)", borderRadius: 10, padding: "16px 20px", cursor: "pointer", transition: "border-color 0.15s", display: "flex", alignItems: "flex-start", gap: 16 }}>
                  <div style={{ minWidth: 44, height: 44, borderRadius: 8, background: sprint.hex50, display: "flex", alignItems: "center", justifyContent: "center", fontWeight: 500, fontSize: 13, color: sprint.hex800, flexShrink: 0 }}>
                    {sprint.code}
                  </div>
                  <div style={{ flex: 1 }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap", marginBottom: 4 }}>
                      <span style={{ fontSize: 15, fontWeight: 500 }}>{sprint.label}</span>
                      <span style={{ fontSize: 11, padding: "2px 8px", borderRadius: 4, background: pc.bg, color: pc.text, border: `0.5px solid ${pc.border}` }}>{sprint.priority}</span>
                      <span style={{ fontSize: 11, color: "var(--color-text-secondary, #888)" }}>{sprint.duration} · {sprint.tasks.length} tareas</span>
                    </div>
                    <div style={{ fontSize: 13, color: "var(--color-text-secondary, #666)", lineHeight: 1.5 }}>
                      {sprint.issues[0]}
                    </div>
                  </div>
                  <span style={{ fontSize: 18, color: "var(--color-text-secondary, #aaa)", alignSelf: "center" }}>›</span>
                </div>
              );
            })}
          </div>

          {/* Orden sugerido de ejecución */}
          <div style={{ marginTop: "2rem", padding: "16px 20px", border: "0.5px solid var(--color-border-tertiary, #e0e0e0)", borderRadius: 10 }}>
            <div style={{ fontSize: 13, fontWeight: 500, marginBottom: 10 }}>Orden sugerido de ejecución</div>
            <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
              {["S1: Conceptual", "→", "S2: Bibliográfico", "→", "S3: Glosario", "→", "S4: Crítica", "→", "S5: Adaptación"].map((item, i) => (
                <span key={i} style={{
                  fontSize: 12,
                  padding: item === "→" ? "0 2px" : "5px 12px",
                  borderRadius: item === "→" ? 0 : 6,
                  background: item === "→" ? "transparent" : "var(--color-background-secondary, #f5f5f5)",
                  color: item === "→" ? "var(--color-text-secondary, #aaa)" : "var(--color-text-primary, #333)",
                  fontWeight: item === "→" ? 400 : 500
                }}>{item}</span>
              ))}
            </div>
            <p style={{ fontSize: 12, color: "var(--color-text-secondary, #777)", marginTop: 10, lineHeight: 1.6 }}>
              S1 y S2 son interdependientes: la corrección conceptual requiere simultáneamente la identificación de fuentes válidas. 
              S3 puede ejecutarse en paralelo con S2. S4 y S5 son iterativas y pueden continuar en versiones posteriores.
            </p>
          </div>
        </>
      )}

      {/* DETAIL */}
      {view === "detail" && (
        <div>
          {/* Sprint selector */}
          <div style={{ display: "flex", gap: 8, marginBottom: "1.5rem", flexWrap: "wrap" }}>
            {SPRINTS.map(s => (
              <button key={s.id} onClick={() => { setActiveSprint(s.id); setActiveTask(null); }}
                style={{ padding: "6px 14px", fontSize: 13, cursor: "pointer", borderRadius: 6, fontWeight: activeSprint === s.id ? 500 : 400, border: activeSprint === s.id ? `1.5px solid ${s.hex200}` : "0.5px solid var(--color-border-tertiary, #e0e0e0)", background: activeSprint === s.id ? s.hex50 : "transparent", color: activeSprint === s.id ? s.hex800 : "var(--color-text-primary, #333)" }}>
                {s.code}: {s.label.split(" ").slice(0, 2).join(" ")}
              </button>
            ))}
          </div>

          {SPRINTS.filter(s => !activeSprint || s.id === activeSprint).map(sprint => {
            const pc = PRIORITY_COLORS[sprint.priority];
            return (
              <div key={sprint.id} style={{ marginBottom: "2rem", border: "0.5px solid var(--color-border-tertiary, #e0e0e0)", borderRadius: 12, overflow: "hidden" }}>
                {/* Sprint header */}
                <div style={{ background: sprint.hex50, padding: "16px 20px", display: "flex", alignItems: "flex-start", gap: 14 }}>
                  <div style={{ fontSize: 20, fontWeight: 500, color: sprint.hex800, minWidth: 40 }}>{sprint.code}</div>
                  <div style={{ flex: 1 }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap", marginBottom: 4 }}>
                      <span style={{ fontSize: 16, fontWeight: 500, color: sprint.hex800 }}>{sprint.label}</span>
                      <span style={{ fontSize: 11, padding: "2px 8px", borderRadius: 4, background: pc.bg, color: pc.text, border: `0.5px solid ${pc.border}` }}>{sprint.priority}</span>
                      <span style={{ fontSize: 11, color: sprint.hex800, opacity: 0.7 }}>{sprint.duration}</span>
                    </div>
                    <div style={{ fontSize: 13, color: sprint.hex600, lineHeight: 1.5 }}>
                      <strong>Problemas que atiende:</strong> {sprint.issues.join("; ")}
                    </div>
                  </div>
                </div>

                {/* Tasks */}
                <div style={{ padding: "0 20px 16px" }}>
                  {sprint.tasks.map((task, ti) => {
                    const isOpen = activeTask === task.id;
                    return (
                      <div key={task.id} style={{ borderBottom: ti < sprint.tasks.length - 1 ? "0.5px solid var(--color-border-tertiary, #e8e8e8)" : "none", padding: "14px 0" }}>
                        <div onClick={() => setActiveTask(isOpen ? null : task.id)}
                          style={{ display: "flex", alignItems: "flex-start", gap: 12, cursor: "pointer" }}>
                          <span style={{ fontSize: 11, padding: "2px 8px", borderRadius: 4, background: sprint.hex50, color: sprint.hex800, fontWeight: 500, flexShrink: 0, marginTop: 1 }}>{task.id}</span>
                          <div style={{ flex: 1 }}>
                            <div style={{ fontSize: 14, fontWeight: 500 }}>{task.title}</div>
                            <div style={{ fontSize: 12, color: "var(--color-text-secondary, #777)", marginTop: 2 }}>
                              Archivo: <code style={{ fontSize: 11, background: "var(--color-background-secondary, #f5f5f5)", padding: "1px 5px", borderRadius: 3 }}>{task.file}</code>
                            </div>
                          </div>
                          <span style={{ fontSize: 16, color: "var(--color-text-secondary, #aaa)", transform: isOpen ? "rotate(90deg)" : "none", transition: "transform 0.2s" }}>›</span>
                        </div>
                        {isOpen && (
                          <div style={{ marginTop: 10, marginLeft: 60 }}>
                            <div style={{ fontSize: 13, lineHeight: 1.7, color: "var(--color-text-primary, #333)", padding: "10px 14px", background: "var(--color-background-secondary, #fafafa)", borderRadius: 8, marginBottom: 8 }}>
                              {task.detail}
                            </div>
                            <div style={{ display: "flex", alignItems: "flex-start", gap: 8 }}>
                              <span style={{ fontSize: 11, fontWeight: 500, color: sprint.hex800, marginTop: 2 }}>Entregable:</span>
                              <span style={{ fontSize: 13, color: "var(--color-text-secondary, #555)", lineHeight: 1.5 }}>{task.deliverable}</span>
                            </div>
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* ISSUES VIEW */}
      {view === "issues" && (
        <div>
          <div style={{ marginBottom: "1.5rem", padding: "14px 18px", background: "var(--color-background-secondary, #fafafa)", borderRadius: 8, border: "0.5px solid var(--color-border-tertiary, #e0e0e0)" }}>
            <p style={{ fontSize: 13, lineHeight: 1.7, color: "var(--color-text-secondary, #555)", margin: 0 }}>
              Síntesis de la evaluación externa recibida, organizada por eje de mejora. Cada hallazgo está vinculado a su sprint de respuesta correspondiente.
            </p>
          </div>

          {[
            {
              title: "Representación incorrecta de marcos pedagógicos (TPACK/SAMR)",
              sprint: "S1",
              detail: "TPACK se presenta con lógica lineal cuando es un modelo de conocimiento integrador e interseccional (Mishra & Koehler, 2006). SAMR se plantea como si pudiera desconectarse de lo disciplinar y pedagógico, cuando la crítica académica señala precisamente ese riesgo como su debilidad principal (Hamilton et al., 2016). Ambos modelos requieren explicitación de sus limitaciones y una presentación que no fomente el uso instrumental-tecnicista.",
              source: "S1-T1, S1-T2"
            },
            {
              title: "Ausencia del rol docente en la era IA como eje articulador",
              sprint: "S1",
              detail: "La plataforma no responde preguntas pedagógicamente cruciales: ¿para qué incorporar IA?, ¿desde qué concepción del aprendizaje?, ¿qué papel tiene la IA en cada etapa didáctica? Sin este anclaje, el contenido queda flotando en la dimensión instrumental y no en la profesional-docente. La pregunta por los aprendizajes precede siempre a la pregunta por las herramientas.",
              source: "S1-T3, S1-T4"
            },
            {
              title: "Infografías sin fuentes bibliográficas",
              sprint: "S2",
              detail: "La ausencia de fuentes en las infografías es un problema de integridad académica y de modelo para los docentes. El contenido de IA en Educación cita únicamente un video de YouTube como fuente. Para una plataforma UCR-CIOdD, el estándar mínimo es APA 7.ª ed. con referencias académicas verificables.",
              source: "S2-T1, S2-T2"
            },
            {
              title: "Lenguaje técnico no glosado para principiantes",
              sprint: "S3",
              detail: "Términos como IA simbólica, parámetros, red neuronal, arquitectura Transformer y token aparecen sin definición contextual en secciones dirigidas a docentes sin formación técnica (nivel 'Ninguna' o 'Básica'). El efecto es alienante y contradice el propósito declarado de la plataforma.",
              source: "S3-T1, S3-T2, S3-T3"
            },
            {
              title: "Sesgo de solucionismo tecnológico",
              sprint: "S4",
              detail: "El tono general favorece la adopción sin fricción crítica. Falta invitar al docente a pensar qué aporta la IA y qué es genuinamente irremplazable en su quehacer profesional. La perspectiva crítica no es un añadido opcional, sino la diferencia entre una plataforma de capacitación técnica y una de formación docente.",
              source: "S4-T1, S4-T2, S4-T3"
            },
            {
              title: "Interfaz de niveles no refleja diferenciación de contenido",
              sprint: "S5",
              detail: "El onboarding (3 preguntas) permite seleccionar nivel y modalidad, pero el contenido mostrado es idéntico independientemente de la selección. Esto invalida la promesa de personalización. Adicionalmente, la navegación libre entre módulos sin andamiaje puede generar experiencias fragmentadas, especialmente en usuarios principiantes.",
              source: "S5-T1, S5-T2, S5-T3, S5-T4"
            }
          ].map((issue, i) => {
            const sprint = SPRINTS.find(s => s.code === issue.sprint);
            return (
              <div key={i} style={{ marginBottom: 12, padding: "16px 20px", border: "0.5px solid var(--color-border-tertiary, #e0e0e0)", borderRadius: 10 }}>
                <div style={{ display: "flex", alignItems: "flex-start", gap: 10 }}>
                  <div style={{ minWidth: 36, padding: "3px 0", textAlign: "center", fontSize: 12, fontWeight: 500, color: sprint?.hex800, background: sprint?.hex50, borderRadius: 6, flexShrink: 0 }}>{issue.sprint}</div>
                  <div>
                    <div style={{ fontSize: 14, fontWeight: 500, marginBottom: 6 }}>{issue.title}</div>
                    <div style={{ fontSize: 13, color: "var(--color-text-secondary, #555)", lineHeight: 1.65, marginBottom: 6 }}>{issue.detail}</div>
                    <div style={{ fontSize: 11, color: "var(--color-text-secondary, #999)" }}>Tareas: {issue.source}</div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* Footer */}
      <div style={{ marginTop: "2.5rem", paddingTop: "1.5rem", borderTop: "0.5px solid var(--color-border-tertiary, #e0e0e0)", fontSize: 12, color: "var(--color-text-secondary, #999)", display: "flex", justifyContent: "space-between", flexWrap: "wrap", gap: 8 }}>
        <span>Plan de implementación · CIOdD-UCR / ED-3698 · 2026</span>
        <span>Elaborado a partir de evaluación externa experta · Mayo 2026</span>
      </div>
    </div>
  );
}
