import os
import re

directory = "."

# 1. Update metrics in index.html
with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

index_old_metrics = """                        <div class="grid grid-cols-2 gap-4">
                            <div class="bg-gray-50 p-4 rounded-xl text-center">
                                <div class="text-3xl font-extrabold text-gray-900 mb-1">1</div>
                                <div class="text-xs font-medium text-gray-500 uppercase tracking-wider">Docentes Activos</div>
                            </div>
                            <div class="bg-gray-50 p-4 rounded-xl text-center">
                                <div class="text-3xl font-extrabold text-mep-blue mb-1">9</div>
                                <div class="text-xs font-medium text-gray-500 uppercase tracking-wider">Módulos</div>
                            </div>
                            <div class="bg-gray-50 p-4 rounded-xl text-center">
                                <div class="text-3xl font-extrabold text-gray-900 mb-1">92</div>
                                <div class="text-xs font-medium text-gray-500 uppercase tracking-wider">Microcontenidos</div>
                            </div>
                            <div class="bg-green-50 p-4 rounded-xl text-center border border-green-100">
                                <div class="text-3xl font-extrabold text-mep-green mb-1">0%</div>
                                <div class="text-xs font-medium text-green-700 uppercase tracking-wider">Completación Avg.</div>
                            </div>
                        </div>"""

index_new_metrics = """                        <div class="grid grid-cols-2 gap-4">
                            <div class="bg-gray-50 p-4 rounded-xl text-center">
                                <div class="text-3xl font-extrabold text-gray-900 mb-1">9</div>
                                <div class="text-xs font-medium text-gray-500 uppercase tracking-wider">Módulos</div>
                            </div>
                            <div class="bg-gray-50 p-4 rounded-xl text-center">
                                <div class="text-3xl font-extrabold text-mep-blue mb-1">92</div>
                                <div class="text-xs font-medium text-gray-500 uppercase tracking-wider">Microcontenidos</div>
                            </div>
                            <div class="bg-gray-50 p-4 rounded-xl text-center">
                                <div class="text-3xl font-extrabold text-gray-900 mb-1">15</div>
                                <div class="text-xs font-medium text-gray-500 uppercase tracking-wider">Horas Formación</div>
                            </div>
                            <div class="bg-green-50 p-4 rounded-xl text-center border border-green-100">
                                <div class="text-3xl font-extrabold text-mep-green mb-1">45+</div>
                                <div class="text-xs font-medium text-green-700 uppercase tracking-wider">Recursos Prácticos</div>
                            </div>
                        </div>"""

index_content = index_content.replace(index_old_metrics, index_new_metrics)
index_content = index_content.replace("Ir al Dashboard Principal", "Ir al Panel Principal")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_content)


# 2. Update metrics in dashboard.html and remove Acciones Rápidas
with open("dashboard.html", "r", encoding="utf-8") as f:
    dash_content = f.read()

dash_old_metrics = """            <!-- Stats Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center">
                    <div class="w-12 h-12 bg-blue-50 rounded-full flex items-center justify-center text-mep-blue mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-gray-900 mb-1">12</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Módulos Activos</div>
                </div>

                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center">
                    <div class="w-12 h-12 bg-green-50 rounded-full flex items-center justify-center text-mep-green mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-gray-900 mb-1">1</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Docentes Reg.</div>
                </div>

                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center relative overflow-hidden">
                    <div class="absolute inset-0 bg-orange-50/50 -z-10"></div>
                    <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center text-mep-orange mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-mep-orange mb-1">89%</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Completación Avg</div>
                </div>

                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center">
                    <div class="w-12 h-12 bg-purple-50 rounded-full flex items-center justify-center text-purple-600 mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-gray-900 mb-1">92</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Microcontenidos</div>
                </div>
            </div>"""

dash_new_metrics = """            <!-- Stats Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center">
                    <div class="w-12 h-12 bg-blue-50 rounded-full flex items-center justify-center text-mep-blue mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-gray-900 mb-1">9</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Módulos Activos</div>
                </div>

                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center">
                    <div class="w-12 h-12 bg-purple-50 rounded-full flex items-center justify-center text-purple-600 mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-gray-900 mb-1">92</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Microcontenidos</div>
                </div>

                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center relative overflow-hidden">
                    <div class="absolute inset-0 bg-orange-50/50 -z-10"></div>
                    <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center text-mep-orange mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-mep-orange mb-1">15</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Horas Formación</div>
                </div>

                <div class="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm flex flex-col items-center justify-center text-center">
                    <div class="w-12 h-12 bg-green-50 rounded-full flex items-center justify-center text-mep-green mb-3">
                        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12"></path></svg>
                    </div>
                    <div class="text-3xl font-extrabold text-gray-900 mb-1">45+</div>
                    <div class="text-sm font-medium text-gray-500 uppercase tracking-wider">Recursos Prácticos</div>
                </div>
            </div>"""

dash_content = dash_content.replace(dash_old_metrics, dash_new_metrics)

# Remove Acciones Rápidas
acciones_rapidas_pattern = re.compile(
    r'<!-- Acciones Rápidas -->\s*<div class="bg-gradient-to-b from-blue-50 to-white rounded-2xl border border-blue-100 shadow-sm p-6">.*?</div>\s*(?=<!-- Anuncios -->)',
    re.IGNORECASE | re.DOTALL
)

dash_content = acciones_rapidas_pattern.sub("", dash_content)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(dash_content)

# 3. Global Spanish Translations
# We need to change:
# "Dashboard" -> "Panel Principal"
# "Usuarios" is already fine, but wait, the user said "elimina mi nombre en el sistema y en la funcionalidad porque todo lo relacionado con registor lo voy a manejar por aparte", maybe I should remove "Usuarios" from the sidebar as well since it's user management? Yes! 
# Let's remove "Usuarios" link from all sidebars!

usuarios_sidebar_pattern = re.compile(
    r'<a href="usuarios\.html" class="sidebar-item group flex items-center gap-3 px-3 py-2\.5 text-gray-600 hover:bg-gray-50 hover:text-gray-900 rounded-lg font-medium transition-all">\s*<span class="text-xl group-hover:scale-110 transition-transform grayscale group-hover:grayscale-0">👥</span>\s*<span>Usuarios</span>\s*</a>',
    re.IGNORECASE | re.DOTALL
)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace "Dashboard" -> "Panel Principal"
        content = content.replace("Dashboard", "Panel Principal")
        # Except maybe if they want to keep the file name as dashboard.html, that's fine. We just change the text.
        content = content.replace("<span>Panel Principal</span>", "<span>Panel Principal</span>") # already done by above
        content = content.replace("Ir al Panel Principal Principal", "Ir al Panel Principal") # just in case of double replacement
        
        # Remove Usuarios link from sidebar
        content = usuarios_sidebar_pattern.sub("", content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
