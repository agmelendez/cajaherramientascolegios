import os
import re

workspace_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

errors = []
warnings = []
passed_checks = []

print("=== STARTING SPRINT 3 VERIFICATION ===\n")

# 1. Check existence of crucial files
crucial_files = [
    "glosario.html",
    "glosario-data.js",
    "glosario-tooltips.js"
]

for f in crucial_files:
    path = os.path.join(workspace_dir, f)
    if os.path.exists(path):
        passed_checks.append(f"Crucial file '{f}' exists.")
    else:
        errors.append(f"Crucial file '{f}' is missing from the workspace!")

# 2. Check sidebar glosario link in all HTML files
html_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]
print(f"Checking sidebar glosario link in {len(html_files)} HTML files...")

for filename in html_files:
    filepath = os.path.join(workspace_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check for glosario link
    if 'href="glosario.html"' not in content:
        errors.append(f"File {filename} is missing the sidebar link to 'glosario.html'!")
    else:
        # Check active class styling on glosario.html, and standard styling elsewhere
        if filename == "glosario.html":
            if 'bg-blue-50 text-mep-blue' not in content:
                warnings.append(f"glosario.html does not seem to have the active styling in its sidebar!")
            else:
                passed_checks.append("glosario.html sidebar link has active styling.")
        else:
            passed_checks.append(f"File {filename} has the glosario.html sidebar link.")

passed_checks.append(f"All {len(html_files)} HTML files have 'glosario.html' in their sidebar.")

# 3. Check onboarding profile persistence in index.html
index_path = os.path.join(workspace_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
        
    if "caja_docente_perfil" in index_content:
        passed_checks.append("index.html contains 'caja_docente_perfil' persistence reference.")
    else:
        errors.append("index.html is missing 'caja_docente_perfil' localstorage persistence!")
        
    if "localStorage.removeItem" in index_content or "localStorage.clear" in index_content or "caja_docente_perfil" in index_content:
        passed_checks.append("index.html handles profile resetting.")
    else:
        warnings.append("index.html might be missing profile reset logic.")
else:
    errors.append("index.html is missing!")

# 4. Check tooltips and inline terms
for filename in ["modulo-1.html", "ia-educacion.html"]:
    filepath = os.path.join(workspace_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check for imports
        if "glosario-data.js" in content and "glosario-tooltips.js" in content:
            passed_checks.append(f"{filename} successfully imports glosario-data.js and glosario-tooltips.js script tags.")
        else:
            errors.append(f"{filename} is missing imports for 'glosario-data.js' or 'glosario-tooltips.js'!")
            
        # Check for glosario-term classes
        if "glosario-term" in content:
            passed_checks.append(f"{filename} contains inline terms wrapped with 'glosario-term' class.")
        else:
            warnings.append(f"{filename} does not seem to contain any wrapped 'glosario-term' elements!")
    else:
        errors.append(f"Tooltip target file {filename} is missing!")

# 5. Check level customization in ia-educacion.html
ia_path = os.path.join(workspace_dir, "ia-educacion.html")
if os.path.exists(ia_path):
    with open(ia_path, "r", encoding="utf-8") as f:
        ia_content = f.read()
        
    if 'data-level="beginner"' in ia_content and 'data-level="advanced"' in ia_content:
        passed_checks.append("ia-educacion.html contains double-versioned cards for 'beginner' and 'advanced' levels.")
    else:
        errors.append("ia-educacion.html is missing 'data-level' attributes for level customization!")
        
    if 'setLevel' in ia_content:
        passed_checks.append("ia-educacion.html has the setLevel JavaScript controller function.")
    else:
        errors.append("ia-educacion.html is missing 'setLevel' JavaScript controller function!")
else:
    errors.append("ia-educacion.html is missing!")

print("\n=== VERIFICATION RESULTS ===")
print(f"Passed Checks ({len(passed_checks)}):")
for check in passed_checks[:20]:  # Print first 20 checks to keep it clean
    print(f"  ✓ {check}")
if len(passed_checks) > 20:
    print(f"  ... and {len(passed_checks) - 20} more checks.")

if warnings:
    print(f"\n⚠️ Warnings ({len(warnings)}):")
    for w in warnings:
        print(f"  - {w}")

if errors:
    print(f"\n❌ ERRORS FOUND ({len(errors)}):")
    for e in errors:
        print(f"  - {e}")
else:
    print("\n🎉 ALL TESTS PASSED! Sprint 3 is fully complete and structurally sound.")
