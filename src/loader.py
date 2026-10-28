from pathlib import Path

def load_docs(folder: str= 'knowledge') -> list[dict]:
    docs = []
    for path in sorted(Path(folder).glob('**/*.md')):
        docs.append({
            'source': path.name,
            'text': path.read_text(encoding='utf-8'),
        })
    return docs

if __name__ == '__main__':
    for doc in load_docs():
        print(doc["source"], "->", len(doc["text"]), "characters")