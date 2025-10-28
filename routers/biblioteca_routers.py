from fastapi import APIRouter, Depends, HTTPException
from models import Biblioteca
from dependencies import get_session
from main import bcrypt_context
from sqlalchemy.orm import Session
from schemas import BibliotecaSchema

# Criando uma rota para acesso da biblioteca
biblioteca_router = APIRouter(prefix="/bibliotecas", tags=["bibliotecas"])

# Retornando todas as bibliotecas cadastradas
@biblioteca_router.get("/")
async def home():
    return {"mensagem":"Todos os livros"}

# Cadastrando uma nova biblioteca
@biblioteca_router.post("/cadastrar")
async def register(biblioteca_schema: BibliotecaSchema, session: Session  = Depends(get_session)):
    senha_criptografada = bcrypt_context.hash(biblioteca_schema.senha)
    
    nova_biblioteca = Biblioteca(biblioteca_schema.nome, senha_criptografada, biblioteca_schema.email, biblioteca_schema.admin)
    session.add(nova_biblioteca)
    session.commit()
    return {"mensagem":"biblioteca cadastrada!"}