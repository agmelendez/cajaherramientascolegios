import re

with open("modulos.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the grid content manually since we know its structure and what it needs to be.
# We will just write the inner HTML for <div id="modulesGrid" class="...">
# I'll preserve the exact Tailwind classes for each card.

grid_start = content.find('<div id="modulesGrid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">')
grid_end = content.find('</div>\n            \n            <div id="noResults"')

new_grid = '''<div id="modulesGrid" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
                <!-- Módulo 1 -->
                <a href="modulo-1.html" data-nivel="primaria" data-proposito="ideas" data-trimestre="t1" data-tipo="ficha" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-blue-400 to-mep-blue"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">📚</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-mep-blue transition-colors">Módulo 1: IA en Educación</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Introducción a los conceptos básicos de Inteligencia Artificial y sus aplicaciones en el contexto educativo costarricense.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 4 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 42 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 2 -->
                <a href="modulo-2.html" data-nivel="secundaria" data-proposito="retroalimentacion" data-trimestre="t1" data-tipo="ficha" data-tags="etico" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-emerald-400 to-mep-green"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-emerald-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">🔒</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-mep-green transition-colors">Módulo 2: Ética y Privacidad</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Protección de datos, privacidad y consideraciones éticas en el uso de herramientas de IA en el aula.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 3 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 38 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 3 -->
                <a href="modulo-3.html" data-nivel="secundaria" data-proposito="materiales" data-trimestre="t2" data-tipo="prompt" data-tags="dua" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-orange-400 to-mep-orange"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-orange-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">💬</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-mep-orange transition-colors">Módulo 3: Prompts Efectivos</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Técnicas avanzadas para crear prompts efectivos que maximicen los resultados con herramientas de IA.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 4 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 52 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 4 -->
                <a href="modulo-4.html" data-nivel="primaria" data-proposito="materiales" data-trimestre="t2" data-tipo="ficha" data-tags="dua" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-gray-300 to-gray-500"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-gray-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">🛠️</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-gray-600 transition-colors">Módulo 4: Herramientas Prácticas</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Casos de uso reales y ejemplos prácticos de cómo integrar herramientas de IA en diferentes asignaturas.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 5 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 67 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 5 -->
                <a href="modulo-5.html" data-nivel="primaria" data-proposito="materiales" data-trimestre="t2" data-tipo="ficha" data-tags="dua" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-gray-300 to-gray-500"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-gray-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">🎯</div>
                            <span class="px-2.5 py-1 bg-yellow-100 text-yellow-700 text-xs font-semibold rounded-full border border-yellow-200">Borrador</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-gray-600 transition-colors">Módulo 5: Aplicaciones Prácticas</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Profundización en la aplicación de metodologías de IA con casos prácticos avanzados.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 5 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 67 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 6 -->
                <a href="modulo-6.html" data-nivel="secundaria" data-proposito="analisis" data-trimestre="t3" data-tipo="instrumento" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-blue-400 to-mep-blue"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">📊</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-mep-blue transition-colors">Módulo 6: Análisis de Datos</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Cómo utilizar IA para analizar datos educativos y tomar decisiones basadas en evidencia y evaluación continua.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 3 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 35 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 7 -->
                <a href="modulo-7.html" data-nivel="primaria" data-proposito="ideas" data-trimestre="t3" data-tipo="ficha" class="module-card block bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300 overflow-hidden flex flex-col cursor-pointer group">
                    <div class="h-2 bg-gradient-to-r from-purple-400 to-purple-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-purple-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">🤖</div>
                            <span class="px-2.5 py-1 bg-green-100 text-green-700 text-xs font-semibold rounded-full border border-green-200">Activo</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-purple-600 transition-colors">Módulo 7: Herramientas Especializadas</h3>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Exploración de herramientas específicas como ChatGPT, Gemini, Copilot y sus características únicas en pedagogía.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 4 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 48 min</div>
                        </div>
                    </div>
                </a>

                <!-- Módulo 8 (Dummy) -->
                <div class="module-card modulo-proximamente block bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden flex flex-col group opacity-60 cursor-not-allowed pointer-events-none" aria-disabled="true">
                    <div class="h-2 bg-gradient-to-r from-red-400 to-red-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-red-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">⚙️</div>
                            <span class="px-2.5 py-1 bg-gray-200 text-gray-600 text-xs font-semibold rounded-full border border-gray-300">Próximamente</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-red-600 transition-colors">Módulo 8: IA en Colegios Técnicos</h3>
                        <p class="text-xs text-gray-500 font-medium mb-2 mt-1">Disponible T3 2026</p>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Estrategias específicas para aplicar Inteligencia Artificial en especialidades técnicas y talleres del CTP.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 2 temas</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 25 min</div>
                        </div>
                    </div>
                </div>

                <!-- Módulo 9 (Dummy) -->
                <div class="module-card modulo-proximamente block bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden flex flex-col group opacity-60 cursor-not-allowed pointer-events-none" aria-disabled="true">
                    <div class="h-2 bg-gradient-to-r from-teal-400 to-teal-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-teal-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">🌙</div>
                            <span class="px-2.5 py-1 bg-gray-200 text-gray-600 text-xs font-semibold rounded-full border border-gray-300">Próximamente</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-teal-600 transition-colors">Módulo 9: Jóvenes y Adultos</h3>
                        <p class="text-xs text-gray-500 font-medium mb-2 mt-1">Disponible T3 2026</p>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Cómo utilizar la IA para dar retroalimentación rápida a estudiantes de IPEC y CINDEA en modalidades nocturnas.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 1 tema</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 12 min</div>
                        </div>
                    </div>
                </div>

                <!-- Módulo 10 (Dummy) -->
                <div class="module-card modulo-proximamente block bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden flex flex-col group opacity-60 cursor-not-allowed pointer-events-none" aria-disabled="true">
                    <div class="h-2 bg-gradient-to-r from-pink-400 to-pink-600"></div>
                    <div class="p-6 flex flex-col flex-1">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-12 h-12 bg-pink-50 rounded-xl flex items-center justify-center text-2xl group-hover:scale-110 transition-transform">⚡</div>
                            <span class="px-2.5 py-1 bg-gray-200 text-gray-600 text-xs font-semibold rounded-full border border-gray-300">Próximamente</span>
                        </div>
                        <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-pink-600 transition-colors">Módulo 10: Micro-Prompts</h3>
                        <p class="text-xs text-gray-500 font-medium mb-2 mt-1">Disponible T3 2026</p>
                        <p class="text-sm text-gray-500 mb-6 flex-1">Colección de prompts ultracortos para generar ideas de clase en menos de 1 minuto asegurando ética.</p>
                        
                        <div class="pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path></svg> 1 tema</div>
                            <div class="flex items-center gap-1.5"><svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> 8 min</div>
                        </div>
                    </div>
                </div>
'''

new_content = content[:grid_start] + new_grid + content[grid_end:]

with open("modulos.html", "w", encoding="utf-8") as f:
    f.write(new_content)
    
print("Updated modulos.html grid.")
