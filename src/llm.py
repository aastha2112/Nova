from openai import AsyncOpenAI

from src.config import settings

client = AsyncOpenAI(
    api_key=settings.llm_api_key,
    base_url=settings.llm_base_url,
)

async def ask_llm(message: str, system: str='') -> str:
    messages = []
    if system:
        messages.append({'role': 'system', 'content': system})
    messages.append({'role': 'user', 'content': message})

    reply = await client.chat.completions.create(
        model=settings.llm_model,
        messages=messages,
        max_tokens=400,
        reasoning_effort="none",

    )
    print(reply)
    return reply.choices[0].message.content