from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///librion.db")
Base = declarative_base()

class Livro(Base):
    __tablename__ = "livros"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    isbn = Column("isbn", Integer, nullable=False)
    titulo = Column("titulo", String, nullable=False)
    sinopse = Column("sinopse", String)
    categoria = Column("categoria", String)
    autor = Column("autor", String)
    data_lancamento = Column("data_lancamento", String)
    imagem_capa = Column("imagem_capa", String)

    def __init__(self, isbn, titulo, sinopse, categoria, autor, data_lancamento, imagem_capa):
        self.isbn = isbn
        self.titulo = titulo
        self.sinopse = sinopse
        self.categoria = categoria
        self.autor = autor
        self.data_lancamento = data_lancamento
        self.imagem_capa = imagem_capa
