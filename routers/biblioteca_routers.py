from fastapi import APIRouter, Depends
from models import Biblioteca
from dependencies import get_session

biblioteca_router = APIRouter(prefix="/bibliotecas", tags=["bibliotecas"])

@biblioteca_router.get("/")
async def home():
    return {"mensagem":"Todos os livros"}

@biblioteca_router.post("/cadastrar")
async def register(nome: str, email: str, senha:str, session  = Depends(get_session)):
    return