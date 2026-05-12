import os
import re

base_dir = "."
infografias_dir = os.path.join(base_dir, "infografias")

# Rename subdirectories and files to be web-safe
for mod_folder in os.listdir(infografias_dir):
    mod_path = os.path.join(infografias_dir, mod_folder)
    if os.path.isdir(mod_path) and mod_folder.startswith("Modulo "):
        # e.g., "Modulo 1" -> "modulo-1"
        new_mod_folder = mod_folder.replace("Modulo ", "modulo-")
        new_mod_path = os.path.join(infografias_dir, new_mod_folder)
        os.rename(mod_path, new_mod_path)
        
        # Now rename files inside
        for file in os.listdir(new_mod_path):
            file_path = os.path.join(new_mod_path, file)
            # e.g., "Infografia 1.1.png" -> "infografia-1.1.png"
            # Or "Infografía 1.1.png" -> "infografia-1.1.png"
            new_file = file.lower()
            new_file = new_file.replace("í", "i").replace(" ", "-")
            new_file_path = os.path.join(new_mod_path, new_file)
            if file_path != new_file_path:
                os.rename(file_path, new_file_path)

# Update HTML files
for filename in os.listdir(base_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        original_content = content
        
        # Replace occurrences like "Infografías/Modulo 1/Infografia 1.1.png"
        # We'll use a regex to capture the module number and image number.
        def path_replacer(match):
            mod_num = match.group(1)
            img_num = match.group(2)
            ext = match.group(3)
            # Return new path: "infografias/modulo-1/infografia-1.1.png"
            return f"infografias/modulo-{mod_num}/infografia-{img_num}{ext}"

        # Match Infografías/Modulo X/Infografia X.X.png or similar
        pattern = re.compile(r'Infografías/Modulo (\d+)/Infograf[íi]a ([\d\.]+)(\.[a-zA-Z]+)')
        content = pattern.sub(path_replacer, content)
        
        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filename}")
