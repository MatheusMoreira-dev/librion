from fastapi import APIRouter, Depends, HTTPException
from models import Biblioteca
from dependencies import get_session
from main import bcrypt_context
from sqlalchemy.orm import Session
from schemas import BibliotecaSchema, LoginBibliotecaSchema

# Criando uma rota para acesso da biblioteca
biblioteca_router = APIRouter(prefix="/bibliotecas", tags=["Bibliotecas"])

# Retornando todas as bibliotecas cadastradas
@biblioteca_router.get("/")
async def bibliotecas(session: Session = Depends(get_session)):
    """Retorna todas as bibliotecas cadastradas"""
    bibliotecas = session.query(Biblioteca).all()
    return bibliotecas

# Cadastrando uma nova biblioteca
@biblioteca_router.post("/cadastro")
async def cadastrar(biblioteca_schema: BibliotecaSchema, session: Session  = Depends(get_session)):
    """Cadastrar uma nova biblioteca"""
    biblioteca = session.query(Biblioteca).filter(Biblioteca.email == biblioteca_schema.email).first()
    
    if biblioteca:
        # Se a biblioteca já existir
        raise HTTPException(status_code=400, detail="Biblioteca já cadastrada")
    else:
        # Criptografa a  senha
        senha_criptografada = bcrypt_context.hash(biblioteca_schema.senha)
        
        # cria um objeto da biblioteca
        nova_biblioteca = Biblioteca(**biblioteca_schema.model_dump(exclude_unset=True))
        
        # Adiciona no banco pelo session
        session.add(nova_biblioteca)
        session.commit()
        return {"mensagem":"biblioteca cadastrada!"}

@biblioteca_router.get("/login")
async def login(login_schema: LoginBibliotecaSchema, session: Session = Depends(get_session)):
    """Acessar uma conta já cadastrada se existir"""
    biblioteca = session.query(Biblioteca).filter(Biblioteca.email == login_schema.email).first()
    if not biblioteca:
        raise HTTPException(status_code=400, detail="Biblioteca não cadastrada!")
    
    else:
        return login_schema