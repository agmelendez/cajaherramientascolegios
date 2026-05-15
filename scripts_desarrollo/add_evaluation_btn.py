import os
import glob
import re

base_path = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"
html_files = glob.glob(os.path.join(base_path, "*.html"))

new_btn = """<a href="https://iadocenciaed3698.my.canva.site/pruebacajaherramientacolegios" target="_blank" class="sidebar-item group flex items-center gap-3 px-3 py-2.5 rounded-lg font-medium transition-all text-gray-600 hover:bg-gray-50 hover:text-gray-900" aria-label="Ir a la evaluación del curso">
                    <span class="text-xl group-hover:scale-110 transition-transform grayscale group-hover:grayscale-0">📋</span>
                    <span>Evaluación del Curso</span>
                </a>
                """

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    
    # Check if the button is already there to avoid duplicates
    if "https://iadocenciaed3698.my.canva.site/pruebacajaherramientacolegios" in content:
        print(f"Skipping {os.path.basename(file_path)} - Already has evaluation link.")
        continue

    # Regex to find the configuracion.html link and append the new_btn after it
    # We match the entire <a> block for configuracion.html, plus any trailing whitespace
    content = re.sub(
        r'(<a href="configuracion.html"[^>]*>[\s\S]*?</a>\s*)',
        r'\1' + new_btn,
        content
    )
    
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
    else:
        print(f"No changes needed for {os.path.basename(file_path)}")

print("Done.")
