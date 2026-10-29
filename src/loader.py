from pathlib import Path
from src.chunking import chunk_text

def load_docs(folder: str= 'knowledge') -> list[dict]:
    docs = []
    for path in sorted(Path(folder).glob('**/*.md')):
        docs.append({
            'source': path.name,
            'text': path.read_text(encoding='utf-8'),
        })
    return docs

if __name__ == '__main__':
    doc = load_docs()[0]
    chunks = chunk_text(doc["text"], size=200, overlap=50)
    for i, chunk in enumerate(chunks):
        print(i, chunk)