from fastapi import FastAPI

app = FastAPI()

from routers.livro_routers import livro_router
app.include_router(livro_router)

@app.get("/")
async def home():
    return {"mensagem": "Página inicial da API"}