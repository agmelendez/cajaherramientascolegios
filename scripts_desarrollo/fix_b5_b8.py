#!/usr/bin/env python3
"""
B-5: Agregar aria-label a los ítems de navegación del sidebar.
B-8: Agregar banner de advertencia sobre datos de estudiantes en módulos 1-9.
"""

import os
import glob

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════
# B-5: aria-labels en sidebar
# ═══════════════════════════════════════════

ARIA_REPLACEMENTS = [
    # Sidebar items (both active and inactive variants)
    ('📊</span>\n                    <span>Inicio</span>',
     '📊</span>\n                    <span>Inicio</span>',
     # We need to target the <a> tags, not the text inside
    ),
]

# More targeted approach: replace exact patterns
SIDEBAR_ARIA = {
    'href="index.html"': ('Ir a la página de Inicio', 'Inicio'),
    'href="modulos.html"': ('Ver todos los módulos del curso', 'Módulos'),
    'href="descargas.html"': ('Ir a la sección de descargas', 'Descargas'),
    'href="comunidad.html"': ('Ir a la comunidad docente', 'Comunidad'),
    'href="configuracion.html"': ('Ir a la configuración', 'Configuración'),
    'href="ayuda.html"': ('Ir a la sección de ayuda', 'Ayuda'),
}

html_files = glob.glob(os.path.join(PROJECT_DIR, "*.html"))
b5_count = 0

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    for href, (aria_label, label_text) in SIDEBAR_ARIA.items():
        # Match sidebar-item links that DON'T already have aria-label
        # Pattern: <a href="X.html" class="sidebar-item ...">
        import re
        pattern = rf'(<a\s+{re.escape(href)}\s+class="sidebar-item[^"]*")(>)'
        replacement = rf'\1 aria-label="{aria_label}"\2'
        # Only replace if aria-label not already present
        if f'{href}' in content and f'aria-label="{aria_label}"' not in content:
            content = re.sub(pattern, replacement, content)
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        b5_count += 1
        print(f"  ✅ B-5 {filename} — aria-labels agregados")

print(f"\n🏁 B-5: {b5_count} archivos actualizados con aria-labels.\n")

# ═══════════════════════════════════════════
# B-8: Banner de advertencia en módulos 1-9
# ═══════════════════════════════════════════

WARNING_BANNER = '''
            <!-- ⚠️ Banner de Advertencia: Datos de Estudiantes -->
            <div class="bg-amber-50 border border-amber-200 rounded-2xl p-5 mb-8 flex gap-4 items-start">
                <div class="flex-shrink-0 w-10 h-10 bg-amber-100 rounded-xl flex items-center justify-center text-xl">⚠️</div>
                <div>
                    <h3 class="font-bold text-amber-900 mb-1">Importante: Protección de Datos de Estudiantes</h3>
                    <p class="text-sm text-amber-800 leading-relaxed m-0">Nunca ingrese nombres, cédulas, calificaciones ni datos personales de estudiantes en herramientas de IA de terceros (ChatGPT, Gemini, Copilot, etc.). Use siempre <strong>descripciones genéricas</strong> como "estudiante de sétimo con dificultad lectora". Consulte nuestra <a href="politica-privacidad.html" class="text-amber-900 underline font-semibold hover:text-amber-700">Política de Privacidad</a> y la <a href="politica-privacidad.html" class="text-amber-900 underline font-semibold hover:text-amber-700">Ley 8968 / PRODHAB</a>.</p>
                </div>
            </div>
'''

b8_count = 0

for i in range(1, 10):
    filepath = os.path.join(PROJECT_DIR, f"modulo-{i}.html")
    if not os.path.exists(filepath):
        print(f"  ⚠️  modulo-{i}.html no existe, saltando...")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if banner already exists
    if "Protección de Datos de Estudiantes" in content:
        print(f"  ⏭️  modulo-{i}.html — banner ya existe")
        continue
    
    # Insert after the hero section (after the closing </div> of the hero)
    # Look for the infografías section or the content grid as insertion point
    # The pattern is: after the hero closing </div> and before the next section
    
    # Strategy: insert right after <!-- Hero Section --> closing block
    # Most modules have a pattern like: </div>\n\n            \n            <!-- ... next section
    # Let's find the marker for Infografías or Content Grid
    
    # For modules with infografías section:
    marker_info = '<!-- Recursos / Infografías Section -->'
    marker_content = '<!-- Content Grid'
    
    if marker_info in content:
        content = content.replace(marker_info, WARNING_BANNER + '\n            ' + marker_info)
    elif marker_content in content:
        content = content.replace(marker_content, WARNING_BANNER + '\n            ' + marker_content, 1)
    else:
        # Fallback: insert after <main ...> ... first big </div> block
        # Find the hero section end pattern
        hero_end = '</button>\n                    </div>\n                </div>\n            </div>'
        if hero_end in content:
            content = content.replace(hero_end, hero_end + '\n' + WARNING_BANNER, 1)
        else:
            print(f"  ❌ modulo-{i}.html — no se encontró punto de inserción")
            continue
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    b8_count += 1
    print(f"  ✅ B-8 modulo-{i}.html — banner de advertencia agregado")

print(f"\n🏁 B-8: {b8_count} módulos actualizados con banner de advertencia.")
