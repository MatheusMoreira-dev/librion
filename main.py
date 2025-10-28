from fastapi import FastAPI

app = FastAPI()

from routers import livro_routers
app.include_router(livro_routers)

@app.get("/")
def home():
    return {"mensagem": "Página inicial da API"}