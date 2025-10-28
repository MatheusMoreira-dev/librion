from fastapi import APIRouter, Depends
from dependencies import get_session
from models import Usuario
from sqlalchemy.orm import Session

usuario_router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@usuario_router.get("/")
async def home(session: Session = Depends(get_session)):
    usuarios = session.query(Usuario).all()
    return usuarios

@usuario_router.post("/login")
async def login(session: Session = Depends(get_session)):
    return