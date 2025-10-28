from models import db
from sqlalchemy.orm import sessionmaker

async def get_session():
    try:
        Session = sessionmaker(bind=db) # Classe Session
        session = Session() #Instância(objeto) da classe
        yield session # Retorna uma session sobdemanda
    finally:
        session.close()