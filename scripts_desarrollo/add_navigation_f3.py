"""
F3 — Navegación Secuencial + Prerequisitos
Agrega a cada módulo (M1–M9):
  1. Barra de navegación ← Anterior / Siguiente → antes de </main>
  2. Banner de prerequisito (M3–M9) tras el banner de advertencia ética
"""

import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Configuración de cada módulo ──────────────────────────────────────────────
MODULES = {
    1: {
        "label": "Fundamentos de IA en Educación",
        "prev": None,
        "next": (2, "Ética y Privacidad"),
        "prereq": None,
    },
    2: {
        "label": "Ética y Privacidad",
        "prev": (1, "Fundamentos de IA"),
        "next": (3, "Aplicaciones en el Aula"),
        "prereq": None,
    },
    3: {
        "label": "Aplicaciones en el Aula (REAC y DUA)",
        "prev": (2, "Ética y Privacidad"),
        "next": (4, "Herramientas Prácticas"),
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-1.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 1: Fundamentos de IA</a> "
                  "y <a href=\"modulo-2.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 2: Ética y Privacidad</a> primero.",
    },
    4: {
        "label": "Herramientas Prácticas de IA",
        "prev": (3, "Aplicaciones en el Aula"),
        "next": (5, "Aplicaciones Prácticas"),
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-3.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 3: Aplicaciones en el Aula</a> primero.",
    },
    5: {
        "label": "Aplicaciones Prácticas",
        "prev": (4, "Herramientas Prácticas"),
        "next": (6, "Análisis de Datos con IA"),
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-4.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 4: Herramientas Prácticas</a> primero.",
    },
    6: {
        "label": "Análisis de Datos con IA",
        "prev": (5, "Aplicaciones Prácticas"),
        "next": (7, "Comparativa de Herramientas Especializadas"),
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-4.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 4: Herramientas Prácticas</a> primero.",
    },
    7: {
        "label": "Comparativa de Herramientas Especializadas",
        "prev": (6, "Análisis de Datos con IA"),
        "next": (8, "IA en Colegios Técnicos"),
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-4.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 4: Herramientas Prácticas</a> primero.",
    },
    8: {
        "label": "IA en Colegios Técnicos (CTP)",
        "prev": (7, "Herramientas Especializadas"),
        "next": (9, "Jóvenes y Adultos (IPEC/CINDEA)"),
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-2.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 2: Ética y Privacidad</a> "
                  "y <a href=\"modulo-4.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 4: Herramientas Prácticas</a> primero.",
    },
    9: {
        "label": "Jóvenes y Adultos (IPEC/CINDEA)",
        "prev": (8, "IA en Colegios Técnicos"),
        "next": None,
        "prereq": "Para aprovechar mejor este módulo, le recomendamos haber revisado "
                  "<a href=\"modulo-2.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 2: Ética y Privacidad</a> "
                  "y <a href=\"modulo-4.html\" class=\"font-bold underline hover:text-blue-900\">Módulo 4: Herramientas Prácticas</a> primero.",
    },
}


def build_nav(mod_num, cfg):
    """Genera el HTML de la barra de navegación anterior/siguiente."""
    prev = cfg["prev"]
    nxt  = cfg["next"]

    # Botón Anterior
    if prev:
        btn_prev = f"""
        <a href="modulo-{prev[0]}.html"
           class="flex items-center gap-3 px-5 py-3 bg-white border border-gray-200
                  rounded-xl text-gray-600 hover:bg-gray-50 hover:border-gray-300
                  font-medium transition-all group">
            <svg class="w-4 h-4 flex-shrink-0 group-hover:-translate-x-1 transition-transform"
                 fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M15 19l-7-7 7-7"/>
            </svg>
            <div class="hidden sm:block text-left">
                <div class="text-xs text-gray-400">Anterior</div>
                <div class="text-sm font-semibold">{prev[1]}</div>
            </div>
        </a>"""
    else:
        btn_prev = '<div class="invisible w-10"></div>'  # ocupa espacio pero invisible

    # Botón Siguiente (o mensaje de completado en M9)
    if nxt:
        btn_next = f"""
        <a href="modulo-{nxt[0]}.html"
           class="flex items-center gap-3 px-5 py-3 bg-mep-blue hover:bg-blue-700
                  rounded-xl text-white font-medium transition-all group
                  shadow-lg shadow-blue-500/20">
            <div class="hidden sm:block text-right">
                <div class="text-xs text-blue-200">Siguiente</div>
                <div class="text-sm font-semibold">{nxt[1]}</div>
            </div>
            <svg class="w-4 h-4 flex-shrink-0 group-hover:translate-x-1 transition-transform"
                 fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M9 5l7 7-7 7"/>
            </svg>
        </a>"""
    else:
        btn_next = """
        <div class="flex items-center gap-3 px-5 py-3 bg-green-50 border border-green-200
                    rounded-xl text-green-800 font-medium">
            <span class="text-xl">🎉</span>
            <div class="hidden sm:block text-left">
                <div class="text-xs text-green-600 font-semibold uppercase tracking-wide">¡Completado!</div>
                <div class="text-sm font-semibold">Has recorrido todos los módulos</div>
            </div>
        </div>"""

    return f"""
            <!-- ═══ Navegación entre módulos ═══ -->
            <div class="border-t border-gray-200 mt-10 pt-8 pb-2
                        flex items-center justify-between gap-4" id="mod-nav">
                {btn_prev}
                <a href="modulos.html"
                   class="text-sm text-gray-400 hover:text-mep-blue underline transition-colors
                          hidden sm:block">
                    Ver catálogo
                </a>
                {btn_next}
            </div>
"""


