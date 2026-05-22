import os
import re

base_dir = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

# Find all HTML files in the base directory
html_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]

descargas_pattern = re.compile(r'(<a\s+[^>]*href=["\']descargas.html["\'][^>]*>)(.*?)(</a>)', re.DOTALL)
config_pattern = re.compile(r'(<a\s+[^>]*href=["\']configuracion.html["\'][^>]*>)(.*?)(</a>)', re.DOTALL)

updated_count = 0

for filename in html_files:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    original_content = content
    
    # Process descargas.html anchor
    def repl_descargas(match):
        start_tag = match.group(1)
        inner_content = match.group(2)
        end_tag = match.group(3)
        
        # Only modify if it is a sidebar item
        if 'sidebar-item' not in start_tag:
            return match.group(0)
            
        # Standardize aria-label inside start_tag
        if 'aria-label=' in start_tag:
            start_tag = re.sub(r'aria-label="[^"]*"', 'aria-label="Ir a la sección de descargas"', start_tag)
        else:
            start_tag = start_tag.replace('<a ', '<a aria-label="Ir a la sección de descargas" ')
            
        # Determine if active state
        is_active = 'bg-blue-50' in start_tag
        
        # Build the new inner content
        if is_active:
            new_inner = '\n                    <span class="text-xl group-hover:scale-110 transition-transform">📥</span>\n                    <span>Descargas</span>\n                '
        else:
            new_inner = '\n                    <span class="text-xl group-hover:scale-110 transition-transform grayscale group-hover:grayscale-0">📥</span>\n                    <span>Descargas</span>\n                '
            
        return f"{start_tag}{new_inner}{end_tag}"

    # Process configuracion.html anchor
    def repl_config(match):
        start_tag = match.group(1)
        inner_content = match.group(2)
        end_tag = match.group(3)
        
        # Only modify if it is a sidebar item
        if 'sidebar-item' not in start_tag:
            return match.group(0)
            
        # Standardize aria-label inside start_tag
        if 'aria-label=' in start_tag:
            start_tag = re.sub(r'aria-label="[^"]*"', 'aria-label="Ir a la sección de información"', start_tag)
        else:
            start_tag = start_tag.replace('<a ', '<a aria-label="Ir a la sección de información" ')
            
        # Determine if active state
        is_active = 'bg-blue-50' in start_tag
        
        # Build the new inner content
        if is_active:
            new_inner = '\n                    <span class="text-xl group-hover:scale-110 transition-transform">ℹ️</span>\n                    <span>Información</span>\n                '
        else:
            new_inner = '\n                    <span class="text-xl group-hover:scale-110 transition-transform grayscale group-hover:grayscale-0">ℹ️</span>\n                    <span>Información</span>\n                '
            
        return f"{start_tag}{new_inner}{end_tag}"

    content = descargas_pattern.sub(repl_descargas, content)
    content = config_pattern.sub(repl_config, content)
    
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
        updated_count += 1

print(f"Total updated files: {updated_count}")
