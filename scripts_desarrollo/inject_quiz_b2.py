#!/usr/bin/env python3
"""B-2: Inject quiz/autoevaluación block into modules 1-9."""
import os

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quiz data per module: list of (question, [options], correct_index, explanation)
QUIZZES = {
    1: [
        ("¿Qué hace realmente la IA Generativa cuando produce un texto?",
         ["Busca la respuesta exacta en internet", "Predice la siguiente palabra más probable", "Copia fragmentos de documentos existentes", "Piensa como un ser humano"],
         1, "La IA Generativa es un motor predictivo de lenguaje: calcula la palabra más probable a continuación, no 'piensa' ni 'busca' como un humano."),
        ("¿Cuál es el principal riesgo al usar IA para generar datos históricos?",
         ["Que el texto sea muy largo", "Que 'alucine' datos falsos con gran elocuencia", "Que use un idioma incorrecto", "Que no tenga acceso a internet"],
         1, "Las 'alucinaciones' son uno de los riesgos más graves: la IA inventa hechos, fechas y citas con total seguridad."),
        ("¿Cuál es la mejor práctica al redactar un prompt para IA?",
         ["Ser lo más breve posible", "Dar contexto: rol, formato, audiencia y tono", "Copiar y pegar preguntas de examen", "Dejar que la IA decida todo"],
         1, "Un buen prompt incluye contexto claro (rol, formato, audiencia, tono) para obtener resultados útiles y relevantes."),
    ],
    2: [
        ("¿Qué datos de estudiantes NUNCA deben ingresarse en herramientas de IA de terceros?",
         ["Temas generales del currículo", "Nombres, cédulas y calificaciones", "Estrategias pedagógicas genéricas", "Nombres de asignaturas"],
         1, "Los datos personales de menores (nombres, cédulas, calificaciones, datos médicos) están protegidos por la Ley 8968 y nunca deben ingresarse en chatbots externos."),
        ("¿Qué son los 'sesgos' en la IA?",
         ["Errores de ortografía en las respuestas", "Prejuicios reflejados desde los datos de entrenamiento", "Problemas de conexión a internet", "Limitaciones de idioma"],
         1, "Los sesgos son prejuicios heredados de los datos de entrenamiento que pueden reflejar falta de diversidad o estereotipos."),
        ("¿Cuál es la diferencia entre uso válido de IA y plagio?",
         ["No hay diferencia", "El uso válido es transparente, fomenta aprendizaje y es validado", "Solo es plagio si se copia todo el texto", "Depende de la herramienta utilizada"],
         1, "El uso es válido cuando es transparente, fomenta el aprendizaje y el resultado es verificado por el docente. Copiar sin entender ni declarar es inaceptable."),
    ],
    3: [
        ("¿Qué es la técnica de 'cadena de pensamiento' (Chain of Thought) en prompting?",
         ["Escribir prompts muy largos", "Pedir a la IA que explique su razonamiento paso a paso", "Encadenar varias herramientas de IA", "Usar IA para generar más prompts"],
         1, "La cadena de pensamiento pide a la IA que muestre su razonamiento paso a paso, mejorando la calidad y verificabilidad de las respuestas."),
        ("¿Para qué sirve especificar un 'rol' al inicio de un prompt?",
         ["Para que la IA cambie de idioma", "Para contextualizar el tono, vocabulario y enfoque de la respuesta", "Para activar funciones premium", "No tiene ningún efecto real"],
         1, "Asignar un rol (ej. 'Actúa como profesor de primaria en Costa Rica') contextualiza el tono, vocabulario y nivel de la respuesta."),
        ("¿Qué debe hacer el docente SIEMPRE después de recibir una respuesta de IA?",
         ["Publicarla inmediatamente", "Verificar la información y adaptarla a su contexto", "Pedir una segunda opinión a otra IA", "Borrar el historial de chat"],
         1, "El docente debe siempre verificar, contrastar y adaptar cualquier contenido generado por IA antes de usarlo."),
    ],
    4: [
        ("¿Cuál es la principal ventaja de Google Gemini para docentes MEP?",
         ["Es la IA más avanzada del mercado", "Se integra nativamente con Google Workspace (Docs, Drive)", "Es la única IA gratuita", "Puede calificar exámenes automáticamente"],
         1, "Gemini se integra con el ecosistema de Google Workspace utilizado frecuentemente por cuentas MEP, facilitando el flujo de trabajo docente."),
        ("¿Qué herramienta es más adecuada para crear presentaciones educativas con IA?",
         ["Solo ChatGPT", "Herramientas como Gamma, Canva con IA o Google Slides + Gemini", "Microsoft Paint", "Editores de código"],
         1, "Herramientas como Gamma, Canva con IA y Google Slides integrado con Gemini permiten crear presentaciones educativas de forma eficiente."),
        ("¿Qué debe considerar un docente antes de adoptar una nueva herramienta de IA?",
         ["Solo el precio", "Privacidad, políticas de datos, utilidad pedagógica y accesibilidad", "La popularidad en redes sociales", "Que sea la más reciente"],
         1, "Antes de adoptar cualquier herramienta, el docente debe evaluar sus políticas de privacidad, utilidad pedagógica real y accesibilidad para su contexto."),
    ],
    5: [
        ("¿Cómo puede la IA ayudar en la diferenciación pedagógica?",
         ["Reemplazando al docente en clase", "Generando variantes de un mismo contenido adaptadas a distintos niveles", "Calificando automáticamente a los estudiantes", "Creando exámenes idénticos para todos"],
         1, "La IA permite generar versiones de un contenido adaptadas a diferentes niveles de comprensión, apoyando la diferenciación según el DUA."),
        ("¿Cuál es un ejemplo apropiado de uso de IA en evaluación formativa?",
         ["Que la IA califique los exámenes finales", "Generar rúbricas y retroalimentación formativa personalizada", "Dejar que los estudiantes usen IA en el examen", "Automatizar toda la evaluación"],
         1, "La IA puede ayudar a diseñar rúbricas claras y generar retroalimentación formativa que el docente revisa y personaliza."),
        ("¿Qué principio del DUA se fortalece más directamente con el uso de IA?",
         ["Principio de acción y expresión únicamente", "Principio de representación: múltiples formas de presentar la información", "Principio de motivación solamente", "Ninguno"],
         1, "El Principio I del DUA (proveer múltiples formas de representación) se fortalece al poder transformar textos a diferentes formatos y niveles de complejidad."),
    ],
    6: [
        ("¿Para qué puede usar un docente la IA en el análisis de datos educativos?",
         ["Para manipular calificaciones", "Para identificar patrones de rendimiento y generar visualizaciones", "Para reemplazar el juicio profesional", "Para comparar estudiantes entre sí"],
         1, "La IA puede ayudar a identificar patrones de rendimiento grupal y generar gráficos, siempre complementando (nunca reemplazando) el criterio profesional."),
        ("¿Qué precaución es fundamental al analizar datos de rendimiento con IA?",
         ["Usar la versión más cara de la herramienta", "No ingresar datos personales identificables de estudiantes", "Analizar todos los datos disponibles sin filtrar", "Compartir los resultados en redes sociales"],
         1, "Nunca se deben ingresar datos personales identificables. Use datos agregados o anonimizados para proteger la privacidad estudiantil."),
        ("¿Qué tipo de visualización puede solicitar a la IA para presentar resultados?",
         ["Solo texto plano", "Gráficos de barras, tablas comparativas, diagramas de tendencia", "Solo capturas de pantalla", "Documentos PDF únicamente"],
         1, "La IA puede generar descripciones de gráficos, tablas y diagramas que facilitan la presentación de datos a colegas y padres de familia."),
    ],
    7: [
        ("¿Qué son las herramientas especializadas de IA en educación?",
         ["Las más caras del mercado", "Herramientas diseñadas para tareas pedagógicas específicas como evaluación o planificación", "Herramientas que solo usan expertos en tecnología", "Versiones premium de ChatGPT"],
         1, "Son herramientas enfocadas en tareas pedagógicas concretas, como generación de rúbricas, planificación didáctica o creación de material adaptado."),
        ("¿Cuál es la ventaja de usar NotebookLM de Google para docentes?",
         ["Reemplaza la planificación docente", "Permite analizar documentos propios sin enviar datos a servidores externos de entrenamiento", "Es la herramienta más rápida", "Genera exámenes automáticamente"],
         1, "NotebookLM permite trabajar con documentos propios dentro del ecosistema Google, manteniendo mayor control sobre los datos."),
        ("¿Qué criterio es prioritario al elegir una herramienta especializada?",
         ["Que sea gratuita", "Que cumpla con estándares de privacidad y se alinee con objetivos pedagógicos", "Que sea la más popular", "Que tenga la interfaz más atractiva"],
         1, "La prioridad es que la herramienta cumpla estándares de privacidad (especialmente con datos de menores) y se alinee con los objetivos pedagógicos del docente."),
    ],
    8: [
        ("¿Cómo puede la IA apoyar la formación técnica profesional en un CTP?",
         ["Reemplazando las prácticas de taller", "Generando guías de procedimientos, manuales técnicos y simulaciones paso a paso", "Evaluando habilidades prácticas automáticamente", "Eliminando la necesidad de instructores"],
         1, "La IA puede generar documentación técnica, guías paso a paso y materiales de apoyo que complementan la formación práctica presencial."),
        ("¿Qué adaptación específica necesitan los prompts para educación técnica?",
         ["Deben ser más cortos", "Deben incluir vocabulario técnico específico de la especialidad y contexto del taller", "No necesitan adaptación", "Deben evitar términos técnicos"],
         1, "Los prompts para CTP deben incluir el vocabulario y contexto técnico específico de la especialidad para obtener resultados relevantes y precisos."),
        ("¿Cuál es la limitación más importante de la IA en la educación técnica?",
         ["No puede generar texto en español", "No puede reemplazar la práctica presencial ni la supervisión de seguridad en taller", "No funciona sin internet", "Solo sirve para materias teóricas"],
         1, "La IA no sustituye la práctica presencial, la supervisión de seguridad ni el desarrollo de habilidades manuales que requieren experiencia directa."),
    ],
    9: [
        ("¿Qué característica especial tiene la población de IPEC/CINDEA?",
         ["Son todos menores de edad", "Son personas jóvenes y adultas que combinan estudio con trabajo y responsabilidades familiares", "No necesitan adaptaciones", "Solo estudian presencialmente"],
         1, "La población IPEC/CINDEA incluye jóvenes y adultos que trabajan y tienen responsabilidades familiares, requiriendo comunicaciones concisas y horarios flexibles."),
        ("¿Cómo debe adaptarse el tono de las comunicaciones generadas con IA para esta población?",
         ["Usar lenguaje infantil y sencillo", "Usar un tono respetuoso, directo y profesional, reconociendo su experiencia de vida", "Usar un tono académico formal", "No hay necesidad de adaptarlo"],
         1, "El tono debe ser respetuoso, directo y profesional, reconociendo que son personas adultas con experiencia de vida valiosa."),
        ("¿Qué estrategia de IA es más útil para docentes de educación de adultos?",
         ["Generar contenido extenso y detallado", "Crear resúmenes concisos, materiales autoexplicativos y comunicaciones directas al punto", "Usar solo herramientas avanzadas", "Automatizar toda la interacción"],
         1, "Para adultos que trabajan, los materiales deben ser concisos, autoexplicativos y directos, maximizando el valor del tiempo limitado de estudio."),
    ],
}

