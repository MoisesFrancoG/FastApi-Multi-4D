from pydantic import BaseModel
from typing import Optional

class AlimentosSchema(BaseModel):
    idalimentos: Optional[int]
    id_usuario: int
    nombre: str
    marca: Optional[str] = None
    calorias: int
    proteina: int
    carbohidratos: int
    grasa: int
    tamañoporcion: int
    tipomedida: str
