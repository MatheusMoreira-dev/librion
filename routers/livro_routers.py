from fastapi import APIRouter

livros = APIRouter(prefix="/livros", tags=["livros"])

@livros.get("/")
def todos_os_livros():
    return {"mensagem":"Todos os livros"}