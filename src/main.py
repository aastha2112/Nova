import asyncio
from fastapi import FastAPI, HTTPException, Query
from openai import APIError, RateLimitError
from pydantic import BaseModel, Field

from src.llm import ask_llm
from src.prompts import SUPPORT_SYSTEM_PROMPT, build_rag_prompt
from src.store import search


app = FastAPI(title='Nova')

@app.get('/health')
def health_check():
    return {'status': 'all GOOD'}

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=500)

class ChatResponse(BaseModel):
    answer: str    

@app.post('/chat', response_model=ChatResponse)
async def chat(req: ChatRequest):
    try:
        found = await asyncio.to_thread(search, req.message, 3)
        chunks = [item["text"] for item in found]
        print(chunks)                                   # temporary: dekho kya mila

        prompt = build_rag_prompt(req.message, chunks)
        answer = await ask_llm(prompt, SUPPORT_SYSTEM_PROMPT)
        return ChatResponse(answer=answer)
    except RateLimitError:
        raise HTTPException(
            status_code=429,
            detail="API rate limit hit. Wait a minute and try again.",
        )    
    except APIError as e:
        raise HTTPException(status_code=500, detail=f'LLM Error: {e}')

@app.get('/search')
def search_docs(q: str = Query(min_length = 1, max_length=300), k: int = Query(default = 3, ge=1, le =10)):
    return search(q, k)        