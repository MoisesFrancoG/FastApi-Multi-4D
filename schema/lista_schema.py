from pydantic import BaseModel
from typing import Optional

class ListSchema(BaseModel):
    idlistaalimentos: Optional[int]
    idcomida: int
    idalimento : int
    nombre: str
    marca: Optional[str]
    calorias: int
    proteina: int
    carbohidratos: int
    grasa : int
    tamañoporcion: int
    tipomedida :str
    categoriacomida: str