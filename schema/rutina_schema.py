from pydantic import BaseModel
from typing import Optional

class RutinaSchema(BaseModel):
    idrutina: Optional[int]
    progresion : str
    tiempo : str
    fecha : str 
    nombre : str