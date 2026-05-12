import os
import re

base_dir = "."
infografias_dir = os.path.join(base_dir, "infografias")

# Function to rename HTML file and its corresponding infografias folder
def shift_module(old_num, new_num):
    old_html = f"modulo-{old_num}.html"
    new_html = f"modulo-{new_num}.html"
    old_info = os.path.join(infografias_dir, f"modulo-{old_num}")
    new_info = os.path.join(infografias_dir, f"modulo-{new_num}")
    
    if os.path.exists(old_html):
        os.rename(old_html, new_html)
        print(f"Renamed {old_html} to {new_html}")
    if os.path.exists(old_info):
        os.rename(old_info, new_info)
        print(f"Renamed {old_info} to {new_info}")

# Cascade shift from top to bottom to avoid overwriting
# 9 -> 10
# 8 -> 9
# 7 -> 8
# 6 -> 7
# 5 -> 6
# 4 -> 5
shift_module(9, 10)
shift_module(8, 9)
shift_module(7, 8)
shift_module(6, 7)
shift_module(5, 6)
shift_module(4, 5)

# Special case for 2 -> 4
shift_module(2, 4)

# 2 <- privacidad-etica.html
if os.path.exists("privacidad-etica.html"):
    os.rename("privacidad-etica.html", "modulo-2.html")
    print("Renamed privacidad-etica.html to modulo-2.html")

# Now we need to update the contents of the files to reflect their new module numbers
# We need to do this carefully. 

# A mapping of file -> new module number
updates = {
    "modulo-10.html": 10,
    "modulo-9.html": 9,
    "modulo-8.html": 8,
    "modulo-7.html": 7,
    "modulo-6.html": 6,
    "modulo-5.html": 5,
    "modulo-4.html": 4,
    "modulo-2.html": 2
}

for filename, new_num in updates.items():
    if not os.path.exists(filename):
        continue
    
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the old module number with the new one in text
    # The title usually says "Módulo X: " or "Módulo X</span>"
    # We must be careful because the old number might be replaced incorrectly.
    # To be safe, we only replace specific patterns.
    
    # Let's dynamically find the OLD module number this file used to have.
    # For modulo-4, old was 2. For modulo-5, old was 4. For modulo-X, old was X-1.
    old_num = new_num - 1 if new_num >= 5 else (2 if new_num == 4 else None)
    
    if old_num:
        # Title tag
        content = re.sub(f"<title>Módulo {old_num}:", f"<title>Módulo {new_num}:", content)
        # H1 tag? Actually usually it doesn't say "Módulo X" in H1, it's just the name.
        # But there is a pill: <span class="px-3 py-1 bg-... text-... font-bold rounded-full uppercase tracking-wide">Módulo X</span>
        content = re.sub(f">Módulo {old_num}<", f">Módulo {new_num}<", content)
        # Breadcrumb
        content = re.sub(f"Módulo {old_num}</span>", f"Módulo {new_num}</span>", content)
        # Alt texts
        content = re.sub(f'Módulo {old_num} detallando', f'Módulo {new_num} detallando', content)
        # Infografias links
        # Previously we normalized them to "infografias/modulo-old_num/infografia-old_num.x.png"
        content = re.sub(f'infografias/modulo-{old_num}/infografia-{old_num}\\.', f'infografias/modulo-{new_num}/infografia-{new_num}.', content)

    # For modulo-2 (old privacidad-etica), there might not be "Módulo X" in it.
    if new_num == 2:
        content = re.sub(r'<title>.*?</title>', '<title>Módulo 2: Ética y Privacidad - Caja de Herramientas</title>', content)
        # Add the Modulo 2 pill in the hero if not exists (it doesn't exist in privacidad-etica)
        # Actually we just leave it for now and update manually if needed.
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
    # We must also rename the infografia images themselves inside the folders
    # e.g., infografias/modulo-5/infografia-4.1.png -> infografia-5.1.png
    info_dir = os.path.join(infografias_dir, f"modulo-{new_num}")
    if os.path.exists(info_dir):
        for img in os.listdir(info_dir):
            if old_num and f"infografia-{old_num}." in img:
                new_img = img.replace(f"infografia-{old_num}.", f"infografia-{new_num}.")
                os.rename(os.path.join(info_dir, img), os.path.join(info_dir, new_img))

print("Cascade shift complete.")
