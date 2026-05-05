import re

with open("index.html", "r") as f:
    content = f.read()

# We need everything up to <main class="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 overflow-y-auto">
top_split = '<main class="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 overflow-y-auto">'
parts = content.split(top_split)
top_boilerplate = parts[0] + top_split + "\n"

# We need everything from </main>
bottom_split = '</main>'
bottom_boilerplate = "\n" + bottom_split + parts[1].split(bottom_split)[1]

pages = {
    "ia-educacion.html": {
        "title": "🧠 IA en Educación: Qué sí hace y qué no hace",
        "description": "Bajar el miedo, aclarar expectativas y alinear el uso de IA con la Guía Oficial MEP 2026.",
        "content_text": """
  La Inteligencia Artificial es una herramienta que aprende patrones y ayuda a procesar información, pero <strong>requiere criterio pedagógico humano</strong>. Según la Guía MEP 2026, la IA sirve para ampliar la mediación pedagógica, nunca para reemplazarla.
  
  <br><br><strong class="text-xl">✅ Qué SÍ puede hacer la IA:</strong>
  <ul class="list-disc pl-5 mt-3 mb-6 text-gray-700 space-y-2">
    <li>Generar múltiples ejemplos y opciones didácticas de forma instantánea.</li>
    <li>Personalizar materiales y actividades según el nivel y necesidades del estudiante.</li>
    <li>Ahorrar tiempo significativo en tareas administrativas, resúmenes y trabajo repetitivo.</li>
    <li>Automatizar estrategias de retroalimentación formativa inicial.</li>
    <li>Explicar conceptos complejos de múltiples formas o analogías.</li>
  </ul>
  
  <strong class="text-xl">❌ Qué NO puede hacer la IA:</strong>
  <ul class="list-disc pl-5 mt-3 mb-6 text-gray-700 space-y-2">
    <li>Pensar por el docente o elegir por el estudiante.</li>
    <li>Reemplazar el juicio pedagógico y conocimiento del contexto de aula.</li>
    <li>Sustituir la empatía y la relación humana fundamental para el aprendizaje.</li>
    <li>Garantizar la verdad absoluta (es propensa a "alucinar" o inventar hechos).</li>
    <li>Proteger automáticamente datos sensibles de estudiantes.</li>
  </ul>
  
  <div class="bg-blue-50 border-l-4 border-mep-blue p-6 mt-6 rounded-r-lg">
    <p class="font-bold text-gray-900 text-lg mb-2">🎯 REGLA DE ORO</p>
    <p class="text-gray-700">La IA se utiliza para <strong>ampliar</strong>, nunca para <strong>reemplazar</strong> la mediación pedagógica y el vínculo humano.</p>
  </div>
"""
    },
    "privacidad-etica.html": {
        "title": "🔒 Privacidad, Ética y Verificación",
        "description": "Principios fundamentales para un uso seguro y responsable de la IA, cuidando a nuestros estudiantes y nuestra práctica docente.",
        "content_text": """
  El uso de la IA conlleva una gran responsabilidad. Es vital proteger los datos personales, entender las implicaciones éticas y mitigar riesgos asociados a herramientas generativas, tal como lo exige el marco regulatorio.
  <br><br>
  <strong class="text-xl">✋ 5 Cuidados Antes de Usar IA en Clase:</strong>
  <ul class="list-decimal pl-5 mt-3 mb-6 text-gray-700 space-y-3">
    <li><strong>Verifica información importante:</strong> La IA "alucina" hechos falsos que suenan reales. Nunca copies una respuesta sin verificar en fuentes confiables o contrastar los datos.</li>
    <li><strong>Protege datos de menores de edad:</strong> NUNCA ingreses nombres, apellidos, calificaciones o datos médicos a un chatbot. Usa descripciones genéricas (ej. "estudiante de nivel inicial con dificultad lectora").</li>
    <li><strong>Sabe qué herramienta usas:</strong> Asegúrate de conocer las políticas de privacidad de la herramienta. Prefiere entornos seguros institucionales (como Google Workspace for Education).</li>
    <li><strong>Sé transparente:</strong> Cuéntale al grupo cuando estás usando IA, para qué la usas y cómo funciona el proceso de verificación.</li>
    <li><strong>Distingue apoyo de plagio:</strong> El uso es válido si fomenta el aprendizaje, es transparente y validado. Copiar sin entender, y además ocultarlo, es inaceptable.</li>
  </ul>
  
  <div class="bg-green-50 border-l-4 border-mep-green p-6 mt-6 rounded-r-lg">
    <p class="font-bold text-gray-900 text-lg mb-2">⚠️ Riesgos Comunes que Debes Vigilar</p>
    <p class="text-gray-700 mb-2"><strong>Alucinaciones:</strong> Hechos inventados o citas inexistentes presentadas con total seguridad. ¡Siempre contrasta la información clave!</p>
    <p class="text-gray-700"><strong>Sesgos:</strong> Respuestas que reflejan prejuicios de los datos de entrenamiento (ej. falta de diversidad en ejemplos profesionales). El docente debe aportar la corrección y diversificación.</p>
  </div>
"""
    },
    "prompts-efectivos.html": {
        "title": "💬 Prompts Efectivos",
        "description": "Domina el arte de comunicarte con la IA aplicando el Método 4P para obtener los mejores resultados pedagógicos.",
        "content_text": """
  Un 'prompt' es la instrucción o petición que le damos a la Inteligencia Artificial. Un prompt vago genera respuestas inútiles; un prompt estructurado genera materiales listos para llevar al aula.
  <br><br>
  <strong class="text-xl">📝 La Fórmula: El Método 4P</strong>
  <p class="text-gray-600 mt-2 mb-4">Para pasar de un simple "dame una actividad" a un resultado espectacular, asegura incluir estos elementos:</p>
  
  <ul class="list-disc pl-5 mt-2 mb-6 text-gray-700 space-y-4">
    <li>
      <strong>PROPÓSITO (Rol y Contexto):</strong> Define quién eres y el contexto. 
      <br><span class="text-sm text-gray-500 italic">Ejemplo: "Soy docente de primaria, especialidad matemáticas, para 2° grado de una zona urbana."</span>
    </li>
    <li>
      <strong>PARÁMETROS (Restricciones):</strong> Establece el nivel cognitivo, duración y particularidades del estudiante. 
      <br><span class="text-sm text-gray-500 italic">Ejemplo: "...necesito una actividad introductoria de 15 minutos para niños con déficit atencional."</span>
    </li>
    <li>
      <strong>PRODUCTO (Formato esperado):</strong> Especifica exactamente cómo quieres la respuesta. 
      <br><span class="text-sm text-gray-500 italic">Ejemplo: "...presenta el resultado en formato de lista de pasos numerados con viñetas."</span>
    </li>
    <li>
      <strong>PRECISIÓN (Detalles extra):</strong> Añade materiales a utilizar, enfoques didácticos o metodologías específicas. 
      <br><span class="text-sm text-gray-500 italic">Ejemplo: "...utilizando únicamente material manipulable como tapas de botellas o fichas."</span>
    </li>
  </ul>
  
  <div class="bg-orange-50 border-l-4 border-mep-orange p-6 mt-6 rounded-r-lg">
    <p class="font-bold text-gray-900 text-lg mb-2">🔄 La Magia está en Iterar</p>
    <p class="text-gray-700">Si la primera respuesta no es lo que esperabas, ¡no te rindas! Interactúa con la IA dándole retroalimentación: pídele que lo haga <em>"más simple"</em>, <em>"añade más ejemplos locales"</em> o <em>"enfócalo en el trabajo colaborativo"</em>. Cada seguimiento mejora drásticamente la calidad.</p>
  </div>
"""
    }
}

