from pydantic import BaseModel
from typing import Optional

class AlimentosSchema(BaseModel):
    idalimentos: Optional[int]
    id_usuario: int
    nombre: str
    marca: Optional[str] = None
    calorias: float
    proteina: float
    carbohidratos: float
    grasa: float
    porcion: int
    tipomedida: str
    categoria: str
    
    