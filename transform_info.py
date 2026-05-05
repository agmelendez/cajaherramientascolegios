import re

with open("configuracion.html", "r") as f:
    content = f.read()

# Change title
content = content.replace("<title>Configuración - Caja de Herramientas</title>", "<title>Información - Caja de Herramientas</title>")

# Change sidebar "Configuración" to "Información" and icon ⚙️ to ℹ️
content = content.replace("<span>Configuración</span>", "<span>Información</span>")
content = content.replace("⚙️", "ℹ️")
content = content.replace("Ajustes del Sistema", "Información del Proyecto")

# Replace Main Content
top_split = '<main class="flex-1 w-full max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8 overflow-y-auto">'
parts = content.split(top_split)
top_boilerplate = parts[0] + top_split + "\n"

bottom_split = '</main>'
bottom_boilerplate = "\n" + bottom_split + parts[1].split(bottom_split)[1]

info_content = """
            <!-- Page Header -->
            <div class="mb-8">
                <h1 class="text-3xl font-extrabold text-gray-900 mb-2">Información del Proyecto</h1>
                <p class="text-gray-600">Datos, referencias y medios de contacto del Centro de Investigación Observatorio del Desarrollo (CIOdD).</p>
            </div>

            <div class="space-y-6">
                
                <!-- About Project -->
                <div class="bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden">
                    <div class="px-6 py-5 border-b border-gray-100 bg-gray-50/50">
                        <h3 class="text-lg font-bold text-gray-900 flex items-center gap-2">
                            <svg class="w-5 h-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                            Acerca de
                        </h3>
                    </div>
                    <div class="p-6">
                        <p class="text-gray-700 leading-relaxed mb-4">
                            Esta plataforma es parte del proyecto <strong>ED-3698 "Inteligencia Artificial en el aula: una guía para la educación innovadora"</strong>, desarrollado por la Universidad de Costa Rica en 2026.
                        </p>
                        <p class="text-gray-700 leading-relaxed">
                            El objetivo del <strong>Centro de Investigación Observatorio del Desarrollo (CIOdD)</strong> es contribuir a la creación, gestión y transmisión de conocimiento innovador multi, inter y trans-disciplinario, por medio de índices y métricas para la definición y orientación de políticas, con el fin de incidir en el bienestar y desarrollo integral del país.
                        </p>
                    </div>
                </div>

                <!-- Contact Info -->
                <div class="bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden">
                    <div class="px-6 py-5 border-b border-gray-100 bg-gray-50/50">
                        <h3 class="text-lg font-bold text-gray-900 flex items-center gap-2">
                            <svg class="w-5 h-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>
                            Contacto Institucional
                        </h3>
                    </div>
                    <div class="p-0">
                        <div class="grid grid-cols-1 md:grid-cols-2">
                            <!-- Dirección -->
                            <div class="p-6 border-b md:border-b-0 md:border-r border-gray-100">
                                <h4 class="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wider">Dirección General</h4>
                                <div class="flex items-center gap-3 mb-2">
                                    <span class="text-mep-blue">📧</span>
                                    <a href="mailto:ciodd@ucr.ac.cr" class="text-gray-600 hover:text-mep-blue transition-colors">ciodd@ucr.ac.cr</a>
                                </div>
                                <div class="flex items-center gap-3">
                                    <span class="text-mep-blue">📞</span>
                                    <a href="tel:+50625111488" class="text-gray-600 hover:text-mep-blue transition-colors">(506) 2511-1488</a>
                                </div>
                            </div>
                            
                            <!-- Administración -->
                            <div class="p-6 border-b border-gray-100">
                                <h4 class="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wider">Administración</h4>
                                <div class="flex items-center gap-3 mb-2">
                                    <span class="text-mep-blue">📧</span>
                                    <a href="mailto:johanna.tenorio@ucr.ac.cr" class="text-gray-600 hover:text-mep-blue transition-colors">johanna.tenorio@ucr.ac.cr</a>
                                </div>
                                <div class="flex items-center gap-3">
                                    <span class="text-mep-blue">📞</span>
                                    <a href="tel:+50625114878" class="text-gray-600 hover:text-mep-blue transition-colors">(506) 2511-4878</a>
                                </div>
                            </div>

                            <!-- Prensa -->
                            <div class="p-6 border-b md:border-b-0 md:border-r border-gray-100">
                                <h4 class="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wider">Prensa</h4>
                                <div class="flex items-center gap-3 mb-2">
                                    <span class="text-mep-blue">📧</span>
                                    <a href="mailto:ciodd@ucr.ac.cr" class="text-gray-600 hover:text-mep-blue transition-colors">ciodd@ucr.ac.cr</a>
                                </div>
                                <div class="flex items-center gap-3">
                                    <span class="text-mep-blue">📞</span>
                                    <a href="tel:+50625114878" class="text-gray-600 hover:text-mep-blue transition-colors">(506) 2511-4878</a>
                                </div>
                            </div>

                            <!-- Ubicación -->
                            <div class="p-6">
                                <h4 class="text-sm font-bold text-gray-900 mb-3 uppercase tracking-wider">Ubicación</h4>
                                <div class="flex items-start gap-3">
                                    <span class="text-mep-blue mt-1">📍</span>
                                    <p class="text-gray-600 text-sm leading-relaxed">
                                        Montes de Oca, San Pedro.<br>
                                        De la Fuente de la Hispanidad 100 E, 100 N, 100 E, 25 N.<br>
                                        Universidad de Costa Rica.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Enlaces y Redes -->
                <div class="bg-blue-50 rounded-2xl border border-blue-100 p-6 shadow-inner mt-8">
                    <h3 class="text-sm font-bold text-mep-blue uppercase tracking-wider mb-6">Enlaces y Redes Sociales (CIOdD)</h3>
                    
                    <div class="flex flex-wrap gap-4">
                        <a href="https://ciodd.ucr.ac.cr/" target="_blank" class="px-4 py-2 bg-white rounded-lg border border-blue-200 text-gray-700 hover:text-mep-blue hover:shadow-sm transition-all text-sm font-medium flex items-center gap-2">
                            🌐 Sitio Web CIOdD
                        </a>
                        <a href="https://www.facebook.com/CIOdD.UCR" target="_blank" class="px-4 py-2 bg-white rounded-lg border border-blue-200 text-gray-700 hover:text-mep-blue hover:shadow-sm transition-all text-sm font-medium flex items-center gap-2">
                            📘 Facebook
                        </a>
                        <a href="https://www.instagram.com/ciobdesarrollo/" target="_blank" class="px-4 py-2 bg-white rounded-lg border border-blue-200 text-gray-700 hover:text-mep-blue hover:shadow-sm transition-all text-sm font-medium flex items-center gap-2">
                            📸 Instagram
                        </a>
                        <a href="https://www.twitter.com/CIOdDUCR" target="_blank" class="px-4 py-2 bg-white rounded-lg border border-blue-200 text-gray-700 hover:text-mep-blue hover:shadow-sm transition-all text-sm font-medium flex items-center gap-2">
                            🐦 Twitter
                        </a>
                        <a href="https://www.youtube.com/channel/UC6Kz7-OMjFg4zwNDehxs2jQ" target="_blank" class="px-4 py-2 bg-white rounded-lg border border-blue-200 text-gray-700 hover:text-mep-blue hover:shadow-sm transition-all text-sm font-medium flex items-center gap-2">
                            ▶️ YouTube
                        </a>
                        <a href="https://www.linkedin.com/company/obdesarrollo/" target="_blank" class="px-4 py-2 bg-white rounded-lg border border-blue-200 text-gray-700 hover:text-mep-blue hover:shadow-sm transition-all text-sm font-medium flex items-center gap-2">
                            💼 LinkedIn
                        </a>
                    </div>
                </div>

            </div>
"""

with open("configuracion.html", "w") as f:
    f.write(top_boilerplate + info_content + bottom_boilerplate)
