import json

input_file = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios/Textos Educativos para Toolkit.json"
output_file = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios/public/biblioteca_reducida.json"

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

documents = data.get("documents", [])
reduced_docs = []

for doc in documents:
    meta = doc.get("metadata", {})
    filename = doc.get("filename", "")
    
    # Try to extract year from filename (e.g. 03.20.26 -> 2026)
    year = "s.f."
    if "20" in filename:
        import re
        match = re.search(r'(20\d{2})', filename)
        if match:
            year = match.group(1)
        else:
            # check if 03.20.26 pattern
            match2 = re.search(r'\.(\d{2})-', filename)
            if match2:
                year = "20" + match2.group(1)
                
    # Get snippet
    snippet = ""
    pages = doc.get("pages", [])
    if pages and len(pages) > 0:
        text_obj = pages[0].get("text", {})
        if text_obj:
            snippet = text_obj.get("text", "")[:150].replace('\n', ' ') + "..."

    reduced_docs.append({
        "id": doc.get("document_id", ""),
        "filename": filename,
        "title": meta.get("title", "") or filename.replace("-", " ").replace(".pdf", ""),
        "author": meta.get("author", "") or "Autor Desconocido",
        "page_count": meta.get("page_count", 0),
        "year": year,
        "snippet": snippet
    })

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(reduced_docs, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(reduced_docs)} documents to {output_file}")
