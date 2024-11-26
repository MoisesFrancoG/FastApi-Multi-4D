from pydantic import BaseModel
from typing import Optional

class ListSchema(BaseModel):
    idlistaalimentos: Optional[int]
    idcomida: int
    idalimento: int
    porcion: int  # Porción es obligatoria
    categoriacomida: str
