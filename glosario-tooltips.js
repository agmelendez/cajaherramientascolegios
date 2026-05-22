/**
 * Sistema de Glosario Inline con Tooltips Accesibles (WCAG AA)
 * Caja de Herramientas para Docentes de Colegios - UCR / CIOdD
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Inicializar base de datos de términos
    const termsData = window.GLOSARIO_DATA;
    if (!termsData) {
        console.warn('Glosario: Base de datos "window.GLOSARIO_DATA" no encontrada.');
        return;
    }

    // 2. Obtener perfil del docente
    let userProfile = null;
    try {
        const storedProfile = localStorage.getItem('caja_docente_perfil');
        if (storedProfile) {
            userProfile = JSON.parse(storedProfile);
        }
    } catch (e) {
        console.error('Error al parsear el perfil de caja_docente_perfil', e);
    }

    // 3. Crear el contenedor único del Tooltip en el body
    const tooltipEl = document.createElement('div');
    tooltipEl.id = 'glosario-tooltip-container';
    tooltipEl.role = 'tooltip';
    tooltipEl.setAttribute('aria-hidden', 'true');
    tooltipEl.className = 'fixed z-[100] max-w-[340px] w-[90vw] p-4 bg-white/95 backdrop-blur-md border border-gray-100 shadow-2xl rounded-2xl text-slate-800 transition-all duration-200 opacity-0 scale-95 pointer-events-none text-left';
    tooltipEl.innerHTML = `
        <div class="flex flex-col gap-2">
            <div class="flex items-center justify-between border-b border-slate-100 pb-2">
                <h4 id="tooltip-title" class="font-bold text-slate-900 text-sm tracking-tight"></h4>
                <span id="tooltip-category" class="text-[10px] font-semibold tracking-wider uppercase px-2 py-0.5 rounded-full"></span>
            </div>
            <p id="tooltip-def" class="text-xs leading-relaxed text-slate-600 font-medium"></p>
            <div id="tooltip-analogy-box" class="bg-amber-50/60 border border-amber-100/50 rounded-lg p-2.5 my-0.5 text-xs text-amber-900/90 leading-normal flex gap-1.5 items-start">
                <span class="text-sm select-none">💡</span>
                <div>
                    <span class="font-bold block text-[10px] uppercase text-amber-700 tracking-wider">Analogía Sencilla</span>
                    <span id="tooltip-analogy"></span>
                </div>
            </div>
            <div id="tooltip-example-box" class="bg-blue-50/60 border border-blue-100/50 rounded-lg p-2.5 text-xs text-blue-900/90 leading-normal flex gap-1.5 items-start">
                <span class="text-sm select-none">🏫</span>
                <div>
                    <span class="font-bold block text-[10px] uppercase text-blue-700 tracking-wider">En el Aula</span>
                    <span id="tooltip-example"></span>
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(tooltipEl);

    // Variables de control de estado del tooltip
    let activeTrigger = null;
    let dismissProactiveTimeout = null;

    // 4. Buscar y preparar todos los términos marcados en la página
    const triggers = document.querySelectorAll('.glosario-term');
    
    triggers.forEach((trigger, index) => {
        const termId = trigger.getAttribute('data-term');
        if (!termId || !termsData[termId]) {
            console.warn(`Glosario: Término "${termId}" no configurado en la base de datos.`);
            return;
        }

        const data = termsData[termId];

        // Asegurar accesibilidad básica WCAG AA
        trigger.setAttribute('tabindex', '0');
        trigger.setAttribute('role', 'button');
        trigger.setAttribute('aria-haspopup', 'true');
        trigger.setAttribute('aria-expanded', 'false');
        trigger.setAttribute('id', `term-trigger-${termId}-${index}`);
        
        // Estilos base premium por clases Tailwind dinámicas
        trigger.className = 'glosario-term border-b-2 border-dotted border-mep-blue cursor-help hover:bg-mep-blue/5 focus:bg-mep-blue/10 focus:outline-none focus:ring-2 focus:ring-mep-blue/50 focus:ring-offset-1 rounded px-0.5 transition-all duration-150 inline font-semibold text-mep-blue';

        // Manejadores de eventos
        const show = (event) => {
            if (activeTrigger === trigger && tooltipEl.getAttribute('aria-hidden') === 'false') return;
            
            // Si el tooltip proactivo estaba activo y se interactúa con otro término, se cierra el proactivo sin problema
            if (activeTrigger && activeTrigger !== trigger) {
                hide();
            }

            activeTrigger = trigger;
            fillTooltip(data);
            positionTooltip(trigger);
            
            tooltipEl.setAttribute('aria-hidden', 'false');
            tooltipEl.classList.remove('opacity-0', 'scale-95', 'pointer-events-none');
            tooltipEl.classList.add('opacity-100', 'scale-100');
            trigger.setAttribute('aria-expanded', 'true');
        };

        const hide = () => {
            if (activeTrigger !== trigger) return;
            
            tooltipEl.setAttribute('aria-hidden', 'true');
            tooltipEl.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
            tooltipEl.classList.remove('opacity-100', 'scale-100');
            trigger.setAttribute('aria-expanded', 'false');
            activeTrigger = null;
        };

        // Eventos Hover
        trigger.addEventListener('mouseenter', show);
        trigger.addEventListener('mouseleave', (e) => {
            // Permitir mover el mouse al tooltip sin cerrarlo si quisiéramos copiar texto,
            // pero para tooltips estándar un pequeño delay o cierre directo funciona bien.
            // Para simplicidad robusta, cerramos en mouseleave
            hide();
        });

        // Eventos Teclado (Accesibilidad)
        trigger.addEventListener('focus', show);
        trigger.addEventListener('blur', hide);

        // Eventos Táctiles / Click (Móviles)
        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (activeTrigger === trigger && tooltipEl.getAttribute('aria-hidden') === 'false') {
                hide();
            } else {
                show(e);
            }
        });

        // Evento Escape para cerrar
        trigger.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' || e.key === 'Esc') {
                hide();
                trigger.focus();
            }
        });
    });

    // Cerrar tooltip si se hace click fuera
    document.addEventListener('click', (e) => {
        if (activeTrigger && !activeTrigger.contains(e.target) && !tooltipEl.contains(e.target)) {
            const currentTrigger = activeTrigger;
            // Hack temporal para disparar hide
            activeTrigger = currentTrigger;
            tooltipEl.setAttribute('aria-hidden', 'true');
            tooltipEl.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
            tooltipEl.classList.remove('opacity-100', 'scale-100');
            currentTrigger.setAttribute('aria-expanded', 'false');
            activeTrigger = null;
        }
    });

    // 5. Función para llenar datos del tooltip
    function fillTooltip(data) {
        document.getElementById('tooltip-title').textContent = data.title;
        const catEl = document.getElementById('tooltip-category');
        catEl.textContent = data.category;

        // Limpiar estilos previos de categoría
        catEl.className = 'text-[10px] font-semibold tracking-wider uppercase px-2 py-0.5 rounded-full';
        if (data.category === 'Técnico') {
            catEl.classList.add('bg-blue-100', 'text-blue-800');
        } else if (data.category === 'Pedagogía') {
            catEl.classList.add('bg-emerald-100', 'text-emerald-800');
        } else if (data.category === 'Ética') {
            catEl.classList.add('bg-amber-100', 'text-amber-800');
        } else {
            catEl.classList.add('bg-gray-100', 'text-gray-800');
        }

        document.getElementById('tooltip-def').textContent = data.simpleDef;
        document.getElementById('tooltip-analogy').textContent = data.analogy;
        document.getElementById('tooltip-example').textContent = data.classroomExample;
    }

    // 6. Posicionamiento dinámico preciso del tooltip
    function positionTooltip(trigger) {
        const triggerRect = trigger.getBoundingClientRect();
        const tooltipWidth = tooltipEl.offsetWidth || 340;
        const tooltipHeight = tooltipEl.offsetHeight || 220;
        
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;

        // Calcular posición ideal: arriba del término y centrado horizontalmente
        let top = triggerRect.top - tooltipHeight - 12;
        let left = triggerRect.left + (triggerRect.width / 2) - (tooltipWidth / 2);

        // Ajustar si se sale por arriba de la pantalla (colocar abajo del término)
        if (top < 14) {
            top = triggerRect.bottom + 12;
        }

        // Ajustar si se sale por la izquierda de la pantalla
        if (left < 14) {
            left = 14;
        }

        // Ajustar si se sale por la derecha de la pantalla
        if (left + tooltipWidth > viewportWidth - 14) {
            left = viewportWidth - tooltipWidth - 14;
        }

        tooltipEl.style.top = `${top}px`;
        tooltipEl.style.left = `${left}px`;
    }

    // Ocultar al hacer scroll o cambiar tamaño de ventana
    window.addEventListener('scroll', () => {
        if (activeTrigger) {
            // Ocultar directamente o reposicionar. Ocultar es mejor para no molestar la lectura
            const currentTrigger = activeTrigger;
            tooltipEl.setAttribute('aria-hidden', 'true');
            tooltipEl.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
            tooltipEl.classList.remove('opacity-100', 'scale-100');
            currentTrigger.setAttribute('aria-expanded', 'false');
            activeTrigger = null;
        }
    }, { passive: true });

    window.addEventListener('resize', () => {
        if (activeTrigger) {
            positionTooltip(activeTrigger);
        }
    });

    // 7. Implementar el Tooltip Proactivo para usuarios con 'ninguna' experiencia
    function initProactiveTooltip() {
        const isNoExp = userProfile && userProfile.experience === 'ninguna';
        const alreadyDismissed = sessionStorage.getItem('caja_docente_proactive_dismissed') === 'true';

        if (isNoExp && !alreadyDismissed) {
            const firstTerm = document.querySelector('.glosario-term');
            if (firstTerm) {
                // Pequeño retardo elegante para que el usuario asimile la página antes del tooltip
                dismissProactiveTimeout = setTimeout(() => {
                    // Resaltar visualmente el término
                    firstTerm.classList.add('ring-4', 'ring-mep-orange', 'ring-offset-2', 'animate-pulse');

                    // Llenar y mostrar el tooltip proactivo
                    const termId = firstTerm.getAttribute('data-term');
                    const data = termsData[termId];
                    fillTooltip(data);
                    
                    // Personalizar el tooltip con cabecera y botón especial de descarte
                    const titleContainer = document.getElementById('tooltip-title');
                    titleContainer.innerHTML = `<span class="text-mep-orange text-xs select-none">✨</span> Guía Interactiva`;

                    // Agregar botón de descarte si no existe
                    let dismissBtn = document.getElementById('dismiss-proactive-btn');
                    if (!dismissBtn) {
                        dismissBtn = document.createElement('button');
                        dismissBtn.id = 'dismiss-proactive-btn';
                        dismissBtn.className = 'mt-3 w-full text-xs font-semibold bg-mep-blue text-white py-2 px-4 rounded-xl hover:bg-blue-700 active:scale-[0.98] transition-all flex items-center justify-center gap-1.5 shadow-md shadow-mep-blue/10';
                        dismissBtn.innerHTML = `<span>¡Entendido!</span> <span class="text-[10px] opacity-75">Click para cerrar</span>`;
                        tooltipEl.querySelector('.flex.flex-col').appendChild(dismissBtn);
                        
                        dismissBtn.addEventListener('click', (e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            
                            // Desactivar resaltado
                            firstTerm.classList.remove('ring-4', 'ring-mep-orange', 'ring-offset-2', 'animate-pulse');
                            
                            // Guardar en sessionStorage para que sea una vez por sesión
                            sessionStorage.setItem('caja_docente_proactive_dismissed', 'true');
                            
                            // Animación de salida y limpieza
                            tooltipEl.setAttribute('aria-hidden', 'true');
                            tooltipEl.classList.add('opacity-0', 'scale-95', 'pointer-events-none');
                            tooltipEl.classList.remove('opacity-100', 'scale-100');
                            firstTerm.setAttribute('aria-expanded', 'false');
                            activeTrigger = null;
                            
                            // Quitar el botón del DOM para las siguientes interacciones normales
                            dismissBtn.remove();
                        });
                    }

                    // Forzar activación del tooltip
                    activeTrigger = firstTerm;
                    positionTooltip(firstTerm);
                    
                    tooltipEl.setAttribute('aria-hidden', 'false');
                    tooltipEl.classList.remove('opacity-0', 'scale-95', 'pointer-events-none');
                    tooltipEl.classList.add('opacity-100', 'scale-100');
                    firstTerm.setAttribute('aria-expanded', 'true');

                }, 1500); // 1.5 segundos de retardo elegante
            }
        }
    }

    // 8. Sistema de Adaptación de Contenidos por Niveles y Contexto Educativo (Sprint 5)
    function setLevelContent() {
        let profile = null;
        try {
            const storedProfile = localStorage.getItem('caja_docente_perfil');
            if (storedProfile) {
                profile = JSON.parse(storedProfile);
            }
        } catch (e) {
            console.error('Error al parsear el perfil', e);
        }

        // Si no hay perfil, cargamos valores por defecto seguros
        const level = profile ? profile.computedLevel : 'beginner'; // 'beginner' o 'advanced'
        const eduLevel = profile ? profile.level : 'primaria'; // 'primaria', 'secundaria', 'tecnica', 'adultos'

        console.log(`Caja de Herramientas: Aplicando adaptación de nivel [${level}] y nivel educativo [${eduLevel}]`);

        // A. Filtrado por Nivel de Complejidad (data-level="beginner|advanced")
        const levelElements = document.querySelectorAll('[data-level]');
        levelElements.forEach(el => {
            const elLevel = el.getAttribute('data-level');
            if (elLevel === level) {
                el.classList.remove('hidden');
            } else {
                el.classList.add('hidden');
            }
        });

        // B. Resaltado por Nivel Educativo (data-edu-level="primaria|secundaria|tecnica|adultos")
        const eduElements = document.querySelectorAll('[data-edu-level]');
        eduElements.forEach(el => {
            const elEduLevel = el.getAttribute('data-edu-level');
            
            // Remover clases previas de resalte para evitar duplicados
            el.classList.remove('ring-4', 'ring-mep-blue', 'bg-blue-50/40', 'opacity-65', 'scale-[1.01]', 'relative');
            const badge = el.querySelector('.edu-level-badge');
            if (badge) badge.remove();

            if (elEduLevel === eduLevel) {
                // Resaltar tarjeta coincidente
                el.classList.add('ring-4', 'ring-mep-blue', 'bg-blue-50/40', 'scale-[1.01]', 'relative');
                
                // Inyectar un badge elegante flotante "Recomendado para tu nivel"
                const badgeEl = document.createElement('div');
                badgeEl.className = 'edu-level-badge absolute -top-3 right-4 px-3 py-1 bg-mep-blue text-white text-[10px] font-black uppercase tracking-wider rounded-full shadow-md z-10';
                badgeEl.innerHTML = '✨ Recomendado para ti';
                el.appendChild(badgeEl);
            } else {
                // Atenuar sutilmente tarjetas no coincidentes
                el.classList.add('opacity-65');
            }
        });
    }

    // Iniciar con un pequeño retardo
    initProactiveTooltip();
    
    // Ejecutar la adaptación de contenidos
    setLevelContent();
});
