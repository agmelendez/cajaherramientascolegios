import os

workspace = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

with open(os.path.join(workspace, "modulo-6.html"), "r") as f:
    template = f.read()

def generate_module(mod_num, title, description, color, duration, sections):
    html = template
    # Replace basic info
    html = html.replace("<title>Módulo 6: Herramientas Especializadas - Caja de Herramientas</title>", f"<title>Módulo {mod_num}: {title} - Caja de Herramientas</title>")
    html = html.replace("Módulo 6", f"Módulo {mod_num}")
    html = html.replace(">Herramientas Especializadas<", f">{title}<")
    html = html.replace("48 minutos", duration)
    html = html.replace("Conozca las diferencias clave entre los principales motores de Inteligencia Artificial (ChatGPT, Gemini, Copilot, Claude) y descubra cuál es el más adecuado según la tarea pedagógica específica que necesite resolver.", description)
    
    # Replace colors
    html = html.replace("purple", color)
    
    # Extract the left column content and right column TOC
    # We will just find the markers and replace them
    
    import re
    
    # Left column content
    left_col_start = html.find('<div class="lg:col-span-3')
    left_col_end = html.find('<!-- Right Column: Sticky Navigation (TOC) -->')
    
    if left_col_start != -1 and left_col_end != -1:
        # Keep the wrapper div
        wrapper_start = html.find('>', left_col_start) + 1
        
        new_content = "\n"
        for i, sec in enumerate(sections):
            new_content += f'''                    <section id="s{i+1}" class="scroll-mt-24">
                        <h2>{i+1}. {sec['title']}</h2>
                        {sec['content']}
                    </section>\n\n'''
        
        html = html[:wrapper_start] + new_content + "                </div>\n\n                " + html[left_col_end:]
        
    # TOC content
    toc_start = html.find('<nav class="space-y-1 text-sm">')
    toc_end = html.find('</nav>', toc_start)
    
    if toc_start != -1 and toc_end != -1:
        nav_start = html.find('>', toc_start) + 1
        new_toc = "\n"
        for i, sec in enumerate(sections):
            new_toc += f'''                            <a href="#s{i+1}" class="toc-link block px-3 py-2 text-gray-500 hover:text-gray-900 hover:bg-gray-50 rounded-lg border-l-2 border-transparent transition-all">{i+1}. {sec['short_title']}</a>\n'''
        
        html = html[:nav_start] + new_toc + "                        " + html[toc_end:]

    with open(os.path.join(workspace, f"modulo-{mod_num}.html"), "w") as f:
        f.write(html)
    print(f"Generated modulo-{mod_num}.html")

