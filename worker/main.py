from fastapi import FastAPI, UploadFile, File, Form
from config import settings
from file_processing import process_file
from retrieval import get_response

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Chatbot AI (RAG) Backend is Running"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    text = await process_file(file)
    return {"extracted_text": text}

@app.post("/query/")
async def query_chatbot(query: str = Form(...)):
    response = get_response(query)
    return {"response": response}
