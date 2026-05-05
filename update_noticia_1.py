import re

with open("index.html", "r") as f:
    content = f.read()

top_split = '<main class="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 overflow-y-auto">'
parts = content.split(top_split)
top_boilerplate = parts[0] + top_split + "\n"

bottom_split = '</main>'
bottom_boilerplate = "\n" + bottom_split + parts[1].split(bottom_split)[1]

noticia_1_content = """
            <div class="mb-8">
                <a href="notificaciones.html" class="inline-flex items-center gap-2 text-mep-blue hover:underline mb-6 font-medium">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                    </svg>
                    Volver a Notificaciones
                </a>
                
                <div class="flex items-center gap-3 mb-4">
                    <span class="px-3 py-1 bg-blue-100 text-mep-blue text-sm font-bold rounded-full">Actualización</span>
                    <span class="text-gray-500 text-sm">15 de Mayo, 2026</span>
                </div>
                
                <h1 class="text-3xl md:text-4xl font-extrabold text-gray-900 mb-6">Noticia 1: Panorama Actual del Uso de IA en Educación Secundaria</h1>
            </div>

            <div class="bg-white rounded-2xl border border-gray-100 shadow-sm p-6 lg:p-10 mb-10">
                <div class="prose max-w-none text-gray-700 space-y-6">
                    <p class="text-lg leading-relaxed">
                        En los últimos meses se ha acelerado el uso de IA (especialmente generativa) en educación secundaria, con avances en políticas, experimentos pedagógicos y también alertas sobre riesgos. A continuación te resumo las tendencias más recientes en prensa, organismos internacionales y algunos ejemplos cercanos a Costa Rica.
                    </p>

                    <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Tendencias globales recientes</h2>
                    <ul class="list-disc pl-5 space-y-2">
                        <li>Varios países reportan que la IA generativa (ChatGPT, Gemini, etc.) pasó en 3 cursos de ser curiosidad a integrarse en la rutina de docentes y estudiantes de secundaria y universidad; el debate ya no es “si usarla” sino “cómo hacerlo bien”. <a href="https://elpais.com/economia/formacion/2026-04-16/cuando-la-inteligencia-artificial-hace-los-deberes-la-educacion-cambia-de-reglas.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></li>
                        <li>Encuestas en Europa muestran que entre 40% y 80% de adolescentes usan IA para estudiar en casa, muchas veces sin supervisión adulta; en España, un dato oficial del INE indica que 59% de personas de 16‑24 años ya la usan con fines de estudio. <a href="https://elpais.com/educacion/2025-11-30/los-alumnos-se-lanzan-a-usar-la-ia-para-estudiar-crece-sin-control-como-paso-con-las-redes-sociales.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></li>
                        <li>La OCDE ha difundido resultados (recogidos en prensa especializada) que apuntan a que la IA generativa mejora el rendimiento educativo solo cuando existe supervisión docente y un diseño pedagógico claro, alertando sobre riesgos de uso automático o sustitución de tareas sin reflexión. <a href="https://www.infobae.com/tecno/2026/03/18/el-uso-de-ia-generativa-mejora-el-rendimiento-educativo-solo-con-supervision-docente-afirma-la-ocde/" target="_blank" class="text-mep-blue hover:underline">[infobae]</a></li>
                    </ul>

                    <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Lineamientos y debates de política educativa</h2>
                    <ul class="list-disc pl-5 space-y-2">
                        <li>La UNESCO publicó en abril 2026 lineamientos sobre IA en educación, destacando su potencial para personalizar aprendizajes y apoyar al profesorado, pero insistiendo en marcos éticos, protección de datos y equidad en el acceso. <a href="https://www.unesco.org/es/digital-education/artificial-intelligence" target="_blank" class="text-mep-blue hover:underline">[unesco]</a></li>
                        <li>En España, el Ministerio de Educación actualizó en 2022 el marco de competencia digital docente e incluyó una guía específica sobre uso de IA generativa en el aula, centrada en formación de profesorado, transparencia y protección de datos de estudiantes. <a href="https://elpais.com/economia/formacion/2026-04-16/cuando-la-inteligencia-artificial-hace-los-deberes-la-educacion-cambia-de-reglas.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></li>
                        <li>Paralelamente, se tramita una ley para protección de menores en entornos digitales que permitirá a los centros regular el uso de móviles y reforzar la educación en hábitos de pantalla, en un contexto donde el acceso a IA se mezcla con redes sociales y otras plataformas. <a href="https://elpais.com/economia/formacion/2026-04-16/cuando-la-inteligencia-artificial-hace-los-deberes-la-educacion-cambia-de-reglas.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></li>
                    </ul>

                    <h3 class="text-xl font-bold text-gray-900 mt-6 mb-3">Ejemplo de medidas recientes</h3>
                    <div class="overflow-x-auto">
                        <table class="min-w-full bg-white border border-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th class="py-3 px-4 border-b text-left text-sm font-semibold text-gray-900">Aspecto</th>
                                    <th class="py-3 px-4 border-b text-left text-sm font-semibold text-gray-900">Medida reciente mencionada en noticias</th>
                                    <th class="py-3 px-4 border-b text-left text-sm font-semibold text-gray-900">País/organismo</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-200 text-sm">
                                <tr>
                                    <td class="py-3 px-4">Formación docente en IA</td>
                                    <td class="py-3 px-4">Guía oficial sobre IA generativa y competencia digital docente. <a href="https://elpais.com/economia/formacion/2026-04-16/cuando-la-inteligencia-artificial-hace-los-deberes-la-educacion-cambia-de-reglas.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></td>
                                    <td class="py-3 px-4">España</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4">Regulación de menores</td>
                                    <td class="py-3 px-4">Proyecto de ley para regular móviles y hábitos de pantalla en centros educativos. <a href="https://elpais.com/economia/formacion/2026-04-16/cuando-la-inteligencia-artificial-hace-los-deberes-la-educacion-cambia-de-reglas.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></td>
                                    <td class="py-3 px-4">España</td>
                                </tr>
                                <tr>
                                    <td class="py-3 px-4">Orientación global</td>
                                    <td class="py-3 px-4">Marco UNESCO sobre IA en educación, énfasis ético y de equidad. <a href="https://www.unesco.org/es/digital-education/artificial-intelligence" target="_blank" class="text-mep-blue hover:underline">[unesco]</a></td>
                                    <td class="py-3 px-4">UNESCO</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Prácticas en aula de secundaria</h2>
                    <ul class="list-disc pl-5 space-y-2">
                        <li>Una revisión sistemática de 43 estudios (2021‑2024) sobre educación secundaria identifica cuatro estrategias de implementación de IA generativa: actividades puntuales (ejercicios aislados), proyectos interdisciplinarios, unidades curriculares completas y sistemas de tutoría automatizada. <a href="https://revistas.ucr.ac.cr/index.php/reducacion/article/download/4009/5575/24454" target="_blank" class="text-mep-blue hover:underline">[revistas.ucr.ac]</a></li>
                        <li>ChatGPT aparece como la herramienta más utilizada en esos estudios (presente en 26 de 43 artículos), condicionando tipos de uso como redacción guiada, retroalimentación automática de textos y apoyo en resolución de problemas. <a href="https://revistas.ucr.ac.cr/index.php/reducacion/article/download/4009/5575/24454" target="_blank" class="text-mep-blue hover:underline">[revistas.ucr.ac]</a></li>
                        <li>Otros trabajos recientes recogen experiencias de centros de secundaria que usan sistemas de IA para generar rúbricas y calificaciones coherentes, con el fin de reducir la subjetividad en la corrección, aunque todavía exigen revisión final del docente. <a href="https://openwebinars.net/blog/inteligencia-artificial-en-educacion-usos-ventajas-y-riesgos/" target="_blank" class="text-mep-blue hover:underline">[openwebinars]</a></li>
                    </ul>

                    <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Riesgos y desafíos que resaltan las noticias</h2>
                    <ul class="list-disc pl-5 space-y-2">
                        <li>Artículos de divulgación científica subrayan que, aunque la IA puede ayudar a personalizar el aprendizaje y detectar dificultades, también introduce desafíos: sesgos en los modelos, dependencia tecnológica, riesgos de copia y debilitamiento de habilidades de escritura y razonamiento si se usa sin mediación pedagógica. <a href="https://ciencia.unam.mx/leer/1633/grandes-desafios-del-uso-de-la-ia-en-la-escuela-" target="_blank" class="text-mep-blue hover:underline">[ciencia.unam]</a></li>
                        <li>La prensa educativa ha señalado que muchos centros “entraron en la era de la IA sin manual de instrucciones”, es decir, sin protocolos claros sobre qué se permite, cómo evaluar tareas realizadas con IA y cómo educar en un uso crítico. <a href="https://elpais.com/economia/formacion/2026-04-16/cuando-la-inteligencia-artificial-hace-los-deberes-la-educacion-cambia-de-reglas.html" target="_blank" class="text-mep-blue hover:underline">[elpais]</a></li>
                        <li>Se advierte que las grandes brechas de conectividad y formación docente pueden hacer que los beneficios de la IA se concentren en colegios con más recursos, ampliando la desigualdad educativa si no se acompaña de políticas de equidad. <a href="https://www.unesco.org/es/digital-education/artificial-intelligence" target="_blank" class="text-mep-blue hover:underline">[unesco]</a></li>
                    </ul>

                    <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Ejemplos recientes en el contexto latinoamericano y Costa Rica</h2>
                    <ul class="list-disc pl-5 space-y-2">
                        <li>En Argentina, se habla de un “boom de la inteligencia artificial en la educación”: la Ciudad de Buenos Aires anunció la ampliación de programas de IA incluso en nivel inicial, mientras empresas venden chatbots personalizados para escuelas, lo que intensifica el debate sobre comercialización y protección de datos de menores. <a href="https://www.pagina12.com.ar/2026/04/10/que-hay-detras-del-boom-de-la-inteligencia-artificial-en-la-educacion-riesgo-o-beneficio/" target="_blank" class="text-mep-blue hover:underline">[pagina12.com]</a></li>
                        <li>En Costa Rica, notas recientes destacan el uso de herramientas de IA en aulas para mejorar el rendimiento estudiantil y reducir carga de trabajo docente, con evidencia de aumentos en calificaciones cuando la integración se hace de forma intencional y acompañada. <a href="https://ufidelitas.ac.cr/blog/educacion/impacto-de-la-inteligencia-artificial-en-la-educacion/" target="_blank" class="text-mep-blue hover:underline">[ufidelitas.ac]</a></li>
                        <li>El MEP reportó actividades donde 240 colegiales de colegios públicos y privados participaron en experiencias de aproximación a IA y tecnología en el mundo empresarial, vinculadas al Bachillerato Internacional y a teoría del conocimiento, mostrando un enfoque de orientación vocacional y ética de la tecnología. <a href="https://www.mep.go.cr/noticias/240-colegiales-aprenden-uso-inteligencia-artificial-tecnologia-mundo-empresarial" target="_blank" class="text-mep-blue hover:underline">[mep.go]</a></li>
                    </ul>

                    <div class="bg-blue-50 border-l-4 border-mep-blue p-6 mt-8 rounded-r-lg">
                        <p class="font-bold text-gray-900 text-lg mb-2">💡 ¿Necesitas aterrizar esto a tu contexto?</p>
                        <p class="text-gray-700">En la comunidad podemos debatir propuestas concretas para tu colegio, por ejemplo: criterios de política interna, diseño de proyectos disciplinarios o un protocolo de uso de IA para estudiantes de III ciclo y diversificado.</p>
                    </div>
                </div>
            </div>
"""

with open("noticia-1.html", "w") as f:
    f.write(top_boilerplate + noticia_1_content + bottom_boilerplate)
