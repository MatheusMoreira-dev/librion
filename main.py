from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from routers.livro_routers import livro_router
from routers.biblioteca_routers import biblioteca_router

app.include_router(livro_router)
app.include_router(biblioteca_router)

@app.get("/")
async def home():
    return {"mensagem": "Página inicial da API"}