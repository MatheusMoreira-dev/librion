from fastapi import APIRouter

livros_router = APIRouter(prefix="/livros", tags=["livros"])

@livros_router.get("/")
async def todos_os_livros():
    return {"mensagem":"Todos os livros"}