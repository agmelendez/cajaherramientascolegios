import os
import re

base_dir = "."

for filename in os.listdir(base_dir):
    if filename.startswith("modulo-") and filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # We need to find alt="Infografía" near <img src="infografias/modulo-X/..."
        # Actually, let's just replace alt="Infografía" with alt="Infografía del Módulo X detallando su tema central"
        # Since filename is modulo-X.html, we can extract X
        mod_num_match = re.search(r'modulo-(\d+)\.html', filename)
        if mod_num_match:
            mod_num = mod_num_match.group(1)
            
            # The HTML has <img src="infografias/modulo-X/infografia-X.1.png" alt="Infografía"
            new_alt = f'alt="Infografía del Módulo {mod_num} detallando su tema central"'
            
            # Use regex to find img tags with alt="Infografía"
            content = re.sub(r'alt="Infograf[íi]a"', new_alt, content)
            
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated alt text in {filename}")
