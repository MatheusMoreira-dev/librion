from models import db
from sqlalchemy.orm import sessionmaker

async def get_session():
    try:
        Session = sessionmaker(bind=db) # Classe Session
        session = Session() #Instância(objeto) da classe
        yield session # Retorna uma session sobdemanda
    finally:
        session.close()

async def create_token(identifier):
    token = f"mdashgfasyhduiweyw{identifier}"
    return token

async def authenticate_user(email, senha, session, Entity):
    user = session.query(Entity).filter(Entity.email == email).first()
