import os
import re

base_path = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

modules_data = {
    "modulo-1.html": "Infografías/Modulo 1/Esta es la IA que nos prometieron? .png",
    "modulo-2.html": "Infografías/Modulo 2/Escudo Digital IA Aula.png",
    "modulo-3.html": "Infografías/Modulo 3/Guía Rápida IA Aula.png",
    "modulo-4.html": "Infografías/Modulo 4/Planteamiento ágil en el aula.png",
}

lightbox_code = """
    <!-- Lightbox Modal -->
    <div id="lightbox" class="fixed inset-0 z-[100] bg-black/90 hidden flex-col items-center justify-center backdrop-blur-sm transition-opacity duration-300 opacity-0">
        <div class="absolute top-4 right-4 flex gap-4">
            <a id="lightbox-download" href="#" download class="text-white hover:text-gray-300 p-2 bg-white/10 rounded-full transition-colors" title="Descargar">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
            </a>
            <button onclick="closeLightbox()" class="text-white hover:text-gray-300 p-2 bg-white/10 rounded-full transition-colors" title="Cerrar">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
            </button>
        </div>
        <div class="w-full h-full p-4 md:p-12 flex items-center justify-center overflow-auto" onclick="if(event.target === this) closeLightbox()">
            <img id="lightbox-img" src="" alt="Infografía Ampliada" class="max-w-full max-h-full object-contain rounded-lg shadow-2xl">
        </div>
    </div>

    <script>
        function openLightbox(imageSrc) {
            const lightbox = document.getElementById('lightbox');
            const img = document.getElementById('lightbox-img');
            const downloadBtn = document.getElementById('lightbox-download');
            
            img.src = imageSrc;
            downloadBtn.href = imageSrc;
            
            lightbox.classList.remove('hidden');
            setTimeout(() => {
                lightbox.classList.remove('opacity-0');
            }, 10);
            
            document.body.classList.add('overflow-hidden');
        }

        function closeLightbox() {
            const lightbox = document.getElementById('lightbox');
            lightbox.classList.add('opacity-0');
            
            setTimeout(() => {
                lightbox.classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
            }, 300);
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeLightbox();
        });
    </script>
</body>"""

for filename, img_path in modules_data.items():
    filepath = os.path.join(base_path, filename)
    
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "Recursos / Infografías" in content:
        print(f"Already processed {filename}")
        continue

    section_code = f"""
            <!-- Recursos / Infografías Section -->
            <div class="bg-white rounded-2xl border border-gray-200 shadow-sm p-6 mb-8">
                <div class="flex items-center gap-3 mb-4">
                    <span class="text-2xl">🖼️</span>
                    <h2 class="text-xl font-bold text-gray-900">Recursos / Infografías</h2>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                    <div class="group relative rounded-xl overflow-hidden border border-gray-200 shadow-sm hover:shadow-md transition-all cursor-pointer bg-gray-50 flex flex-col" onclick="openLightbox('{img_path}')">
                        <div class="aspect-[3/4] overflow-hidden bg-gray-100 flex items-center justify-center p-2">
                            <img src="{img_path}" alt="Infografía" class="w-full h-full object-contain group-hover:scale-105 transition-transform duration-300">
                        </div>
                        <div class="p-3 bg-white border-t border-gray-100">
                            <p class="text-sm font-medium text-gray-700 text-center flex items-center justify-center gap-2">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-mep-blue" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7" /></svg>
                                Ampliar Infografía
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Content Grid: 2 Columns -->"""

    # Inject section
    new_content = content.replace("<!-- Content Grid: 2 Columns -->", section_code, 1)
    
    # Inject lightbox
    new_content = new_content.replace("</body>", lightbox_code, 1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"Updated {filename}")

print("Done.")
