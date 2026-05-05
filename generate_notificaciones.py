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

# 1. Generate Notificaciones Index
index_content = """
            <div class="mb-10">
                <h1 class="text-3xl font-bold text-gray-900 flex items-center gap-3">
                    <span class="text-4xl">🔔</span> Centro de Notificaciones y Novedades
                </h1>
                <p class="text-gray-600 mt-2 max-w-2xl">
                    Mantente al día con las últimas actualizaciones de la plataforma, nuevos módulos disponibles, alertas de seguridad y noticias relevantes para tu práctica docente.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <!-- Noticia 1 -->
                <a href="noticia-1.html" class="bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg transition-all p-6 group block">
                    <div class="flex items-center justify-between mb-4">
                        <span class="px-3 py-1 bg-blue-100 text-mep-blue text-xs font-bold rounded-full">Actualización</span>
                        <span class="text-gray-400 text-sm">15 de Mayo, 2026</span>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-mep-blue transition-colors">Noticia 1: Nuevos Prompts Validados para Primaria</h3>
                    <p class="text-gray-600 mb-4 line-clamp-2">Hemos agregado una colección de 20 nuevos prompts específicamente diseñados para docentes de I y II ciclo. Descubre cómo utilizarlos para generar actividades dinámicas en menos de 5 minutos.</p>
                    <div class="text-mep-blue font-medium text-sm flex items-center gap-1 group-hover:gap-2 transition-all">
                        Leer artículo completo <span aria-hidden="true">&rarr;</span>
                    </div>
                </a>

                <!-- Noticia 2 -->
                <a href="noticia-2.html" class="bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg transition-all p-6 group block">
                    <div class="flex items-center justify-between mb-4">
                        <span class="px-3 py-1 bg-orange-100 text-mep-orange text-xs font-bold rounded-full">Alerta Ética</span>
                        <span class="text-gray-400 text-sm">2 de Mayo, 2026</span>
                    </div>
                    <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-mep-orange transition-colors">Noticia 2: Cambios en Políticas de Privacidad de Herramientas Gratuitas</h3>
                    <p class="text-gray-600 mb-4 line-clamp-2">Importante aviso sobre recientes actualizaciones en los términos de servicio de varias herramientas de IA generativa de acceso público. Recomendaciones para proteger los datos de tus estudiantes.</p>
                    <div class="text-mep-blue font-medium text-sm flex items-center gap-1 group-hover:gap-2 transition-all">
                        Leer artículo completo <span aria-hidden="true">&rarr;</span>
                    </div>
                </a>
            </div>
"""
with open("notificaciones.html", "w") as f:
    f.write(top_boilerplate + index_content + bottom_boilerplate)


# 2. Generate Noticia 1
noticia_1_content = """
            <div class="mb-8">
                <a href="notificaciones.html" class="inline-flex items-center gap-2 text-mep-blue hover:underline mb-6 font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    Volver a Notificaciones
                </a>
                
                <div class="flex items-center gap-3 mb-4">
                    <span class="px-3 py-1 bg-blue-100 text-mep-blue text-sm font-bold rounded-full">Actualización</span>
                    <span class="text-gray-500 text-sm">15 de Mayo, 2026</span>
                </div>
                
                <h1 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-6">Noticia 1: Nuevos Prompts Validados para Primaria</h1>
            </div>

            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none text-gray-700 space-y-6">
                    <p class="text-lg leading-relaxed">
                        ¡Tenemos excelentes noticias para nuestros docentes de I y II ciclo! Atendiendo a sus solicitudes en la comunidad, hemos publicado un nuevo banco de prompts especializados.
                    </p>
                    <p>
                        A menudo, encontrar la instrucción exacta para que la IA genere materiales adaptados a niños pequeños puede ser un reto. La IA tiende a utilizar vocabulario complejo o estructuras abstractas que no resuenan con estudiantes de primaria. 
                    </p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">¿Qué incluye esta actualización?</h3>
                    <ul class="list-disc pl-5 space-y-2">
                        <li><strong>10 Prompts para Matemáticas:</strong> Enfocados en material manipulativo y resolución de problemas cotidianos.</li>
                        <li><strong>5 Prompts para Lectoescritura:</strong> Diseñados para generar cuentos cortos con fonemas específicos y preguntas de comprensión literal e inferencial.</li>
                        <li><strong>5 Prompts de Ciencias:</strong> Orientados a la indagación, experimentos caseros sencillos y exploración del entorno.</li>
                    </ul>
                    <div class="bg-blue-50 border-l-4 border-mep-blue p-4 mt-6">
                        <p class="font-bold text-gray-900 mb-1">💡 Ejemplo de la nueva colección:</p>
                        <p class="italic">"Actúa como un maestro experto en lectoescritura de primer grado. Crea un cuento muy corto (máximo 100 palabras) en el que predominen las palabras con la sílaba 'ma', 'me', 'mi', 'mo', 'mu'. El protagonista debe ser un mono llamado Tito. Al final, incluye 2 preguntas sencillas de comprensión lectora literal."</p>
                    </div>
                    <p class="mt-6">
                        Puedes encontrar este nuevo recurso en la sección de <strong>Descargas > Banco de Prompts Trimestral</strong>. ¡Pruébalos y cuéntanos en la comunidad cómo te funcionaron!
                    </p>
                </div>
            </div>
"""
with open("noticia-1.html", "w") as f:
    f.write(top_boilerplate + noticia_1_content + bottom_boilerplate)


