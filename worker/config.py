import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")
    PINECONE_HOST = os.getenv("PINECONE_HOST")
    PINECONE_REGION = os.getenv("PINECONE_REGION")
    PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

settings = Settings()
