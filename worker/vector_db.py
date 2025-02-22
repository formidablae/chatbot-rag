from pinecone import Pinecone
import os

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Controlla se l'indice esiste, altrimenti lo crea
if os.getenv("PINECONE_INDEX") not in pc.list_indexes().names():
    pc.create_index(
        name=os.getenv("PINECONE_INDEX"),
        dimension=1536,  # Cambia se il modello di embedding è diverso
        metric='cosine'
    )

# Ottieni l'indice
index = pc.Index(os.getenv("PINECONE_INDEX"))

def upsert_embedding(text, metadata):
    embedding = generate_embedding(text)
    index.upsert([(metadata["id"], embedding, metadata)])

def query_pinecone(vector, top_k=5):
    results = index.query(vector=vector, top_k=top_k, include_metadata=True)
    return results["matches"]
