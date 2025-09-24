import json
from pathlib import Path
from unstructured.partition.docx import partition_docx

def docx_to_json(input_path: str, output_path: str):
    """
    Transforme un fichier DOCX en JSON prêt pour ingestion RAG.
    - Découpe en éléments (titres, paragraphes, tableaux, etc.)
    - Conserve les métadonnées (page, type de contenu)
    """

    elements = partition_docx(input_path)

    data = []
    for i, el in enumerate(elements):
        chunk = {
            "id": f"chunk-{i}",         # identifiant unique pour un vecteur store
            "type": el.category,        # ex: Title, Paragraph, List, Table
            "text": el.text.strip(),
            "metadata": el.metadata.to_dict()
        }
        data.append(chunk)

    # Sauvegarde en JSON lisible
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Conversion terminée ! Fichier sauvegardé : {output_path}")


if __name__ == "__main__":
    # Exemple d'utilisation
    input_file = "myDoc.docx"   # ton fichier source
    output_file = "myDoc.json"  # sortie JSON

    # Vérification de l'existence du fichier
    if Path(input_file).exists():
        docx_to_json(input_file, output_file)
    else:
        print(f"⚠️ Fichier introuvable : {input_file}")