mod7_sections = [
    {"title": "¿Para qué le sirve al docente técnico?", "short_title": "Utilidad en CTP", "content": "<p>Permite adaptar el conocimiento teórico a las necesidades prácticas de los talleres y especialidades técnicas. La IA puede ayudar a redactar manuales de seguridad, procedimientos paso a paso y escenarios de resolución de problemas reales.</p>"},
    {"title": "IA en el Taller", "short_title": "IA en el Taller", "content": "<p>Genere escenarios de simulación de fallas en maquinaria o procesos técnicos para que los estudiantes practiquen el diagnóstico sin riesgos físicos.</p>"},
    {"title": "Herramientas Sugeridas", "short_title": "Herramientas", "content": "<p>Claude es excelente para analizar manuales técnicos largos en inglés y extraer los puntos clave en español. Copilot es útil para buscar especificaciones actualizadas de equipos.</p>"},
    {"title": "Prompt base para CTP", "short_title": "Prompt base", "content": "<div class=\"bg-gray-900 text-gray-100 p-5 rounded-xl font-mono text-sm shadow-inner mb-4\">\"Crea un caso de estudio sobre una falla en un motor eléctrico trifásico para estudiantes de duodécimo año.\"</div>"},
    {"title": "Uso mejorado", "short_title": "Uso mejorado", "content": "<div class=\"bg-red-600 text-white p-5 rounded-xl font-mono text-sm shadow-lg shadow-red-500/20 mb-4\">\"Actúa como un experto en electromecánica. Crea un escenario realista donde un motor trifásico presenta sobrecalentamiento. Incluye 3 síntomas visibles y pide al estudiante que proponga un diagrama de diagnóstico paso a paso.\"</div>"},
    {"title": "Adaptación por especialidad", "short_title": "Especialidades", "content": "<p><strong>Agropecuaria:</strong> Modelos predictivos de clima y cosechas.<br><strong>Industrial:</strong> Simulaciones de control de calidad.<br><strong>Comercial:</strong> Casos de contabilidad y servicio al cliente.</p>"},
    {"title": "Seguridad Ocupacional", "short_title": "Seguridad", "content": "<p>Nunca permita que la IA dicte procedimientos de seguridad críticos sin revisión exhaustiva por parte del docente. La seguridad física en el taller no debe depender únicamente de recomendaciones generadas por IA.</p>"},
    {"title": "Ejemplo Aplicado", "short_title": "Ejemplo Aplicado", "content": "<p>Use Copilot para generar un cuestionario rápido de reglas de seguridad específicas para el uso del torno CNC antes de permitir que los estudiantes operen la máquina.</p>"},
    {"title": "Conexión con la Evaluación", "short_title": "Evaluación", "content": "<p>La IA puede generar rúbricas específicas para evaluar competencias procedimentales, definiendo claramente qué se espera en cada nivel de desempeño (Aún no competente, Competente, Sobresaliente).</p>"},
    {"title": "Evidencias para práctica", "short_title": "Evidencias", "content": "<p>Fomente que los estudiantes usen IA para documentar sus proyectos (ej. redactar la bitácora técnica), citando la herramienta utilizada.</p>"},
    {"title": "Versión Inclusiva (DUA)", "short_title": "Inclusión DUA", "content": "<p>Adapte los manuales técnicos complejos convirtiéndolos en resúmenes visuales o pasos simplificados para estudiantes con adecuaciones curriculares.</p>"},
    {"title": "Microreto de Autoformación", "short_title": "Microreto", "content": "<div class=\"bg-red-50 border border-red-200 rounded-xl p-6 text-center my-6\"><h4 class=\"text-lg font-bold text-red-700 mb-2\">Reto del Taller</h4><p class=\"text-gray-700 mb-4\">Pida a una IA que redacte un procedimiento de seguridad para su taller. Revíselo críticamente: ¿Qué omitió la IA? ¿Qué detalles locales (específicos de su colegio) debe agregar?</p></div>"},
    {"title": "Checklist Rápido", "short_title": "Checklist", "content": "<ul class=\"space-y-2 list-none pl-0\"><li class=\"flex items-center gap-3\"><input type=\"checkbox\" class=\"w-5 h-5 text-red-600 rounded\"><span>Reviso las medidas de seguridad generadas por IA.</span></li></ul>"},
    {"title": "Recursos Complementarios", "short_title": "Recursos", "content": "<ul><li><a href=\"#\" class=\"text-red-600 hover:underline font-medium\">Guía de prompts para Educación Técnica</a></li></ul>"},
    {"title": "Conclusión", "short_title": "Conclusión", "content": "<p>La IA es un asistente poderoso para el docente técnico, permitiendo dedicar menos tiempo a la redacción de materiales y más tiempo a la supervisión práctica.</p>"}
]

generate_module(7, "IA en Colegios Técnicos", "Estrategias específicas para aplicar Inteligencia Artificial en especialidades técnicas y talleres del CTP.", "red", "25 minutos", mod7_sections)

