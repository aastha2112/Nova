from fastapi import FastAPI

app = FastAPI(title='Nova')

@app.get('/health')
def health_check():
    return {'status': 'all GOOD'}

@app.get('/hello/{name}')  
def greet_user(name: str):
    return {'message': f'Hello, {name}!!'}  