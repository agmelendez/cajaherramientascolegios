import os

# Read template from privacidad-etica.html
with open('privacidad-etica.html', 'r', encoding='utf-8') as f:
    template = f.read()

# We need to replace the content section and title.
# Look for <h1 class="text-3xl font-bold text-gray-900">...</h1>
# Look for <!-- Content Section --> ... <!-- Comenzar Ahora Section -->

start_title = template.find('<h1')
end_title = template.find('</h1>', start_title) + 5
start_desc = template.find('<p class="text-gray-600 ml-9">')
end_desc = template.find('</p>', start_desc) + 4

start_content = template.find('<!-- Content Section -->')
end_content = template.find('<!-- Comenzar Ahora Section -->')

# Generate politica-privacidad.html
pp_title = '<h1 class="text-3xl font-bold text-gray-900">📜 Política de Privacidad</h1>'
pp_desc = '<p class="text-gray-600 ml-9">Información sobre el manejo de datos de acuerdo a la Ley 8968 (Costa Rica).</p>'
pp_content = '''            <!-- Content Section -->
            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none">
                    <div class="text-lg text-gray-700 leading-relaxed mb-6">
                        <h2 class="text-xl font-bold text-gray-900 mb-4" id="ley8968">1. Marco Legal: Ley 8968</h2>
                        <p class="mb-4">De conformidad con la Ley N° 8968 de Costa Rica, "Ley de Protección de la Persona frente al Tratamiento de sus Datos Personales", y su Reglamento, le informamos que esta plataforma está diseñada para la autoformación docente y opera bajo los principios de consentimiento informado, propósito legítimo y confidencialidad.</p>
                        
                        <h2 class="text-xl font-bold text-gray-900 mt-6 mb-4">2. Uso de LocalStorage</h2>
                        <p class="mb-4">Esta plataforma opera bajo una arquitectura "cliente-side" estricta. Todo el progreso, marcadores y configuraciones que usted realiza se almacenan <strong>exclusivamente en el LocalStorage de su propio navegador</strong>.</p>
                        <p class="mb-4">Ningún dato personal, patrón de navegación o métrica de progreso es enviado a servidores externos, ni siquiera a los servidores del CIOdD o de la UCR. Usted tiene el control total de sus datos y puede eliminarlos en cualquier momento borrando el caché de su navegador.</p>

                        <h2 class="text-xl font-bold text-gray-900 mt-6 mb-4">3. Ausencia de Base de Datos Centralizada</h2>
                        <p class="mb-4">Dado que la Caja de Herramientas no cuenta con una base de datos centralizada para usuarios, no existe riesgo de filtraciones o vulneración de su información personal. Al usar avatares genéricos y navegación local, se garantiza un entorno 100% privado.</p>
                    </div>
                </div>
            </div>
'''

pp_html = template[:start_title] + pp_title + template[end_title:start_desc] + pp_desc + template[end_desc:start_content] + pp_content + template[end_content:]

# Update the header in the template to point to the correct links in Footer, as the template might still have old links
pp_html = pp_html.replace(
    '''<li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a></li>
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Servicio</a></li>
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Cumplimiento RGPD</a></li>''',
    '''<li><a href="politica-privacidad.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a></li>
                        <li><a href="terminos-uso.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Uso</a></li>
                        <li><a href="politica-privacidad.html#ley8968" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Ley 8968 / PRODHAB</a></li>'''
)

with open('politica-privacidad.html', 'w', encoding='utf-8') as f:
    f.write(pp_html)

# Generate terminos-uso.html
tu_title = '<h1 class="text-3xl font-bold text-gray-900">⚖️ Términos de Uso</h1>'
tu_desc = '<p class="text-gray-600 ml-9">Condiciones para el uso responsable de la Caja de Herramientas.</p>'
tu_content = '''            <!-- Content Section -->
            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none">
                    <div class="text-lg text-gray-700 leading-relaxed mb-6">
                        <h2 class="text-xl font-bold text-gray-900 mb-4">1. Propósito de la Plataforma</h2>
                        <p class="mb-4">La "Caja de Herramientas Docente en IA" es un proyecto de autoformación y exploración tecnológica. Todos los "prompts", fichas y recomendaciones se proveen "tal cual", con fines estrictamente pedagógicos.</p>

                        <h2 class="text-xl font-bold text-gray-900 mt-6 mb-4">2. Verificación de Outputs</h2>
                        <p class="mb-4">El usuario entiende que las herramientas de IA generativa pueden producir "alucinaciones" (información falsa que parece plausible). <strong>El docente es el único responsable de verificar la precisión académica, la pertinencia cultural y la seguridad</strong> de cualquier contenido generado por IA antes de presentarlo en el aula a personas menores de edad.</p>

                        <h2 class="text-xl font-bold text-gray-900 mt-6 mb-4">3. Propiedad Intelectual</h2>
                        <p class="mb-4">Este proyecto es una iniciativa del Centro de Investigación Observatorio del Desarrollo (CIOdD) de la Universidad de Costa Rica. El diseño, estructura pedagógica y contenido original están protegidos, sin embargo, el uso en el aula por parte de los docentes costarricenses es incentivado y permitido libremente bajo el marco del proyecto ED-3698.</p>

                        <h2 class="text-xl font-bold text-gray-900 mt-6 mb-4">4. Restricción sobre Datos de Menores</h2>
                        <div class="bg-red-50 border-l-4 border-red-500 p-4 rounded-r-lg mt-4 mb-4">
                            <p class="text-red-700"><strong>PROHIBICIÓN ESTRICTA:</strong> Queda terminantemente prohibido utilizar las estrategias enseñadas aquí para procesar datos reales de estudiantes (nombres, adecuaciones, problemas disciplinarios o notas) a través de herramientas de Inteligencia Artificial comerciales externas.</p>
                        </div>
                    </div>
                </div>
            </div>
'''

tu_html = template[:start_title] + tu_title + template[end_title:start_desc] + tu_desc + template[end_desc:start_content] + tu_content + template[end_content:]

# Update footer links
tu_html = tu_html.replace(
    '''<li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a></li>
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Servicio</a></li>
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Cumplimiento RGPD</a></li>''',
    '''<li><a href="politica-privacidad.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a></li>
                        <li><a href="terminos-uso.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Uso</a></li>
                        <li><a href="politica-privacidad.html#ley8968" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Ley 8968 / PRODHAB</a></li>'''
)

with open('terminos-uso.html', 'w', encoding='utf-8') as f:
    f.write(tu_html)

print("Created politica-privacidad.html and terminos-uso.html successfully.")
