from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
from config import settings
import pinecone
from worker.vector_db import query_pinecone

embeddings = OpenAIEmbeddings(api_key=settings.OPENAI_API_KEY)

def get_response(query):
    query_vector = embeddings.embed_query(query)
    results = query_pinecone(query_vector)

    documents = [Document(page_content=res["metadata"]["text"]) for res in results]
    
    llm = ChatOpenAI(model_name="gpt-4", openai_api_key=settings.OPENAI_API_KEY)
    response = llm.generate(documents)

    return response
