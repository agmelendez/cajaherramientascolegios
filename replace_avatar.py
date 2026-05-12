import os
import re

directory = "."
pattern = re.compile(
    r'<img src="https://ui-avatars\.com/api/\?name=Agustin\+Gomez[^"]*" alt="Avatar" class="([^"]*)">\s*<span class="([^"]*)">Agustín(?: Gómez Meléndez)?</span>',
    re.IGNORECASE | re.DOTALL
)

replacement = r'<img src="https://ui-avatars.com/api/?name=Docente+MEP&background=006633&color=fff" alt="Perfil de usuario" class="\1">\n                <span class="\2">Docente</span>'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = pattern.sub(replacement, content)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            count += 1
            print(f"Updated {filename}")

print(f"Total files updated: {count}")
