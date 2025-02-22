import openai
from config import settings

def generate_embedding(text):
    response = openai.Embedding.create(
        input=text,
        model=settings.EMBEDDING_MODEL,
        api_key=settings.OPENAI_API_KEY
    )
    return response["data"][0]["embedding"]
