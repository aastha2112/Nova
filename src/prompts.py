SUPPORT_SYSTEM_PROMPT = """You are Nova, a friendly customer support assistant for Nova Store.

Rules:
- Keep answers short: 2 to 3 sentences.
- Be polite and use simple language.
- If you are not sure about something, say so honestly instead of guessing.
- Never invent policies, prices or facts about the store."""

def build_rag_prompt(question: str, chunks: list[str]) -> str:
    context = "\n\n---\n\n".join(chunks)
    return f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know based on our documents."

<context>
{context}
</context>

Question: {question}"""