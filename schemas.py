from pydantic import BaseModel
from typing import Optional

class BibliotecaSchema(BaseModel):
    nome: str
    senha: str
    email: str
    admin: Optional[bool]

    class Config:
        from_attributes = True