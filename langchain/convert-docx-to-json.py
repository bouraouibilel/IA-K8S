from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Charger un document Word
loader = Docx2txtLoader("D:\work\sample\IA-K8S\docs\pasrau\PASRAU_DCT_Dossier_conception_technique_16.0.docx")
docs = loader.load()

# Découper en chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splitted_docs = splitter.split_documents(docs)

# Transformer en JSON
import json
json_data = [doc.dict() for doc in splitted_docs]

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
