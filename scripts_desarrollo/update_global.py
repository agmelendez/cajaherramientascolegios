import os
import re
import glob

public_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios/public"
html_files = glob.glob(os.path.join(public_dir, "*.html"))

new_footer = "Centro de Investigación Observatorio del Desarrollo de la Universidad de Costa Rica. Proyecto ED-3698 Inteligencia Artificial en el aula: una guía para la educación innovadora, 2026."
old_footer = "&copy; 2026 Ministerio de Educación Pública (MEP). Costa Rica. Todos los derechos reservados."

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Footer
    content = content.replace(old_footer, new_footer)

    # 2. Update Avatar name and image
    # For 'Agustin'
    content = re.sub(
        r'<img src="https://ui-avatars\.com/api/\?name=Agustin\+Gomez&background=0066cc&color=fff" alt="Avatar" class="([^"]+)">\s*<span class="([^"]+)">Agustín</span>',
        r'<img src="https://ui-avatars.com/api/?name=Agustin+Gomez&background=0066cc&color=fff" alt="Avatar" class="\1">\n                <span class="\2">Agustín Gómez Meléndez</span>',
        content
    )
    # For 'Docente'
    content = re.sub(
        r'<img src="https://ui-avatars\.com/api/\?name=Docente&background=0066cc&color=fff" alt="Avatar" class="([^"]+)">\s*<span class="([^"]+)">Docente</span>',
        r'<img src="https://ui-avatars.com/api/?name=Agustin+Gomez&background=0066cc&color=fff" alt="Avatar" class="\1">\n                <span class="\2">Agustín Gómez Meléndez</span>',
        content
    )

    # 3. Update Metrics (only in index.html and dashboard.html)
    if "index.html" in filepath or "dashboard.html" in filepath:
        # 156 -> 1
        content = re.sub(
            r'<div class="text-3xl font-extrabold text-gray-900 mb-1">156</div>',
            r'<div class="text-3xl font-extrabold text-gray-900 mb-1">1</div>',
            content
        )
        content = re.sub(
            r'156 docentes',
            r'1 docente',
            content
        )
        # 12 -> 9
        content = re.sub(
            r'<div class="text-3xl font-extrabold text-mep-blue mb-1">12</div>',
            r'<div class="text-3xl font-extrabold text-mep-blue mb-1">9</div>',
            content
        )
        # 42 -> 92
        content = re.sub(
            r'<div class="text-3xl font-extrabold text-gray-900 mb-1">42</div>',
            r'<div class="text-3xl font-extrabold text-gray-900 mb-1">92</div>',
            content
        )
        # 89% -> 0%
        content = re.sub(
            r'<div class="text-3xl font-extrabold text-mep-green mb-1">89%</div>',
            r'<div class="text-3xl font-extrabold text-mep-green mb-1">0%</div>',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files successfully.")
