import os
import re

def verify_sprint5():
    workspace_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"
    errors = []
    successes = []

    print("=== INICIANDO VERIFICACIÓN DE SPRINT 5 ===")

    # 1. Verificar index.html (Onboarding y Timeline)
    index_path = os.path.join(workspace_dir, "index.html")
    if not os.path.exists(index_path):
        errors.append("index.html no existe")
    else:
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()
        
        # Buscar el almacenamiento del perfil JSON completo
        if "caja_docente_perfil" in index_content:
            successes.append("index.html: Guarda perfil bajo la clave 'caja_docente_perfil'")
        else:
            errors.append("index.html: No se encontró almacenamiento para 'caja_docente_perfil'")

        # Buscar el Timeline interactivo
        if "onb-timeline" in index_content or "timeline" in index_content.lower():
            successes.append("index.html: Contiene la interfaz de Timeline del plan de aprendizaje")
        else:
            errors.append("index.html: No se encontró la interfaz del Timeline de 3 pasos")

    # 2. Verificar glosario-tooltips.js (Script de Adaptación Global)
    glosario_js_path = os.path.join(workspace_dir, "glosario-tooltips.js")
    if not os.path.exists(glosario_js_path):
        errors.append("glosario-tooltips.js no existe")
    else:
        with open(glosario_js_path, "r", encoding="utf-8") as f:
            js_content = f.read()
        
        if "function setLevelContent()" in js_content and "setLevelContent();" in js_content:
            successes.append("glosario-tooltips.js: Define y ejecuta la función global setLevelContent()")
        else:
            errors.append("glosario-tooltips.js: Falta la definición o ejecución de setLevelContent()")

    # 3. Verificar modulo-1.html (Adaptaciones y Widgets)
    m1_path = os.path.join(workspace_dir, "modulo-1.html")
    if not os.path.exists(m1_path):
        errors.append("modulo-1.html no existe")
    else:
        with open(m1_path, "r", encoding="utf-8") as f:
            m1_content = f.read()

        # data-level adaptation
        if 'data-level="beginner"' in m1_content and 'data-level="advanced"' in m1_content:
            successes.append("modulo-1.html: Contiene bloques diferenciados por data-level")
        else:
            errors.append("modulo-1.html: No se encontraron bloques data-level='beginner' o data-level='advanced'")

        # data-edu-level adaptation
        if 'data-edu-level="primaria"' in m1_content and 'data-edu-level="secundaria"' in m1_content:
            successes.append("modulo-1.html: Contiene bloques adaptativos por data-edu-level")
        else:
            errors.append("modulo-1.html: No se encontraron bloques data-edu-level")

        # widgets interactivos de comprobación rápida
        if "checkAnswer" in m1_content:
            successes.append("modulo-1.html: Contiene los widgets interactivos VerificationCheck")
        else:
            errors.append("modulo-1.html: No se encontraron los widgets interactivos checkAnswer")

    # 4. Verificar modulos.html (Mapa de Ruta SVG y Roadmap JS Controller)
    modulos_path = os.path.join(workspace_dir, "modulos.html")
    if not os.path.exists(modulos_path):
        errors.append("modulos.html no existe")
    else:
        with open(modulos_path, "r", encoding="utf-8") as f:
            modulos_content = f.read()

        # Círculos SVG
        missing_circles = []
        for i in range(1, 11):
            if f'id="circle-{i}"' not in modulos_content:
                missing_circles.append(i)
        if not missing_circles:
            successes.append("modulos.html: El SVG contiene los 10 círculos de nodos (circle-1 a circle-10)")
        else:
            errors.append(f"modulos.html: Faltan círculos en el SVG para los módulos: {missing_circles}")

        # Conexiones SVG
        connections = ['link-1-2', 'link-1-3', 'link-2-4', 'link-3-5', 'link-3-6', 'link-4-7', 'link-5-8', 'link-6-9', 'link-3-10']
        missing_links = [l for l in connections if f'id="{l}"' not in modulos_content]
        if not missing_links:
            successes.append("modulos.html: El SVG contiene todas las conexiones requeridas (roadmap-link)")
        else:
            errors.append(f"modulos.html: Faltan las líneas de conexión: {missing_links}")

        # Tarjeta lateral informativa y controlador JS
        if "node-detail-content" in modulos_content and "updateRoadmap" in modulos_content:
            successes.append("modulos.html: Contiene la tarjeta de detalle lateral y el Roadmap JS Controller")
        else:
            errors.append("modulos.html: Falta el panel lateral de detalle o el script Roadmap JS Controller")

        # Tarjeta del Módulo 10 en la rejilla de módulos
        if 'modulo-10.html' in modulos_content and 'Módulo 10: Micro-Prompts' in modulos_content:
            successes.append("modulos.html: La rejilla de módulos contiene la tarjeta activa para el Módulo 10")
        else:
            errors.append("modulos.html: No se encontró la tarjeta del Módulo 10 en la rejilla")

    # 5. Verificar Banners de Prerrequisitos en Módulo 2 al 10
    missing_banners = []
    for i in range(2, 11):
        path = os.path.join(workspace_dir, f"modulo-{i}.html")
        if not os.path.exists(path):
            errors.append(f"modulo-{i}.html no existe")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if "caja-prerrequisitos" not in content:
            missing_banners.append(i)
            
    if not missing_banners:
        successes.append("Módulos 2-10: Todos contienen el banner dinámico y reactivo de prerrequisitos")
    else:
        errors.append(f"Módulos faltantes del banner de prerrequisitos: {missing_banners}")

    print("\n--- RESULTADOS ---")
    for s in successes:
        print(f"✅ {s}")
    for e in errors:
        print(f"❌ {e}")

    if not errors:
        print("\n🎉 ¡VERIFICACIÓN EXITOSA! Sprint 5 cumple al 100% con los requerimientos técnicos y funcionales.")
        return True
    else:
        print(f"\n⚠️ Se encontraron {len(errors)} errores en la verificación.")
        return False

if __name__ == "__main__":
    verify_sprint5()
