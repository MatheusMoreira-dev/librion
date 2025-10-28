from fastapi import APIRouter
from models import Livro

livro_router = APIRouter(prefix="/livros", tags=["livros"])

@livro_router.get("/")
async def home():
    return {"mensagem":"Todos os livros"}

@livro_router.post("/")
async def criar_livro():
    return