from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

# Carregando a minha SecretKey do Arquivo .env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# "Abrindo a minha API"
app = FastAPI()

# Instânciando um objeto da classe CryptContext para ser utilizado em outras partes
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Importando as rotas
from routers.livro_routers import livro_router
from routers.biblioteca_routers import biblioteca_router

# Associando as rotas ao meu app
app.include_router(livro_router)
app.include_router(biblioteca_router)