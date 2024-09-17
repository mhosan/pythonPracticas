import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4]

@app.get('/contacto')
def get_list():
    return {"name": "Marcelito"}

@app.get('/html', response_class=HTMLResponse)
def get_list():
    return """
    <h1>Hola mundo</h1>
"""

def run():
    store.getCategories()

if __name__=='__main__':
    run()