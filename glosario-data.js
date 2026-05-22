// Base de datos conceptual para el Glosario de IA (UCR/CIOdD)
window.GLOSARIO_DATA = {
    "ia_simbolica": {
        "title": "IA Simbólica",
        "category": "Técnico",
        "simpleDef": "Inteligencia artificial basada en reglas lógicas rígidas escritas por programadores humanos, en lugar de aprender sola a partir de datos.",
        "analogy": "Es como un libro de recetas de cocina muy estricto: si sigues los pasos al pie de la letra, el resultado es siempre exacto; pero si falta un ingrediente o paso, el sistema colapsa y no sabe qué hacer.",
        "classroomExample": "Un programa interactivo de preguntas y respuestas donde el docente programó de antemano la respuesta correcta exacta; si el alumno escribe un sinónimo válido pero no previsto, el programa lo califica como incorrecto."
    },
    "red_neuronal": {
        "title": "Red Neuronal",
        "category": "Técnico",
        "simpleDef": "Un modelo matemático computacional inspirado en el cerebro humano que aprende a reconocer patrones complejos procesando grandes volúmenes de datos.",
        "analogy": "Imagina a un grupo de personas pasándose notas en una fila: cada una saca una conclusión simple del papel que le dio el compañero anterior y le pasa una nota resumida al siguiente, logrando resolver un enigma complejo al final.",
        "classroomExample": "El sistema informático de la biblioteca que sugiere un libro basándose en los patrones de lectura de miles de usuarios anteriores con gustos similares."
    },
    "llm": {
        "title": "LLM (Gran Modelo de Lenguaje)",
        "category": "Técnico",
        "simpleDef": "Un sistema de inteligencia artificial entrenado con billones de palabras para leer, predecir, traducir y generar texto con fluidez similar a la humana.",
        "analogy": "Es como un lector superdotado que ha leído casi todos los libros y páginas web de la historia humana y puede completar cualquier texto imitando el estilo exacto de lo que leyó.",
        "classroomExample": "Usar ChatGPT o Gemini para solicitar un borrador de carta de justificación para padres de familia, imitando un tono formal e institucional."
    },
    "token": {
        "title": "Token",
        "category": "Técnico",
        "simpleDef": "La porción mínima de texto (palabra, sílaba o carácter) en la cual la IA subdivide la información para poder procesarla y comprenderla matemáticamente.",
        "analogy": "Como las piezas individuales de un rompecabezas de palabras; la IA desarma todo lo que le escribes en estas fichas para poder contarlas y analizarlas numéricamente.",
        "classroomExample": "Entender por qué la IA tiene problemas para contar letras en palabras largas: no lee la palabra letra por letra, sino en estos bloques numéricos."
    },
    "parametros": {
        "title": "Parámetros",
        "category": "Técnico",
        "simpleDef": "Las variables internas o 'perillas' matemáticas que la IA ajusta durante su entrenamiento para aprender a conectar entradas con las respuestas adecuadas.",
        "analogy": "Como las perillas de ecualización en una consola de sonido gigante: ajustar cada perilla cambia sutilmente los agudos, graves o el balance de todo el audio final.",
        "classroomExample": "Reconocer que un modelo de 175 mil millones de parámetros tiene muchas más 'perillas' para matizar y refinar el tono de su respuesta que un modelo más pequeño."
    },
    "transformer": {
        "title": "Arquitectura Transformer",
        "category": "Técnico",
        "simpleDef": "El diseño de red neuronal profunda que permite a la IA analizar todas las palabras de una oración al mismo tiempo, comprendiendo su contexto inmediato.",
        "analogy": "Como un lector que mira la página entera de un solo golpe de vista en lugar de leer palabra por palabra con el dedo, comprendiendo la relación de cada término con el resto.",
        "classroomExample": "La capacidad de la IA para discernir correctamente si la palabra 'banco' se refiere a una entidad financiera o a un asiento de madera, analizando el resto del párrafo instantáneamente."
    },
    "ia_generativa": {
        "title": "IA Generativa",
        "category": "Técnico",
        "simpleDef": "Sistemas de IA enfocados en la creación de contenidos originales totalmente nuevos (como ensayos, imágenes, música o código) partiendo de indicaciones verbales.",
        "analogy": "Es como un artista extremadamente habilidoso que puede pintar un cuadro o escribir un poema en segundos basándose en una simple idea que le susurres al oído.",
        "classroomExample": "El docente que utiliza herramientas generativas para crear una imagen ilustrativa e inédita de un dinosaurio leyendo en Costa Rica para un material didáctico."
    },
    "prompt": {
        "title": "Prompt (Instrucción)",
        "category": "Pedagogía",
        "simpleDef": "La indicación, pregunta o contexto que un usuario le escribe a una herramienta de IA para obtener una respuesta o comportamiento específico.",
        "analogy": "Como la consigna clara y detallada que un docente le da a sus estudiantes en clase para guiar un proyecto, en lugar de darles instrucciones confusas y ambiguas.",
        "classroomExample": "Redactar una instrucción detallada pidiendo a la IA: 'Actúa como un profesor de colegio costarricense y diseña un examen de 5 preguntas sobre la campaña de 1856 para noveno año'."
    },
    "alucinacion": {
        "title": "Alucinación",
        "category": "Ética",
        "simpleDef": "El error que comete la IA al generar información plausible, bien redactada y con tono seguro, pero que es totalmente falsa o inventada.",
        "analogy": "Como un estudiante muy elocuente que no estudió para el examen e inventa con total seguridad teorías falsas y fechas lógicas para no dejar el espacio en blanco.",
        "classroomExample": "La IA que crea y cita una ley MEP inexistente o un autor ficticio al solicitarle referencias para una unidad de estudio."
    },
    "cadena_pensamiento": {
        "title": "Cadena de Pensamiento",
        "category": "Pedagogía",
        "simpleDef": "Técnica de prompting que le pide a la IA que desglose e ilustre su razonamiento paso a paso antes de dar su respuesta final, disminuyendo fallos de lógica.",
        "analogy": "Es idéntico a pedirle a un estudiante en su examen de matemática que muestre el procedimiento paso a paso en lugar de colocar únicamente el resultado final.",
        "classroomExample": "Agregar la frase 'Explica tu lógica paso a paso' al pedirle a la IA que resuelva un problema complejo de física de secundaria."
    },
    "capacidades_emergentes": {
        "title": "Capacidades Emergentes",
        "category": "Técnico",
        "simpleDef": "Habilidades complejas e inesperadas que aparecen en los sistemas de IA de manera espontánea tras alcanzar un tamaño inmenso, sin haber sido programadas para ello.",
        "analogy": "Como cuando miles de personas se mudan a una zona desierta y, de repente, de manera natural y sin un plan centralizado, surge una rica cultura comunitaria.",
        "classroomExample": "Descubrir que un modelo de IA entrenado solo para predecir texto de repente es capaz de traducir entre idiomas o resolver acertijos lógicos complejos."
    },
    "sesgo_algoritmico": {
        "title": "Sesgo Algorítmico",
        "category": "Ética",
        "simpleDef": "La repetición sistemática de prejuicios, discriminación o estereotipos humanos en los resultados de la IA, debido a los desbalances en los datos con los que fue entrenada.",
        "analogy": "Es como un niño pequeño que repite de manera natural los comentarios e ideas discriminatorias de los adultos a su alrededor sin entender el daño que causan.",
        "classroomExample": "Una herramienta generadora de imágenes que, al pedirle 'dibujar a un científico', siempre genera hombres de avanzada edad, reforzando estereotipos de género en el aula."
    },
    "entrenamiento": {
        "title": "Entrenamiento",
        "category": "Técnico",
        "simpleDef": "El proceso mediante el cual se alimenta a la red neuronal con volúmenes masivos de datos para que aprenda a relacionar entradas con respuestas y afine sus perillas matemáticas.",
        "analogy": "Como el entrenamiento de un portero de fútbol que practica parando miles de tiros desde todos los ángulos hasta que sus músculos reaccionan casi por reflejo.",
        "classroomExample": "Comprender que si una IA se entrenó con textos de internet que datan hasta el 2023, no tendrá 'memoria' ni conocimiento de acontecimientos educativos posteriores."
    },
    "temperatura": {
        "title": "Temperatura",
        "category": "Técnico",
        "simpleDef": "El parámetro ajustable que regula el grado de creatividad, originalidad y riesgo probabilístico de la respuesta que genera la IA.",
        "analogy": "Como ajustar el nivel de improvisación de un músico de jazz: a temperatura cero toca la partitura exacta sin salirse de la nota; a temperatura alta improvisa libremente.",
        "classroomExample": "Configurar la temperatura baja (0.2) para que la IA realice una traducción exacta y rígida, o temperatura alta (0.8) para pedirle lluvias de ideas creativas."
    },
    "ventana_contexto": {
        "title": "Ventana de Contexto",
        "category": "Técnico",
        "simpleDef": "El límite máximo de información (tokens) que la IA puede mantener activa en su memoria de corto plazo y recordar en un solo chat.",
        "analogy": "Es como el bloc de notas mental que tienes abierto mientras redactas: si el bloc se llena, debes archivar las primeras páginas para poder seguir escribiendo, olvidando detalles anteriores.",
        "classroomExample": "El docente que nota que la IA 'olvida' las instrucciones y rúbricas dadas al inicio de un chat muy largo, debido a que superó la capacidad de almacenamiento temporal."
    },
    "fine_tuning": {
        "title": "Ajuste Fino (Fine-Tuning)",
        "category": "Pedagogía",
        "simpleDef": "El re-entrenamiento especializado de un modelo de IA ya existente usando un conjunto de datos específico para convertirlo en experto de un área concreta.",
        "analogy": "Como un graduado de medicina general que realiza tres años de especialización en pediatría para dominar por completo el tratamiento de niños.",
        "classroomExample": "Entrenar a un modelo general con planes curriculares y circulares oficiales del MEP para crear un asistente exclusivo experto en normativas de secundaria de Costa Rica."
    },
    "multimodal": {
        "title": "Multimodal",
        "category": "Técnico",
        "simpleDef": "La habilidad de una IA para interpretar, procesar y relacionar simultáneamente múltiples formas de datos, como texto, imágenes, audio y video.",
        "analogy": "Como un profesor en clase que explica la fotosíntesis hablando, señalando un póster infográfico y mostrando una planta física a la vez.",
        "classroomExample": "Subir una foto de un mapa conceptual hecho a mano en la pizarra para que la IA lo analice, lo convierta en texto digital y redacte una rúbrica de evaluación."
    },
    "ingenieria_prompts": {
        "title": "Ingeniería de Prompts",
        "category": "Pedagogía",
        "simpleDef": "La práctica y el diseño metódico de instrucciones estructuradas para entablar la comunicación más efectiva posible con los modelos de IA.",
        "analogy": "Como aprender a formular excelentes preguntas pedagógicas en clase para guiar eficazmente el pensamiento de nuestros estudiantes.",
        "classroomExample": "Diseñar una plantilla estructurada de prompt (Contexto + Tarea + Formato + Restricciones) para que el cuerpo docente cree planificaciones uniformes."
    },
    "andamiaje_metacognitivo": {
        "title": "Andamiaje Metacognitivo",
        "category": "Pedagogía",
        "simpleDef": "Utilizar la IA no para obtener respuestas terminadas, sino como un andamio que impulsa al docente o estudiante a reflexionar sobre su propio aprendizaje.",
        "analogy": "Como las pistas y preguntas socráticas que hace un docente para que el estudiante resuelva el dilema, en lugar de arrebatarle el cuaderno y resolverlo por él.",
        "classroomExample": "Pedirle a la IA: 'Actúa como un estudiante de secundaria y debate mi explicación sobre el cambio climático, mostrándome contraargumentos para evaluar mi claridad didáctica'."
    },
    "ia_conexionista": {
        "title": "IA Conexionista",
        "category": "Técnico",
        "simpleDef": "Enfoque de la inteligencia artificial basado en aprender de la experiencia mediante conexiones probabilísticas dinámicas (redes neuronales), en lugar de reglas fijas.",
        "analogy": "Es como aprender español mudándose a Costa Rica y escuchando a los locales hablar diariamente, en lugar de memorizar las tablas de gramática de un libro de texto.",
        "classroomExample": "El corrector ortográfico moderno que sugiere palabras basándose en el contexto probable de la oración entera y no solo en un diccionario de reglas rígidas."
    }
};
