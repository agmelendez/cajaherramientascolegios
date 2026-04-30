import json
import os
import re

base_path = "/Users/agustingomez/Desktop/Archivos Agustín/Caja de Herramientas para Docentes de Colegios"

# 1. Load biblioteca_reducida.js
bib_path = os.path.join(base_path, "biblioteca_reducida.js")
with open(bib_path, "r", encoding="utf-8") as f:
    bib_content = f.read()

# Extract json
json_str = bib_content.replace("const bibliotecaData = \n", "").strip()
if json_str.endswith(";"):
    json_str = json_str[:-1]

bib_data = json.loads(json_str)

# 2. Load corpus_calidad_final.json
calidad_path = os.path.join(base_path, "ArchivosJSON", "RecursosIA", "corpus_calidad_final.json")
with open(calidad_path, "r", encoding="utf-8") as f:
    calidad_data = json.load(f)

# 3. Load corpus_indices_completos.json
indices_path = os.path.join(base_path, "ArchivosJSON", "RecursosIA", "corpus_indices_completos.json")
with open(indices_path, "r", encoding="utf-8") as f:
    indices_data = json.load(f)

# Create lookup dicts
calidad_lookup = {doc["document_id"]: doc for doc in calidad_data.get("documents", [])}
indices_lookup = {doc["document_id"]: doc.get("sections", []) for doc in indices_data.get("table_of_contents", [])}

# Merge
merged_data = []
for doc in bib_data:
    doc_id = doc["id"]
    
    # Defaults
    pages = doc.get("page_count", 0)
    words = 0
    tables = 0
    quality = 0.5 # Default fair
    toc = []

    if doc_id in calidad_lookup:
        c_doc = calidad_lookup[doc_id]
        pages = c_doc.get("pages", pages)
        words = c_doc.get("words", 0)
        tables = c_doc.get("tables", 0)
        quality = c_doc.get("quality", 0.5)

    if doc_id in indices_lookup:
        toc = indices_lookup[doc_id]

    doc["pages"] = pages
    doc["words"] = words
    doc["tables"] = tables
    doc["quality"] = quality
    doc["table_of_contents"] = toc
    
    merged_data.append(doc)

# 4. Save to corpus_frontend_data.js
out_path = os.path.join(base_path, "corpus_frontend_data.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(f"const corpusData = \n{json.dumps(merged_data, indent=2, ensure_ascii=False)};")

print(f"Successfully generated {out_path} with {len(merged_data)} documents.")
