# Nova

A support chatbot that answers questions from your own documents, using RAG (Retrieval-Augmented Generation). Built in Python with FastAPI and ChromaDB.

## How it works

1. Documents in `knowledge/` are split into overlapping chunks and stored in ChromaDB as embeddings.
2. A question is matched against the stored chunks and the 3 closest are retrieved.
3. The chunks and the question go into a prompt, and the LLM answers from that context only.

## Stack

- FastAPI, Pydantic, pydantic-settings
- OpenAI Python SDK (any OpenAI-compatible LLM: Ollama, Mistral, OpenAI)
- ChromaDB

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set these in `.env`:

```
LLM_API_KEY=
LLM_BASE_URL=
LLM_MODEL=
```

Add `.md` files to `knowledge/`, then index them and start the server:

```bash
python -m src.ingest
uvicorn src.main:app --reload
```

Docs UI: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/health` | Server status |
| GET | `/search?q=&k=3` | Closest chunks to a question |
| POST | `/chat` | Answer a question using retrieved chunks |

## Structure

```
src/
├── main.py       # endpoints
├── config.py     # settings from .env
├── llm.py        # LLM call
├── prompts.py    # system and RAG prompts
├── loader.py     # read documents
├── chunking.py   # split text
├── store.py      # ChromaDB save and search
└── ingest.py     # load, chunk, store
```