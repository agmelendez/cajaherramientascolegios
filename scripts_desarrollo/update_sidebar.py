import os
import re

files_to_update = [
    "index.html",
    "modulos.html",
    "modulo-1.html",
    "modulo-2.html",
    "modulo-3.html",
    "modulo-4.html",
    "modulo-5.html",
    "modulo-6.html",
    "configuracion.html"
]

base_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios/public"

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'r') as f:
        content = f.read()

    # Determine which item should be active based on filename
    active = "inicio"
    if "modulo" in filename:
        active = "modulos"
    elif "configuracion" in filename:
        active = "configuracion"

    def get_class(item_name):
        base_class = "sidebar-item group flex items-center gap-3 px-3 py-2.5 rounded-lg font-medium transition-all"
        if active == item_name:
            if active == "modulos":
                if "modulo-1" in filename or "modulos" in filename:
                    return f"{base_class} bg-blue-50 text-mep-blue"
                elif "modulo-2" in filename:
                    return f"{base_class} bg-green-50 text-mep-green"
                elif "modulo-3" in filename:
                    return f"{base_class} bg-orange-50 text-mep-orange"
                elif "modulo-4" in filename:
                    return f"{base_class} bg-gray-100 text-gray-800"
                elif "modulo-5" in filename:
                    return f"{base_class} bg-blue-50 text-mep-blue"
                elif "modulo-6" in filename:
                    return f"{base_class} bg-purple-50 text-purple-700"
                else:
                    return f"{base_class} bg-blue-50 text-mep-blue"
            else:
                return f"{base_class} bg-blue-50 text-mep-blue"
        else:
            return f"{base_class} text-gray-600 hover:bg-gray-50 hover:text-gray-900"
            
    def get_icon_class(item_name):
        if active == item_name:
            return "text-xl group-hover:scale-110 transition-transform"
        else:
            return "text-xl group-hover:scale-110 transition-transform grayscale group-hover:grayscale-0"

    nav_content = f"""<nav class="flex-1 px-4 py-6 space-y-1 overflow-y-auto">
                <a href="index.html" class="{get_class('inicio')}">
                    <span class="{get_icon_class('inicio')}">📊</span>
                    <span>Inicio</span>
                </a>
                <a href="modulos.html" class="{get_class('modulos')}">
                    <span class="{get_icon_class('modulos')}">📚</span>
                    <span>Módulos</span>
                </a>
                <a href="descargas.html" class="{get_class('descargas')}">
                    <span class="{get_icon_class('descargas')}">📥</span>
                    <span>Descargas</span>
                </a>
                <a href="comunidad.html" class="{get_class('comunidad')}">
                    <span class="{get_icon_class('comunidad')}">💬</span>
                    <span>Comunidad</span>
                </a>
                <a href="configuracion.html" class="{get_class('configuracion')}">
                    <span class="{get_icon_class('configuracion')}">⚙️</span>
                    <span>Configuración</span>
                </a>
                <div class="pt-6 mt-6 border-t border-gray-100">
                    <a href="ayuda.html" class="{get_class('ayuda')}">
                        <span class="text-xl opacity-70 group-hover:opacity-100 transition-opacity">❓</span>
                        <span>Ayuda</span>
                    </a>
                </div>
            </nav>"""

    # Regex to replace the entire <nav>...</nav> block
    new_content = re.sub(r'<nav class="flex-1 px-4 py-6 space-y-1 overflow-y-auto">.*?</nav>', nav_content, content, flags=re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filename}")

