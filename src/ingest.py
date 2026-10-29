from src.loader import load_docs
from src.chunking import chunk_text
from src.store import add_chunks, collection

for doc in load_docs():
    chunks = chunk_text(doc['text'])
    add_chunks(doc['source'], chunks)
    print(f"{doc['source']}: {len(chunks)} chunks stored")

print("Total chunks in database:", collection.count())    