mod8_sections = [
    {"title": "El reto de la Andragogía", "short_title": "Andragogía", "content": "<p>Los jóvenes y adultos en IPEC y CINDEA tienen necesidades de aprendizaje directo, práctico y relevante para su vida laboral. La IA ayuda a personalizar el aprendizaje para estos contextos.</p>"},
    {"title": "Retroalimentación Rápida", "short_title": "Retroalimentación", "content": "<p>Utilice la IA para generar borradores de retroalimentación constructiva sobre los trabajos de los estudiantes, ahorrando tiempo valioso en modalidades nocturnas donde el tiempo es limitado.</p>"},
    {"title": "Adaptación de Materiales", "short_title": "Adaptación", "content": "<p>Pida a la IA que reescriba textos escolares con un tono más maduro y profesional, adecuado para adultos que retoman sus estudios.</p>"},
    {"title": "Prompt base", "short_title": "Prompt base", "content": "<div class=\"bg-gray-900 text-gray-100 p-5 rounded-xl font-mono text-sm shadow-inner mb-4\">\"Reescribe este texto sobre historia para un estudiante adulto.\"</div>"},
    {"title": "Uso mejorado", "short_title": "Uso mejorado", "content": "<div class=\"bg-teal-600 text-white p-5 rounded-xl font-mono text-sm shadow-lg shadow-teal-500/20 mb-4\">\"Reescribe este concepto de educación cívica enfocándolo en cómo afecta la vida laboral y familiar de un adulto trabajador en Costa Rica, manteniendo un tono respetuoso y profesional.\"</div>"},
    {"title": "Simulaciones Laborales", "short_title": "Simulaciones", "content": "<p>Cree simulaciones de entrevistas de trabajo o redacción de correos profesionales para que los estudiantes practiquen habilidades blandas.</p>"},
    {"title": "Horarios Flexibles", "short_title": "Horarios", "content": "<p>La IA puede ayudar a crear planes de estudio modulares y flexibles que los estudiantes adultos puedan seguir a su propio ritmo.</p>"},
    {"title": "Ejemplo Aplicado", "short_title": "Ejemplo Aplicado", "content": "<p>Un estudiante entrega un ensayo. El docente usa IA para identificar rápidamente los 2 errores gramaticales más comunes y genera ejercicios específicos solo para esos errores.</p>"},
    {"title": "Evaluación Formativa", "short_title": "Evaluación Formativa", "content": "<p>Implemente quizzes cortos generados por IA que los estudiantes puedan hacer desde sus teléfonos móviles en sus tiempos libres (ej. en el autobús).</p>"},
    {"title": "Consideraciones de Privacidad", "short_title": "Privacidad", "content": "<p>Al usar IA para analizar trabajos de los estudiantes, asegúrese de anonimizar los datos y no incluir información personal.</p>"},
    {"title": "Motivación y Retención", "short_title": "Motivación", "content": "<p>Genere mensajes motivacionales personalizados para estudiantes que han faltado a lecciones debido a compromisos laborales.</p>"},
    {"title": "Microreto de Autoformación", "short_title": "Microreto", "content": "<div class=\"bg-teal-50 border border-teal-200 rounded-xl p-6 text-center my-6\"><h4 class=\"text-lg font-bold text-teal-700 mb-2\">Reto de Contextualización</h4><p class=\"text-gray-700 mb-4\">Tome un tema de su currículo y pida a la IA que lo explique usando analogías del ámbito de la construcción o del comercio minorista.</p></div>"},
    {"title": "Checklist Rápido", "short_title": "Checklist", "content": "<ul class=\"space-y-2 list-none pl-0\"><li class=\"flex items-center gap-3\"><input type=\"checkbox\" class=\"w-5 h-5 text-teal-600 rounded\"><span>Uso un tono andragógico (adulto) en los prompts.</span></li></ul>"},
    {"title": "Recursos Complementarios", "short_title": "Recursos", "content": "<ul><li><a href=\"#\" class=\"text-teal-600 hover:underline font-medium\">Plantillas de retroalimentación para jóvenes y adultos</a></li></ul>"},
    {"title": "Conclusión", "short_title": "Conclusión", "content": "<p>La IA permite una educación más empática y ajustada a la compleja realidad del estudiante adulto.</p>"}
]

generate_module(8, "Jóvenes y Adultos", "Cómo utilizar la IA para dar retroalimentación rápida a estudiantes de IPEC y CINDEA en modalidades nocturnas.", "teal", "12 minutos", mod8_sections)