# 3. Generate Noticia 2
noticia_2_content = """
            <div class="mb-8">
                <a href="notificaciones.html" class="inline-flex items-center gap-2 text-mep-blue hover:underline mb-6 font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    Volver a Notificaciones
                </a>
                
                <div class="flex items-center gap-3 mb-4">
                    <span class="px-3 py-1 bg-orange-100 text-mep-orange text-sm font-bold rounded-full">Alerta Ética</span>
                    <span class="text-gray-500 text-sm">2 de Mayo, 2026</span>
                </div>
                
                <h1 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-6">Noticia 2: Cambios en Políticas de Privacidad de Herramientas Gratuitas</h1>
            </div>

            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none text-gray-700 space-y-6">
                    <p class="text-lg leading-relaxed text-red-600 font-medium">
                        Atención docentes: Hemos detectado cambios importantes en los términos de servicio de varias plataformas de IA generativa de uso gratuito. 
                    </p>
                    <p>
                        A partir de este mes, algunas de las herramientas gratuitas más populares han modificado sus políticas de privacidad. Las nuevas cláusulas indican que <strong>los datos introducidos en los chats gratuitos podrán ser utilizados de forma predeterminada para el entrenamiento de futuros modelos de lenguaje</strong>.
                    </p>
                    <h3 class="text-xl font-bold text-gray-900 mt-8 mb-4">¿Por qué es esto importante para nosotros?</h3>
                    <p>
                        Como educadores, manejamos información confidencial a diario. Si utilizamos una de estas herramientas gratuitas para resumir el expediente de un estudiante, redactar un correo para un padre de familia (incluyendo nombres), o analizar calificaciones, esa información pasa a ser parte de la base de datos de la empresa de tecnología. Esto constituye una violación a la normativa de protección de datos de menores.
                    </p>
                    <div class="bg-orange-50 border-l-4 border-mep-orange p-6 mt-6">
                        <p class="font-bold text-gray-900 text-lg mb-2">Protocolo de Acción Recomendado</p>
                        <ol class="list-decimal pl-5 space-y-2 text-gray-800">
                            <li><strong>Privilegia cuentas institucionales:</strong> Utiliza únicamente las herramientas licenciadas por la institución educativa (ej. Google Workspace for Education), ya que estas cuentas tienen acuerdos que impiden el uso de datos para entrenamiento.</li>
                            <li><strong>Anonimiza todo:</strong> Si te ves obligado a usar una herramienta gratuita para generar ideas, NUNCA introduzcas nombres reales, edades, instituciones, números de identificación, ni diagnósticos médicos. Utiliza alias (Estudiante A) o descripciones muy generales.</li>
                            <li><strong>Revisa las configuraciones:</strong> En herramientas como ChatGPT, puedes ir a Configuración > Controles de Datos y desactivar el historial de chat y el entrenamiento del modelo. Hazlo inmediatamente en tus cuentas personales.</li>
                        </ol>
                    </div>
                    <p class="mt-6 font-medium text-gray-900">
                        La seguridad de nuestros estudiantes es primero. Ante la duda, no subas la información.
                    </p>
                </div>
            </div>
"""
with open("noticia-2.html", "w") as f:
    f.write(top_boilerplate + noticia_2_content + bottom_boilerplate)
