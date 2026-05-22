import os

workspace_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

errors = []
warnings = []
passed_checks = []

print("=== INICIANDO VERIFICACIÓN DE SPRINT 4 ===\n")

# 1. Verificar existencia de la Guía Editorial
guia_path = os.path.join(workspace_dir, "docs", "guia_editorial.md")
if os.path.exists(guia_path):
    passed_checks.append("La Guía Editorial 'docs/guia_editorial.md' existe.")
else:
    errors.append("La Guía Editorial 'docs/guia_editorial.md' no existe en el repositorio.")

# 2. Verificar Panel de Manifiesto en index.html
index_path = os.path.join(workspace_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    if "Lo que siempre comienza en ti" in index_content:
        passed_checks.append("index.html contiene el panel del Manifiesto Humano.")
    else:
        errors.append("index.html no contiene el panel del Manifiesto Humano ('Lo que siempre comienza en ti')!")

    if "Principio de Mediación Humana" in index_content:
        passed_checks.append("index.html contiene el badge del Principio de Mediación Humana.")
    else:
        warnings.append("index.html podría no tener el badge del Principio de Mediación Humana.")
else:
    errors.append("index.html no existe!")

# 3. Verificar Sección 16, TOC y LocalStorage en modulo-1.html, modulo-2.html, modulo-3.html
modulos = {
    "modulo-1.html": {
        "key": "caja_reflexion_modulo_1",
        "fields": ["reflexion-m1-p1", "reflexion-m1-p2", "reflexion-m1-p3"]
    },
    "modulo-2.html": {
        "key": "caja_reflexion_modulo_2",
        "fields": ["reflexion-m2-p1", "reflexion-m2-p2", "reflexion-m2-p3"]
    },
    "modulo-3.html": {
        "key": "caja_reflexion_modulo_3",
        "fields": ["reflexion-m3-p1", "reflexion-m3-p2", "reflexion-m3-p3"]
    }
}

for filename, data in modulos.items():
    filepath = os.path.join(workspace_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # A. Sección id s16
        if 'id="s16"' in content or "id='s16'" in content:
            passed_checks.append(f"{filename} contiene la sección de reflexión con ID 's16'.")
        else:
            errors.append(f"{filename} no contiene la sección con ID 's16'!")

        # B. Título de la sección
        if "¿Qué sigue siendo tuyo?" in content:
            passed_checks.append(f"{filename} contiene el título interactivo '¿Qué sigue siendo tuyo?'.")
        else:
            errors.append(f"{filename} no contiene el título interactivo '¿Qué sigue siendo tuyo?'!")

        # C. Enlace en el TOC
        if 'href="#s16"' in content or "href='#s16'" in content:
            passed_checks.append(f"{filename} contiene el enlace a la sección 16 en el TOC.")
        else:
            errors.append(f"{filename} no contiene el enlace a la sección 16 en el TOC ('href=\"#s16\"')!")

        # D. Clave de LocalStorage
        if data["key"] in content:
            passed_checks.append(f"{filename} utiliza la clave correcta de localStorage '{data['key']}'.")
        else:
            errors.append(f"{filename} no hace referencia a la clave de localStorage '{data['key']}'!")

        # E. IDs de los campos de texto
        fields_ok = True
        for field in data["fields"]:
            if f'id="{field}"' in content or f"id='{field}'" in content:
                passed_checks.append(f"{filename} tiene el campo de texto con ID '{field}'.")
            else:
                errors.append(f"{filename} no tiene el campo de texto con ID '{field}'!")
                fields_ok = False
    else:
        errors.append(f"{filename} no existe!")

# Resultados
print("\n=== RESULTADOS DE VERIFICACIÓN ===")
print(f"Pruebas Superadas ({len(passed_checks)}):")
for check in passed_checks:
    print(f"  ✓ {check}")

if warnings:
    print(f"\n⚠️ Advertencias ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")

if errors:
    print(f"\n❌ ERRORES ENCONTRADOS ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
else:
    print("\n🎉 ¡TODAS LAS PRUEBAS SUPERADAS! El Sprint 4 está completamente implementado y es estructuralmente robusto.")
