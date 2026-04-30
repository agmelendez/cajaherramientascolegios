import re

filepath = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios/public/modulos.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Search Bar and Filters with IDs
filters_html = """            <!-- Buscador y Filtros Avanzados -->
            <div class="bg-white p-5 rounded-2xl border border-gray-200 shadow-sm mb-8 flex flex-col gap-4">
                <div class="relative w-full">
                    <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                        <svg class="h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
                        </svg>
                    </div>
                    <input type="text" id="searchInput" placeholder="Buscar fichas, prompts, cápsulas..." class="w-full pl-11 pr-4 py-3 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-mep-blue focus:border-transparent transition-all bg-gray-50 hover:bg-white text-gray-900 placeholder-gray-500">
                </div>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
                    <select id="filterNivel" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-mep-blue bg-white text-gray-700 cursor-pointer text-sm font-medium hover:border-gray-300 transition-colors">
                        <option value="">Cualquier Nivel</option>
                        <option value="primaria">Primaria</option>
                        <option value="secundaria">Secundaria Académica</option>
                        <option value="ctp">CTP</option>
                        <option value="ipec">IPEC/CINDEA</option>
                    </select>
                    
                    <select id="filterProposito" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-mep-blue bg-white text-gray-700 cursor-pointer text-sm font-medium hover:border-gray-300 transition-colors">
                        <option value="">Cualquier Propósito</option>
                        <option value="ideas">Generar ideas</option>
                        <option value="analisis">Analizar información</option>
                        <option value="materiales">Diseñar materiales</option>
                        <option value="retroalimentacion">Retroalimentar</option>
                    </select>

                    <select id="filterTrimestre" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-mep-blue bg-white text-gray-700 cursor-pointer text-sm font-medium hover:border-gray-300 transition-colors">
                        <option value="">Cualquier Trimestre</option>
                        <option value="t1">T1 2026</option>
                        <option value="t2">T2 2026</option>
                        <option value="t3">T3 2026</option>
                    </select>
                    
                    <select id="filterTipo" class="w-full px-4 py-2.5 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-mep-blue bg-white text-gray-700 cursor-pointer text-sm font-medium hover:border-gray-300 transition-colors">
                        <option value="">Cualquier Tipo</option>
                        <option value="ficha">Fichas Didácticas</option>
                        <option value="prompt">Banco de Prompts</option>
                        <option value="instrumento">Instrumentos</option>
                    </select>
                </div>
                
                <div class="flex flex-wrap items-center gap-2 pt-3 border-t border-gray-100 mt-1">
                    <span class="text-xs font-semibold text-gray-400 uppercase tracking-wider mr-2">Filtros Rápidos:</span>
                    <button id="pill15min" class="px-3 py-1.5 rounded-full bg-gray-50 text-gray-600 border border-gray-200 hover:bg-gray-100 text-xs font-medium transition-colors cursor-pointer">Menos de 15 min</button>
                    <button id="pillDua" class="px-3 py-1.5 rounded-full bg-gray-50 text-gray-600 border border-gray-200 hover:bg-gray-100 text-xs font-medium transition-colors cursor-pointer">Inclusivo (DUA)</button>
                    <button id="pillEtica" class="px-3 py-1.5 rounded-full bg-gray-50 text-gray-600 border border-gray-200 hover:bg-gray-100 text-xs font-medium transition-colors cursor-pointer">Ética y Seguridad</button>
                    <button id="btnLimpiar" class="ml-auto text-sm text-gray-500 hover:text-mep-blue transition-colors font-medium cursor-pointer">Limpiar filtros</button>
                </div>
            </div>"""

content = re.sub(r'<!-- Buscador y Filtros Avanzados -->.*?</button>\s*</div>\s*</div>', filters_html, content, flags=re.DOTALL)


# 2. Update the Cards with data-* attributes
# M1
content = content.replace('<a href="modulo-1.html" class="block', '<a href="modulo-1.html" data-nivel="primaria" data-proposito="ideas" data-trimestre="t1" data-tipo="ficha" class="module-card block')
# M2
content = content.replace('<a href="modulo-2.html" class="block', '<a href="modulo-2.html" data-nivel="secundaria" data-proposito="retroalimentacion" data-trimestre="t1" data-tipo="ficha" data-tags="etico" class="module-card block')
# M3
content = content.replace('<a href="modulo-3.html" class="block', '<a href="modulo-3.html" data-nivel="secundaria" data-proposito="materiales" data-trimestre="t2" data-tipo="prompt" data-tags="dua" class="module-card block')
# M4
content = content.replace('<a href="modulo-4.html" class="block', '<a href="modulo-4.html" data-nivel="primaria" data-proposito="materiales" data-trimestre="t2" data-tipo="ficha" data-tags="dua" class="module-card block')
# M5
content = content.replace('<a href="modulo-5.html" class="block', '<a href="modulo-5.html" data-nivel="secundaria" data-proposito="analisis" data-trimestre="t3" data-tipo="instrumento" class="module-card block')
# M6
content = content.replace('<a href="modulo-6.html" class="block', '<a href="modulo-6.html" data-nivel="primaria" data-proposito="ideas" data-trimestre="t3" data-tipo="ficha" class="module-card block')

# 3. Add ID to grid and add dummy cards, plus the "No Results" container
dummy_cards = """
                <!-- Módulo 7 (Dummy) -->
                <a href="#" data-nivel="ctp" data-proposito="analisis" data-trimestre="t1" data-tipo="instrumento" data-tags="dua" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-red-400 to-red-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-red-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">⚙️</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-red-600 transition-colors">Módulo 7: IA en Colegios Técnicos</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Estrategias específicas para aplicar Inteligencia Artificial en especialidades técnicas y talleres del CTP.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 2 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 25 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 8 (Dummy) -->
                <a href="#" data-nivel="ipec" data-proposito="retroalimentacion" data-trimestre="t2" data-tipo="ficha" data-duracion="corta" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-teal-400 to-teal-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-teal-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">🌙</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-teal-600 transition-colors">Módulo 8: Jóvenes y Adultos</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Cómo utilizar la IA para dar retroalimentación rápida a estudiantes de IPEC y CINDEA en modalidades nocturnas.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 1 tema</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 12 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 9 (Dummy) -->
                <a href="#" data-nivel="primaria" data-proposito="ideas" data-trimestre="t1" data-tipo="prompt" data-duracion="corta" data-tags="etico" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-pink-400 to-pink-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-pink-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">⚡</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-pink-600 transition-colors">Módulo 9: Micro-Prompts</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Colección de prompts ultracortos para generar ideas de clase en menos de 1 minuto asegurando ética.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 1 tema</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 8 min</div>
                        </div>
                    </div>
                </a>
            </div>
            
            <div id="noResults" class="hidden text-center py-16">
                <div class="text-6xl mb-4">🔍</div>
                <h3 class="text-xl font-bold text-gray-900 mb-2">No hay resultados</h3>
                <p class="text-gray-500">Ningún módulo coincide con los filtros seleccionados.</p>
                <button onclick="document.getElementById('btnLimpiar').click()" class="mt-4 px-4 py-2 bg-blue-50 text-mep-blue font-medium rounded-lg hover:bg-blue-100 transition-colors">Limpiar filtros</button>
            </div>
"""

content = content.replace('<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">', '<div id="modulesGrid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">')
content = content.replace('</a>\n            </div>\n\n        </main>', f'</a>{dummy_cards}\n\n        </main>')

# 4. Inject script before closing body
content = content.replace('</body>', '    <script src="modulos-filter.js"></script>\n</body>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("modulos.html updated successfully.")
