import chromadb

client = chromadb.PersistentClient(path="chroma_data")
collection = client.get_or_create_collection('knowledge')

def add_chunks(source: str, chunks: list[str]) -> None:
    collection.upsert(
        documents = chunks,
        ids = [f'{source} - {i}' for i in range(len(chunks))],
        metadatas = [{"source": source} for _ in chunks]
    )