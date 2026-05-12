#!/usr/bin/env python3
"""
B-7: Corregir footers RGPD en todos los archivos HTML.
- Reemplaza "Cumplimiento RGPD" → "Ley 8968 / PRODHAB" con enlace a politica-privacidad.html
- Actualiza "Política de Privacidad" href="#" → href="politica-privacidad.html"
- Actualiza "Términos de Servicio" href="#" → href="terminos-uso.html"
"""

import os
import re
import glob

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All HTML files in the project root
html_files = glob.glob(os.path.join(PROJECT_DIR, "*.html"))

changes_made = 0

for filepath in sorted(html_files):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # 1. Replace "Cumplimiento RGPD" with "Ley 8968 / PRODHAB" and fix href
    content = content.replace(
        '<a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Cumplimiento RGPD</a>',
        '<a href="politica-privacidad.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Ley 8968 / PRODHAB</a>'
    )
    
    # 2. Fix "Política de Privacidad" href="#" → href="politica-privacidad.html"
    content = content.replace(
        '<a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a>',
        '<a href="politica-privacidad.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a>'
    )
    
    # 3. Fix "Términos de Servicio" href="#" → href="terminos-uso.html"
    content = content.replace(
        '<a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Servicio</a>',
        '<a href="terminos-uso.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Servicio</a>'
    )
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        changes_made += 1
        print(f"  ✅ {filename} — footer actualizado")
    else:
        print(f"  ⏭️  {filename} — sin cambios necesarios")

print(f"\n🏁 Total: {changes_made} archivos actualizados.")
