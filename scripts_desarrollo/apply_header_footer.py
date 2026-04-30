import os
import glob
import re

base_path = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"
html_files = glob.glob(os.path.join(base_path, "*.html"))

top_bar_html = """
    <!-- Top Bar Institucional -->
    <div class="fixed top-0 left-0 right-0 h-14 bg-white border-b border-gray-200 z-[60] flex items-center justify-between px-4 md:px-6 shadow-sm">
        <div class="flex items-center gap-4 md:gap-6 h-full py-2">
            <img src="Logos/UCR.png" alt="UCR" class="h-6 md:h-8 object-contain">
            <img src="Logos/VASUCR.png" alt="VAS" class="h-6 md:h-8 object-contain">
            <img src="Logos/PuenteVAS.png" alt="Puentes" class="h-6 md:h-8 object-contain hidden sm:block">
            <img src="Logos/CIOdD.jpg" alt="CIOdD" class="h-6 md:h-8 object-contain">
        </div>
        <div class="flex items-center h-full py-2">
            <img src="Logos/ED3698.png" alt="ED3698" class="h-6 md:h-8 object-contain">
        </div>
    </div>
"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # 1. Add Top Bar if not exists
    if "<!-- Top Bar Institucional -->" not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1' + top_bar_html, content, count=1)

    # 2. Adjust main header position
    content = content.replace('class="fixed top-0 left-0 right-0 h-20', 'class="fixed top-14 left-0 right-0 h-20')

    # 3. Adjust main wrapper padding
    content = content.replace('class="flex flex-1 pt-20"', 'class="flex flex-1 pt-[136px]"')

    # 4. Adjust sidebar padding for mobile
    content = content.replace('pt-20 md:pt-0"', 'pt-[136px] md:pt-0"')

    # 5. Replace Facebook link
    content = re.sub(
        r'<a href="[^"]*" class="([^"]*)">\s*<span class="sr-only">Facebook</span>',
        r'<a href="https://www.facebook.com/CIOdD.UCR" target="_blank" class="\1">\n                        <span class="sr-only">Facebook</span>',
        content
    )

    # 6. Replace Twitter/X link
    content = re.sub(
        r'<a href="[^"]*" class="([^"]*)">\s*<span class="sr-only">Twitter</span>',
        r'<a href="https://x.com/CIOdDUCR" target="_blank" class="\1">\n                        <span class="sr-only">Twitter</span>',
        content
    )

    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")
    else:
        print(f"No changes needed for {os.path.basename(file_path)}")

print("Done.")
