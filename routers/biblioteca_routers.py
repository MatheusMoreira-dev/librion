from fastapi import APIRouter, Depends, HTTPException
from models import Biblioteca
from dependencies import get_session
from main import bcrypt_context

biblioteca_router = APIRouter(prefix="/bibliotecas", tags=["bibliotecas"])

@biblioteca_router.get("/")
async def home():
    return {"mensagem":"Todos os livros"}

@biblioteca_router.post("/cadastrar")
async def register(nome: str, email: str, senha:str, session  = Depends(get_session)):
    senha_criptografada = bcrypt_context.hash(senha)
    
    nova_biblioteca = Biblioteca(nome, senha_criptografada, email)
    session.add(nova_biblioteca)
    session.commit()
    return {"mensagem":"biblioteca cadastrada!"}