QUIZ_TEMPLATE = '''
            <!-- ═══════════════════════════════════════════ -->
            <!-- Autoevaluación del Módulo {mod_num} -->
            <!-- ═══════════════════════════════════════════ -->
            <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6 sm:p-10 mt-8" id="quiz-section-{mod_num}">
                <div class="flex items-center gap-3 mb-6 border-b border-gray-100 pb-4">
                    <span class="text-2xl">📝</span>
                    <h2 class="text-2xl font-bold text-gray-900 m-0">Autoevaluación del Módulo {mod_num}</h2>
                </div>
                <p class="text-gray-600 mb-6">Responda las siguientes preguntas para verificar su comprensión. Sus resultados se guardan localmente en su navegador.</p>

                <div id="quiz-container-{mod_num}">
{questions_html}
                    <!-- Botón de envío -->
                    <div class="text-center mt-8">
                        <button onclick="evaluarQuiz({mod_num})" id="quiz-submit-{mod_num}" class="px-8 py-3 bg-mep-blue hover:bg-blue-600 text-white font-bold rounded-xl shadow-lg shadow-blue-500/30 transition-all hover:-translate-y-1">
                            Verificar Respuestas
                        </button>
                    </div>

                    <!-- Resultado -->
                    <div id="quiz-result-{mod_num}" class="hidden mt-6 p-6 rounded-xl text-center"></div>

                    <!-- Botón reintentar (oculto inicialmente) -->
                    <div id="quiz-retry-{mod_num}" class="hidden text-center mt-4">
                        <button onclick="reintentarQuiz({mod_num})" class="px-6 py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium rounded-lg transition-colors">
                            🔄 Reintentar
                        </button>
                    </div>
                </div>
            </div>

            <script>
            (function() {{
                // Datos del quiz
                const quizData_{mod_num} = {quiz_json};

                // Restaurar estado previo
                const saved = localStorage.getItem('caja_modulo_{mod_num}_quiz');
                if (saved) {{
                    const data = JSON.parse(saved);
                    showSavedResult({mod_num}, data);
                }}

                // Exponer funciones al scope global
                window.evaluarQuiz = window.evaluarQuiz || function(mod) {{
                    const data = window['quizData_' + mod];
                    let correct = 0;
                    data.forEach((q, i) => {{
                        const selected = document.querySelector('input[name="q' + mod + '_' + i + '"]:checked');
                        const feedback = document.getElementById('feedback-' + mod + '-' + i);
                        const options = document.querySelectorAll('input[name="q' + mod + '_' + i + '"]');
                        
                        options.forEach(o => o.disabled = true);
                        
                        if (selected && parseInt(selected.value) === q.correct) {{
                            correct++;
                            feedback.innerHTML = '<span class="text-green-700">✅ ¡Correcto! ' + q.explanation + '</span>';
                            feedback.className = 'mt-3 p-3 rounded-lg text-sm bg-green-50 border border-green-200';
                        }} else {{
                            feedback.innerHTML = '<span class="text-red-700">❌ Incorrecto. ' + q.explanation + '</span>';
                            feedback.className = 'mt-3 p-3 rounded-lg text-sm bg-red-50 border border-red-200';
                        }}
                        feedback.classList.remove('hidden');
                    }});

                    const total = data.length;
                    const passed = correct >= 2;
                    const resultDiv = document.getElementById('quiz-result-' + mod);
                    resultDiv.innerHTML = passed
                        ? '<div class="text-green-800 font-bold text-lg">🎉 ¡Aprobado! ' + correct + '/' + total + ' respuestas correctas.</div><p class="text-green-700 text-sm mt-2">Su progreso ha sido guardado.</p>'
                        : '<div class="text-orange-800 font-bold text-lg">📘 ' + correct + '/' + total + ' respuestas correctas.</div><p class="text-orange-700 text-sm mt-2">Le recomendamos repasar el contenido y volver a intentarlo.</p>';
                    resultDiv.className = passed
                        ? 'mt-6 p-6 rounded-xl text-center bg-green-50 border border-green-200'
                        : 'mt-6 p-6 rounded-xl text-center bg-orange-50 border border-orange-200';
                    resultDiv.classList.remove('hidden');

                    document.getElementById('quiz-submit-' + mod).classList.add('hidden');
                    document.getElementById('quiz-retry-' + mod).classList.remove('hidden');

                    localStorage.setItem('caja_modulo_' + mod + '_quiz', JSON.stringify({{
                        correct: correct, total: total, passed: passed, date: new Date().toISOString()
                    }}));
                }};

                window.reintentarQuiz = window.reintentarQuiz || function(mod) {{
                    localStorage.removeItem('caja_modulo_' + mod + '_quiz');
                    const container = document.getElementById('quiz-container-' + mod);
                    container.querySelectorAll('input[type="radio"]').forEach(r => {{
                        r.checked = false;
                        r.disabled = false;
                    }});
                    container.querySelectorAll('[id^="feedback-"]').forEach(f => {{
                        f.classList.add('hidden');
                    }});
                    document.getElementById('quiz-result-' + mod).classList.add('hidden');
                    document.getElementById('quiz-retry-' + mod).classList.add('hidden');
                    document.getElementById('quiz-submit-' + mod).classList.remove('hidden');
                }};

                window['quizData_' + {mod_num}] = quizData_{mod_num};
            }})();

            function showSavedResult(mod, data) {{
                const resultDiv = document.getElementById('quiz-result-' + mod);
                if (!resultDiv) return;
                const dateStr = new Date(data.date).toLocaleDateString('es-CR', {{day:'numeric',month:'long',year:'numeric'}});
                resultDiv.innerHTML = data.passed
                    ? '<div class="text-green-800 font-bold text-lg">🎉 Aprobado anteriormente: ' + data.correct + '/' + data.total + '</div><p class="text-green-700 text-sm mt-2">Completado el ' + dateStr + '</p>'
                    : '<div class="text-orange-800 font-bold text-lg">📘 Resultado anterior: ' + data.correct + '/' + data.total + '</div><p class="text-orange-700 text-sm mt-2">Intentado el ' + dateStr + '. Recomendamos repasar el contenido.</p>';
                resultDiv.className = data.passed
                    ? 'mt-6 p-6 rounded-xl text-center bg-green-50 border border-green-200'
                    : 'mt-6 p-6 rounded-xl text-center bg-orange-50 border border-orange-200';
                resultDiv.classList.remove('hidden');
                document.getElementById('quiz-retry-' + mod).classList.remove('hidden');
            }}
            </script>
'''