mod9_sections = [
    {"title": "¿Qué es un Micro-Prompt?", "short_title": "¿Qué es?", "content": "<p>Un micro-prompt es una instrucción extremadamente corta (1-2 líneas) diseñada para generar ideas rápidas cuando el docente tiene muy poco tiempo. No produce materiales finales, sino chispas de inspiración.</p>"},
    {"title": "Estructura del Micro-Prompt", "short_title": "Estructura", "content": "<p>Verbo de acción + Tema + Audiencia. Ejemplo: \"Lista 5 ideas para enseñar fracciones a niños de 8 años de forma lúdica\".</p>"},
    {"title": "Generación de Rompehielos", "short_title": "Rompehielos", "content": "<p>\"Dame 3 preguntas rompehielos sobre [Tema] para adolescentes.\"</p>"},
    {"title": "Cierres de Clase (Tickets de Salida)", "short_title": "Cierres", "content": "<p>\"Genera 2 preguntas de reflexión final sobre [Tema de la clase].\"</p>"},
    {"title": "Ideas de Proyectos Rápidos", "short_title": "Proyectos", "content": "<p>\"Sugiere un proyecto de 1 semana donde estudiantes de noveno apliquen [Concepto] usando materiales reciclados.\"</p>"},
    {"title": "Ejemplos de la Vida Real", "short_title": "Ejemplos", "content": "<p>\"Dame una analogía de la vida cotidiana en Costa Rica para explicar [Concepto complejo].\"</p>"},
    {"title": "Variación de Ejercicios", "short_title": "Ejercicios", "content": "<p>\"Crea 3 variaciones de este problema matemático con diferente nivel de dificultad: [Problema base].\"</p>"},
    {"title": "Rúbricas de un solo punto", "short_title": "Rúbricas", "content": "<p>\"Escribe los 3 criterios indispensables que debe tener un ensayo sobre [Tema].\"</p>"},
    {"title": "Asegurando la Ética", "short_title": "Ética", "content": "<p>Incluso en micro-prompts, recuerde revisar los sesgos. La brevedad del prompt a menudo hace que la IA asuma estereotipos. Siempre lea críticamente el resultado.</p>"},
    {"title": "El límite del Micro-Prompt", "short_title": "Límites", "content": "<p>No use micro-prompts cuando necesite planeamientos detallados, rúbricas formales o documentos oficiales. Para eso, use la técnica de \"Uso mejorado\" (prompts estructurados).</p>"},
    {"title": "Integración Diaria", "short_title": "Integración", "content": "<p>Tenga la aplicación de IA abierta en su celular o computadora y úsela en los 5 minutos antes de que empiece la lección para buscar esa última idea brillante.</p>"},
    {"title": "Microreto de Autoformación", "short_title": "Microreto", "content": "<div class=\"bg-pink-50 border border-pink-200 rounded-xl p-6 text-center my-6\"><h4 class=\"text-lg font-bold text-pink-700 mb-2\">Reto del Minuto</h4><p class=\"text-gray-700 mb-4\">Tómese 60 segundos. Escriba 3 micro-prompts distintos para su próxima clase y vea cuál genera la mejor idea.</p></div>"},
    {"title": "Checklist Rápido", "short_title": "Checklist", "content": "<ul class=\"space-y-2 list-none pl-0\"><li class=\"flex items-center gap-3\"><input type=\"checkbox\" class=\"w-5 h-5 text-pink-600 rounded\"><span>Uso micro-prompts solo para inspiración, no para productos finales.</span></li></ul>"},
    {"title": "Recursos Complementarios", "short_title": "Recursos", "content": "<ul><li><a href=\"#\" class=\"text-pink-600 hover:underline font-medium\">Banco de 50 Micro-Prompts Docentes</a></li></ul>"},
    {"title": "Conclusión", "short_title": "Conclusión", "content": "<p>Los micro-prompts son la herramienta de agilidad por excelencia del docente moderno: mínimo esfuerzo de entrada, máxima inspiración de salida.</p>"}
]

generate_module(9, "Micro-Prompts", "Colección de prompts ultracortos para generar ideas de clase en menos de 1 minuto asegurando ética.", "pink", "8 minutos", mod9_sections)

print("All modules generated successfully.")
