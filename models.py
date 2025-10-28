from sqlalchemy import create_engine, Column, String, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///librion.db")
Base = declarative_base()

class Biblioteca(Base):
    __tablename__ = "bibliotecas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    email = Column("email", String, nullable=False)
    admin = Column("admin", Boolean, default=False, nullable=False)

    def __init__(self, nome, email, senha, admin = False):
        self.nome = nome
        self.admin = admin
        self.email = email
        self.senha = senha

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

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer,  primary_key=True, autoincrement=True)
    nome = Column("nome_completo", String, nullable=False)
    idade = Column("idade", Integer, nullable=False)
    biblioteca_mae = Column("biblioteca_mae", ForeignKey("bibliotecas.id"), nullable=False)

    def __init__(self, nome, idade, biblioteca_mae):
        self.nome = nome
        self.idade = idade
        self.biblioteca_mae = biblioteca_mae

#Tabela Associativa (livro_biblioteca) (e)
class BibliotecaLivro(Base):
    __tablename__ = "biblioteca_livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_livro = Column("fk_livro", ForeignKey("livros.id"), nullable=False)
    id_biblioteca = Column("fk_biblioteca", ForeignKey("bibliotecas.id"), nullable=False)
    quantidade = Column("quantidade", Integer, default=1, nullable=False)
    disponivel = Column("disponivel", Boolean, default=True, nullable=False)
    is_global = Column("is_global", Boolean, default=False, nullable=False)

    def __init__(self, id_livro, id_biblioteca, quantidade = 1, disponivel = True, is_global = False):
        self.id_livro = id_livro
        self.id_biblioteca = id_biblioteca
        self.quantidade = quantidade
        self.disponivel = disponivel
        self.is_global = is_global

#Tabela Associativa (Usuario_livro) (Empréstimo)
class UsuarioLivro(Base):
    __tablename__ = "usuario_livros"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    id_biblioteca_livro = Column("id_biblioteca_livro", ForeignKey("biblioteca_livros.id"), nullable=False)
    data_solicitacao = Column("data_solicitacao", String, nullable=False)
    data_retirada = Column("data_retirada", String, nullable=False)
    data_devolucao = Column("data_devolucao", String, nullable=False)