QUESTION_TEMPLATE = '''                    <!-- Pregunta {q_num} -->
                    <div class="mb-6 p-5 bg-gray-50 rounded-xl border border-gray-200">
                        <p class="font-bold text-gray-900 mb-4">{q_num}. {question}</p>
                        <div class="space-y-3">
{options_html}
                        </div>
                        <div id="feedback-{mod_num}-{q_idx}" class="hidden mt-3 p-3 rounded-lg text-sm"></div>
                    </div>'''

OPTION_TEMPLATE = '                            <label class="flex items-center gap-3 p-3 bg-white rounded-lg border border-gray-100 hover:border-mep-blue hover:bg-blue-50 cursor-pointer transition-all"><input type="radio" name="q{mod_num}_{q_idx}" value="{opt_idx}" class="w-4 h-4 text-mep-blue focus:ring-mep-blue border-gray-300"><span class="text-gray-700">{option_text}</span></label>'

import json

for mod_num, questions in QUIZZES.items():
    filepath = os.path.join(PROJECT, f"modulo-{mod_num}.html")
    if not os.path.exists(filepath):
        print(f"  ⚠️ modulo-{mod_num}.html not found"); continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if f'quiz-section-{mod_num}' in content:
        print(f"  ⏭️ modulo-{mod_num}.html — quiz already exists"); continue

    # Build questions HTML
    questions_html_parts = []
    quiz_json_data = []
    for q_idx, (question, options, correct, explanation) in enumerate(questions):
        opts_html = '\n'.join([
            OPTION_TEMPLATE.format(mod_num=mod_num, q_idx=q_idx, opt_idx=oi, option_text=ot)
            for oi, ot in enumerate(options)
        ])
        questions_html_parts.append(QUESTION_TEMPLATE.format(
            q_num=q_idx+1, question=question, options_html=opts_html,
            mod_num=mod_num, q_idx=q_idx
        ))
        quiz_json_data.append({"correct": correct, "explanation": explanation})

    questions_html = '\n'.join(questions_html_parts)
    quiz_json = json.dumps(quiz_json_data, ensure_ascii=False)

    quiz_block = QUIZ_TEMPLATE.format(
        mod_num=mod_num, questions_html=questions_html, quiz_json=quiz_json
    )

    # Insert before the footer
    footer_marker = '<!-- Footer -->'
    if footer_marker not in content:
        # Try alt marker
        footer_marker = '<footer class='
    
    if footer_marker in content:
        # Insert quiz before the footer, after closing </main></div>
        # Find the last </main> before footer
        footer_pos = content.index(footer_marker)
        # Find the </main> + </div> before footer
        main_close = content.rfind('</main>', 0, footer_pos)
        if main_close == -1:
            print(f"  ❌ modulo-{mod_num}.html — no </main> found"); continue
        
        # Insert quiz block right before </main>
        content = content[:main_close] + quiz_block + '\n        ' + content[main_close:]
    else:
        print(f"  ❌ modulo-{mod_num}.html — no footer marker found"); continue

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ modulo-{mod_num}.html — autoevaluación insertada")

print(f"\n🏁 B-2: Autoevaluación completada.")
