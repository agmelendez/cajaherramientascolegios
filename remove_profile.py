import os
import re

directory = "."

# 1. Remove profile from header
profile_pattern = re.compile(
    r'<div class="flex items-center gap-3 p-1 pr-3 rounded-full border border-gray-200 hover:bg-gray-50 cursor-pointer(?: transition-colors)?">\s*<img src="https://ui-avatars\.com/api/\?name=Agustin\+Gomez[^"]*" alt="Avatar" class="w-8 h-8 rounded-full">\s*<span class="text-sm font-medium text-gray-700 hidden sm:block">Agustín Gómez Meléndez</span>\s*</div>',
    re.IGNORECASE | re.DOTALL
)

# 2. Remove Cuenta section from sidebar
cuenta_pattern = re.compile(
    r'<div class="p-5 border-t border-gray-100 bg-gray-50/50">\s*<p class="text-xs font-semibold text-gray-400 uppercase tracking-wider mb-3 px-3">Cuenta</p>\s*<a href="#" class="block px-3 py-2 text-sm text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md transition-colors">Perfil</a>\s*<a href="#" class="block px-3 py-2 text-sm text-gray-600 hover:text-gray-900 hover:bg-gray-100 rounded-md transition-colors">Cerrar sesión</a>\s*</div>',
    re.IGNORECASE | re.DOTALL
)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = profile_pattern.sub("", content)
        new_content = cuenta_pattern.sub("", new_content)
        
        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated {filename}")
