from pydantic import BaseModel
from typing import Optional

class EjercicioSchema(BaseModel):
    idejercicios: Optional[int]
    idrutina: int
    nombre: str
    descripcion : str
    dificultad: str
    musculotrabajado: str
    imagen: Optional[str]  # Cambiado a str para la URL