def build_prereq(text):
    """Genera el banner de prerequisito."""
    return f"""
            <!-- Banner de prerequisito -->
            <div class="bg-blue-50 border border-blue-200 rounded-xl p-4 mb-6
                        flex items-center gap-3" id="prereq-banner">
                <span class="text-xl flex-shrink-0">📋</span>
                <p class="text-sm text-blue-800 m-0">
                    <strong>Prerequisito recomendado:</strong> {text}
                </p>
            </div>
"""


MAIN_CLOSE   = "        </main>"
ETHICS_MARK  = "<!-- ⚠️ Banner de Advertencia: Datos de Estudiantes -->"
NAV_MARK     = "<!-- ═══ Navegación entre módulos ═══ -->"
PREREQ_MARK  = "<!-- Banner de prerequisito -->"


def already_has(content, marker):
    return marker in content


def process_module(mod_num):
    path = os.path.join(BASE, f"modulo-{mod_num}.html")
    if not os.path.exists(path):
        print(f"  ⚠️  No encontrado: {path}")
        return

    cfg = MODULES[mod_num]
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # 1. Insertar navegación antes de </main>
    if not already_has(content, NAV_MARK):
        nav_html = build_nav(mod_num, cfg)
        content = content.replace(MAIN_CLOSE, nav_html + MAIN_CLOSE, 1)
        changed = True
        print(f"  ✅ Navegación añadida a M{mod_num}")
    else:
        print(f"  ℹ️  M{mod_num} ya tiene navegación — omitido")

    # 2. Insertar prerequisito (solo M3–M9)
    if cfg["prereq"] and not already_has(content, PREREQ_MARK):
        prereq_html = build_prereq(cfg["prereq"])
        # Insertar justo después de la línea del banner ético
        ethics_idx = content.find(ETHICS_MARK)
        if ethics_idx != -1:
            # Buscar el cierre del div del banner ético (primera línea en blanco después del div)
            # El banner ético termina con </div>\n y luego una línea vacía antes de la siguiente sección
            after_ethics = content[ethics_idx:]
            # Encontrar el cierre del contenedor del banner (</div>\n)
            close_tag = "            </div>\n"
            close_idx = after_ethics.find(close_tag)
            if close_idx != -1:
                insert_pos = ethics_idx + close_idx + len(close_tag)
                content = content[:insert_pos] + prereq_html + content[insert_pos:]
                changed = True
                print(f"  ✅ Prerequisito añadido a M{mod_num}")
            else:
                print(f"  ⚠️  No se encontró cierre del banner ético en M{mod_num}")
        else:
            print(f"  ⚠️  Banner ético no encontrado en M{mod_num} — prerequisito no añadido")
    elif cfg["prereq"]:
        print(f"  ℹ️  M{mod_num} ya tiene prerequisito — omitido")

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  💾 M{mod_num} guardado")


if __name__ == "__main__":
    print("═" * 50)
    print("F3 — Navegación Secuencial + Prerequisitos")
    print("═" * 50)
    for n in range(1, 10):
        print(f"\n[Módulo {n}]")
        process_module(n)
    print("\n✅ Proceso completado.")
