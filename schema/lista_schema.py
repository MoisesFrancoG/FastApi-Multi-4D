from pydantic import BaseModel
from typing import Optional

class ListSchema(BaseModel):
    idlistaalimentos: Optional[int]
    idcomida: int
    idalimento : int
    nombre: str
    marca: Optional[str]
    calorias: float
    proteina: float
    carbohidratos: float
    grasa : float
    porcion: int
    tipomedida :str
    categoriacomida: str