import re

def update_modulos():
    with open("modulos.html", "r", encoding="utf-8") as f:
        content = f.read()

    # A-4: Fix Marco Legal
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

    # B-4: Fix Modulo 2 and Modulo 4
    # Current Módulo 2 card: href="modulo-2.html" -> we change it to href="privacidad-etica.html"
    content = content.replace(
        '<a href="modulo-2.html" data-nivel="secundaria" data-proposito="retroalimentacion" data-trimestre="t1" data-tipo="ficha" data-tags="etico"',
        '<a href="privacidad-etica.html" data-nivel="secundaria" data-proposito="retroalimentacion" data-trimestre="t1" data-tipo="ficha" data-tags="etico"'
    )

    # A-3: Modulos 7, 8, 9 Próximamente
    def proximamente_replace(match):
        href = match.group(1)
        classes = match.group(2)
        inner = match.group(3)
        
        # Change <a> to <div>, add proximamente classes
        # The user requested classes: opacity-60 cursor-not-allowed pointer-events-none
        classes = classes.replace('hover:shadow-lg hover:-translate-y-1', 'opacity-60 cursor-not-allowed pointer-events-none')
        classes = classes.replace('cursor-pointer', '')
        
        # Change Activo to Próximamente
        inner = re.sub(
            r'<span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>',
            '<span class="px-2.5 py-1 bg-gray-200 text-gray-600 text-xs font-semibold rounded-full border border-gray-300">Próximamente</span>',
            inner
        )
        
        # Add Disponible text below title
        inner = re.sub(
            r'(<h3 class="[^"]+">)(.*?)(</h3>)',
            r'\1\2\3\n                        <p class="text-xs text-gray-500 font-medium mb-2 mt-1">Disponible T3 2026</p>',
            inner
        )
        
        return f'<div {classes}>\n{inner}</div>'

    pattern_7 = r'<a href="(modulo-7\.html)" ([^>]*)>(.*?)</a>'
    content = re.sub(pattern_7, proximamente_replace, content, flags=re.DOTALL)

    pattern_8 = r'<a href="(modulo-8\.html)" ([^>]*)>(.*?)</a>'
    content = re.sub(pattern_8, proximamente_replace, content, flags=re.DOTALL)

    pattern_9 = r'<a href="(modulo-9\.html)" ([^>]*)>(.*?)</a>'
    content = re.sub(pattern_9, proximamente_replace, content, flags=re.DOTALL)

    with open("modulos.html", "w", encoding="utf-8") as f:
        f.write(content)
        
update_modulos()
