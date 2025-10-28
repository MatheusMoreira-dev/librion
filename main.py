from fastapi import FastAPI

app = FastAPI()

from routers.livros_routers import livros_router
app.include_router(livros_router)

@app.get("/")
async def home():
    return {"mensagem": "Página inicial da API"}