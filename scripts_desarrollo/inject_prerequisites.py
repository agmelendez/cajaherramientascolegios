import os
import re

def main():
    workspace_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"
    
    # Mapeo de dependencias de los módulos (Clave: número de módulo, Valor: lista de IDs de prerrequisitos)
    dependencies = {
        1: [],
        2: [1],
        3: [1],
        4: [3],
        5: [3],
        6: [3],
        7: [4],
        8: [6],
        9: [3],
        10: [3]
    }
    
    for i in range(1, 11):
        filename = f"modulo-{i}.html"
        file_path = os.path.join(workspace_dir, filename)
        
        if not os.path.exists(file_path):
            print(f"Advertencia: {filename} no existe, omitiendo.")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        prereqs = dependencies[i]
        
        # Eliminar cualquier bloque de prerrequisitos inyectado anteriormente para permitir re-ejecución limpia
        pattern_existing = re.compile(r'<!-- 🔑 Panel de Prerrequisitos Dinámicos \(Sprint 5\) -->.*?<!-- Fin Panel de Prerrequisitos -->', re.DOTALL)
        content_cleaned, count = pattern_existing.subn("", content)
        
        if not prereqs:
            if count > 0:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content_cleaned)
                print(f"Módulo {i}: No requiere prerrequisitos. Removido banner previo.")
            else:
                print(f"Módulo {i}: No requiere prerrequisitos.")
            continue
            
        prereqs_js_array = ", ".join(map(str, prereqs))
        
        # Plantilla del banner de prerrequisitos didácticos con su JS inline autorreactivo
        template_banner = """<!-- 🔑 Panel de Prerrequisitos Dinámicos (Sprint 5) -->
            <div id="caja-prerrequisitos" class="hidden bg-orange-50 border border-orange-200 rounded-2xl p-5 mb-8 flex gap-4 items-start shadow-sm transition-all duration-300">
                <div class="flex-shrink-0 w-10 h-10 bg-orange-100 rounded-xl flex items-center justify-center text-xl">🔑</div>
                <div class="flex-1">
                    <h3 class="font-bold text-orange-950 mb-1 flex items-center gap-2">Recomendación de Prerrequisitos</h3>
                    <p class="text-sm text-orange-900 leading-relaxed m-0">
                        Te sugerimos completar los siguientes módulos antes de continuar para asegurar una mejor comprensión del contenido actual: 
                        <span id="prereq-list" class="font-extrabold text-orange-950"></span>.
                    </p>
                    <div class="mt-3 flex gap-2">
                        <a href="modulos.html" class="px-3.5 py-1.5 bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold rounded-lg transition-colors flex items-center gap-1 shadow-sm">
                            🗺️ Ver Mapa de Ruta
                        </a>
                        <button onclick="document.getElementById('caja-prerrequisitos').remove()" class="px-3.5 py-1.5 bg-orange-100 hover:bg-orange-200 text-orange-800 text-xs font-bold rounded-lg transition-colors">
                            Omitir recomendación
                        </button>
                    </div>
                </div>
                <script>
                    document.addEventListener('DOMContentLoaded', () => {
                        const requiredPrereqs = [__PREREQS_ARRAY__];
                        const namesMap = {
                            1: "Módulo 1: IA en Educación",
                            2: "Módulo 2: Ética y Privacidad",
                            3: "Módulo 3: Prompts Efectivos",
                            4: "Módulo 4: Herramientas Prácticas de IA",
                            5: "Módulo 5: Aplicaciones Prácticas",
                            6: "Módulo 6: Análisis de Datos",
                            7: "Módulo 7: Comparativa de Motores de IA",
                            8: "Módulo 8: IA en Colegios Técnicos",
                            9: "Módulo 9: Jóvenes y Adultos",
                            10: "Módulo 10: Micro-Prompts"
                        };
                        const missing = requiredPrereqs.filter(id => localStorage.getItem("caja_modulo_" + id + "_quiz") === null);
                        if (missing.length > 0) {
                            const listEl = document.getElementById('prereq-list');
                            if (listEl) {
                                listEl.innerText = missing.map(id => namesMap[id]).join(', ');
                            }
                            const bannerEl = document.getElementById('caja-prerrequisitos');
                            if (bannerEl) {
                                bannerEl.classList.remove('hidden');
                            }
                        }
                    });
                </script>
            </div>
            <!-- Fin Panel de Prerrequisitos -->"""

        banner_html = template_banner.replace("__PREREQS_ARRAY__", prereqs_js_array)

        # Encontrar la etiqueta <main ...> y colocar el banner justo después
        main_tag_match = re.search(r'(<main\s+[^>]*class="[^"]*flex-1[^"]*"[^>]*>)', content_cleaned)
        if not main_tag_match:
            print(f"Error: No se pudo encontrar el tag <main> principal en {filename}.")
            continue
            
        main_tag_str = main_tag_match.group(1)
        # Reemplazar e inyectar
        new_content = content_cleaned.replace(main_tag_str, f"{main_tag_str}\n\n            {banner_html}")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Módulo {i}: Banner de prerrequisitos inyectado correctamente.")

if __name__ == "__main__":
    main()
