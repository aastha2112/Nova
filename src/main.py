from fastapi import FastAPI, HTTPException
from openai import APIError, RateLimitError
from pydantic import BaseModel, Field

from src.llm import ask_llm

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
        answer = await ask_llm(req.message)
        return ChatResponse(answer=answer)
    except RateLimitError:
        raise HTTPException(
            status_code=429,
            detail="API rate limit hit. Wait a minute and try again.",
        )    
    except APIError as e:
        raise HTTPException(status_code=500, detail=f'LLM Error: {e}')