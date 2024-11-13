from pydantic import BaseModel
from typing import Optional

class ConsumoSchema(BaseModel):
    idconsumo : Optional[int]
    id_usuario : int
    fecha : str