for filename, data in pages.items():
    main_content = f"""
            <!-- Page Header -->
            <div class="mb-10 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                <div>
                    <div class="flex items-center gap-3 mb-2">
                        <a href="index.html" class="text-gray-400 hover:text-mep-blue transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                            </svg>
                        </a>
                        <h1 class="text-3xl font-bold text-gray-900">{data['title']}</h1>
                    </div>
                    <p class="text-gray-600 ml-9">{data['description']}</p>
                </div>
            </div>

            <!-- Content Section -->
            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none">
                    <div class="text-lg text-gray-700 leading-relaxed mb-6">{data['content_text']}</div>
                </div>
            </div>

            <!-- Comenzar Ahora Section -->
            <div class="bg-gray-50 rounded-2xl border border-gray-200 p-6 lg:p-10">
                <div class="flex items-center gap-3 mb-6">
                    <span class="text-2xl">🚀</span>
                    <h2 class="text-2xl font-bold text-gray-900">Comenzar Ahora</h2>
                </div>
                <p class="text-gray-600 mb-8">Accede directamente a los módulos que abordan estos contenidos a profundidad:</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <a href="modulo-1.html" class="block p-6 border border-blue-100 rounded-xl bg-white hover:bg-blue-50 hover:shadow-md transition-all group">
                        <div class="text-mep-blue mb-3">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                            </svg>
                        </div>
                        <h4 class="font-bold text-gray-900 mb-2 group-hover:text-mep-blue transition-colors">Módulo 1</h4>
                        <p class="text-sm text-gray-600">Fundamentos de IA y conceptos clave para docentes.</p>
                    </a>
                    
                    <a href="modulo-2.html" class="block p-6 border border-green-100 rounded-xl bg-white hover:bg-green-50 hover:shadow-md transition-all group">
                        <div class="text-mep-green mb-3">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                            </svg>
                        </div>
                        <h4 class="font-bold text-gray-900 mb-2 group-hover:text-mep-green transition-colors">Módulo 2</h4>
                        <p class="text-sm text-gray-600">Herramientas prácticas para el aula y sus usos.</p>
                    </a>
                    
                    <a href="modulo-3.html" class="block p-6 border border-orange-100 rounded-xl bg-white hover:bg-orange-50 hover:shadow-md transition-all group">
                        <div class="text-mep-orange mb-3">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                            </svg>
                        </div>
                        <h4 class="font-bold text-gray-900 mb-2 group-hover:text-mep-orange transition-colors">Módulo 3</h4>
                        <p class="text-sm text-gray-600">Aplicaciones avanzadas, evaluación y lineamientos éticos.</p>
                    </a>
                </div>
                
                <div class="mt-8 text-center">
                    <a href="modulos.html" class="inline-flex items-center gap-2 px-6 py-3 bg-white border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-colors">
                        Explorar todos los módulos de la malla
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
                        </svg>
                    </a>
                </div>
            </div>
"""
    with open(filename, "w") as f:
        f.write(top_boilerplate + main_content + bottom_boilerplate)
