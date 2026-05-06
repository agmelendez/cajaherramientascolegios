import os
import glob
import re

base_path = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

# 1. Update all HTML files to include the "Preguntas y Respuestas" link next to "Notificaciones"
html_files = glob.glob(os.path.join(base_path, "*.html"))

faq_link_html = """
            <a href="preguntas-respuestas.html" class="flex items-center gap-2 px-3 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors text-gray-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="text-sm font-medium hidden sm:block">Preguntas y Respuestas</span>
            </a>"""

def add_link(content):
    # Regex to match Notificaciones closing tag
    pattern = r'(Notificaciones</span>\s*</(a|button)>)'
    if "preguntas-respuestas.html" in content:
        return content # Already added
    return re.sub(pattern, r'\1' + faq_link_html, content)

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = add_link(content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(file_path)}")

# 2. Generate preguntas-respuestas.html
with open(os.path.join(base_path, "index.html"), "r", encoding="utf-8") as f:
    index_content = f.read()

top_split = '<main class="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 overflow-y-auto">'
parts = index_content.split(top_split)
top_boilerplate = parts[0] + top_split + "\n"

bottom_split = '</main>'
bottom_boilerplate = "\n" + bottom_split + parts[1].split(bottom_split)[1]

faq_content = """
            <div class="mb-10">
                <h1 class="text-3xl font-bold text-gray-900 flex items-center gap-3">
                    <span class="text-4xl">❓</span> Preguntas y Respuestas
                </h1>
                <p class="text-gray-600 mt-2 max-w-2xl">
                    Respuestas a las preguntas más frecuentes sobre el uso de la Inteligencia Artificial en el aula, basadas en la conferencia del experto Michael John Wooldridge.
                </p>
            </div>

            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none text-gray-700 space-y-8">
                    
                    <div class="bg-blue-50 border border-blue-100 rounded-xl p-6">
                        <h3 class="text-xl font-bold text-mep-blue mb-3">Pregunta 1: ¿Cuál es el próximo gran paso o la próxima frontera para la Inteligencia Artificial?</h3>
                        <p><strong>Respuesta:</strong> El próximo gran reto es la <strong>IA Robótica</strong>, es decir, llevar la inteligencia artificial al mundo físico. Es increíble que la IA actual pueda escribir sobre mecánica cuántica en latín, pero a la vez sea completamente incapaz de entrar a una casa que no conoce, encontrar la cocina, recoger la mesa y meter los platos al lavaplatos. Realizar tareas físicas cotidianas o replicar la destreza de una mano humana es muchísimo más complejo para una máquina de lo que parece.</p>
                    </div>

                    <div class="bg-green-50 border border-green-100 rounded-xl p-6">
                        <h3 class="text-xl font-bold text-mep-green mb-3">Pregunta 2: ¿Qué tanto influye la calidad de lo que lee la IA (sus datos de entrenamiento) en su capacidad de "razonar"?</h3>
                        <p><strong>Respuesta:</strong> Influye muchísimo. Mientras más estructurada y de mayor calidad sea la información que procesa la IA, mejores serán sus resultados. Por ejemplo, a la IA le va excelente escribiendo código de programación porque los lenguajes informáticos son muy lógicos y ordenados, lo que le facilita aprender esos patrones. El gran problema a futuro es que ya se están agotando las fuentes de textos de alta calidad en internet para seguir entrenándola.</p>
                    </div>

                    <div class="bg-purple-50 border border-purple-100 rounded-xl p-6">
                        <h3 class="text-xl font-bold text-purple-700 mb-3">Pregunta 3: ¿Los bebés y los niños aprenden a hablar de la misma forma que la IA?</h3>
                        <p><strong>Respuesta:</strong> No, para nada. El cerebro humano aprende de una manera <strong>mucho más eficiente</strong> y fundamentalmente distinta. Un adolescente de 15 años ya es un experto comunicándose y logró aprender utilizando una cantidad diminuta de información y muy poquita energía (entre 20 y 40 vatios), en comparación con las supercomputadoras y los billones de palabras que necesita una IA para poder hablar. Lograr que las máquinas aprendan de forma tan eficiente como nosotros es un reto gigante para el cual todavía no hay solución a la vista.</p>
                    </div>

                    <div class="bg-orange-50 border border-orange-100 rounded-xl p-6">
                        <h3 class="text-xl font-bold text-mep-orange mb-3">Pregunta 4: ¿Se puede construir un sistema de IA verdaderamente "racional"? ¿Cómo se vería?</h3>
                        <p><strong>Respuesta:</strong> Una mente verdaderamente racional no se contradice; por ejemplo, no afirmaría que algo es cierto para luego decir que es falso al momento siguiente. Durante unos 30 años, los científicos intentaron construir este tipo de IA perfectamente racional y lógica, pero ese enfoque no dio buenos resultados prácticos. La IA que usamos hoy es increíblemente útil, pero definitivamente no funciona como una mente racional.</p>
                    </div>

                    <div class="bg-red-50 border border-red-100 rounded-xl p-6">
                        <h3 class="text-xl font-bold text-red-600 mb-3">Pregunta 5: ¿Es bueno usar la IA como si fuera un amigo o un confidente?</h3>
                        <p><strong>Respuesta:</strong> No. El expositor advierte fuertemente que no debemos tratar a la IA como a un amigo ni crear apegos emocionales con ella. Lo correcto es verla como una <strong>"prótesis cognitiva"</strong> o como una hoja de cálculo muy avanzada. Es una herramienta maravillosa diseñada para hacernos más inteligentes y aumentar nuestras capacidades, pero no para reemplazar las relaciones humanas ni para darnos soporte emocional.</p>
                    </div>

                    <div class="mt-8 bg-gray-50 border border-gray-200 p-4 rounded-lg flex items-center gap-3">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-500 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1" />
                        </svg>
                        <p class="text-sm text-gray-600">
                            <strong>Fuente:</strong> <a href="https://www.youtube.com/live/CyyL0yDhr7I" target="_blank" class="text-mep-blue hover:underline font-medium">Michael Faraday Prize Lecture - Professor Michael John Wooldridge (Royal Society)</a>
                        </p>
                    </div>
                </div>
            </div>
"""

with open(os.path.join(base_path, "preguntas-respuestas.html"), "w", encoding="utf-8") as f:
    f.write(top_boilerplate + faq_content + bottom_boilerplate)
print("Created preguntas-respuestas.html")
