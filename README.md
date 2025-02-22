# Chatbot AI (RAG)

## Woker

### install python packages

`pip install -r worker/requirements.txt`

### set .env vars

`echo "PINECONE_API_KEY=..." > worker/.env`
`echo "PINECONE_HOST=..." >> worker/.env`
`echo "PINECONE_INDEX=codingtest" >> worker/.env`
`echo "PINECONE_REGION=..." >> worker/.env`
`echo "PINECONE_NAMESPACE=..." >> worker/.env`
`echo "OPENAI_API_KEY=..." >> worker/.env`
`echo "EMBEDDING_MODEL=text-embedding-3-large" >> worker/.env`

### start server

`uvicorn worker.main:app --reload`

### query api

`curl -X 'POST' 'http://127.0.0.1:8000/upload/' -F 'file=@files/example_3.pdf'`

`curl -X 'POST' 'http://127.0.0.1:8000/query/' -d 'query=Dimmi qualcosa sul documento'`

## UI

### node & npm versions

node version: `18.17.1`

npm version: `9.6.7`

### install npm packages

`npm install --prefix webapp`

### start ui

`npm run dev`
