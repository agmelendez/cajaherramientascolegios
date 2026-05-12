import re

with open("modulos.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix Marco Legal
content = content.replace(
    '''                    <ul class="space-y-3">
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a></li>
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Servicio</a></li>
                        <li><a href="#" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Cumplimiento RGPD</a></li>
                    </ul>''',
    '''                    <ul class="space-y-3">
                        <li><a href="politica-privacidad.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Política de Privacidad</a></li>
                        <li><a href="terminos-uso.html" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Términos de Uso</a></li>
                        <li><a href="politica-privacidad.html#ley8968" class="text-sm text-gray-400 hover:text-white transition-colors flex items-center gap-2"><span>→</span> Ley 8968 / PRODHAB</a></li>
                    </ul>'''
)

# Find modules grid
start_idx = content.find('<div id="modulesGrid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">')
end_idx = content.find('</div>\n            \n            <div id="noResults"')
grid_content = content[start_idx:end_idx]

# We want to reconstruct the grid with the correct modules:
# 1. IA en Educación (modulo-1.html)
# 2. Ética y Privacidad (privacidad-etica.html)
# 3. Prompts Efectivos (modulo-3.html)
# 4. Herramientas Prácticas (modulo-2.html)
# 5. Aplicaciones Prácticas (modulo-4.html)
# 6. Análisis de Datos (modulo-5.html)
# 7. IA en Colegios Técnicos (modulo-7.html) -> Próximamente
# 8. Jóvenes y Adultos (modulo-8.html) -> Próximamente
# 9. Micro-Prompts (modulo-9.html) -> Próximamente
# Notice we are dropping Herramientas Especializadas (modulo-6.html) or maybe that is what became 6? The user said 7,8,9 proximamente. If I include Herramientas Prácticas, I have 10 modules total if I keep Herramientas Especializadas. The user specifically listed "Módulo 5: Aplicaciones Prácticas", so they are just renumbering.
