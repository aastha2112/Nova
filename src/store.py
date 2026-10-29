import chromadb

client = chromadb.PersistentClient(path="chroma_data")
collection = client.get_or_create_collection('knowledge')

def add_chunks(source: str, chunks: list[str]) -> None:
    collection.upsert(
        documents = chunks,
        ids = [f'{source} - {i}' for i in range(len(chunks))],
        metadatas = [{"source": source} for _ in chunks]
    )

def search(question: str, lim: int = 3)-> list[dict]:
    results = collection.query(query_texts = [question], n_results = lim)
    return [
        {'text': doc,  "source": meta["source"], "distance": dist}
        for doc, meta, dist in zip(
            results['documents'][0],
            results['metadatas'][0],
            results['distances'][0]
        )
    ]
