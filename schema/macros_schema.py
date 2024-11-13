from pydantic import BaseModel

class MacroSchema(BaseModel):
    calorias: int
    proteina: int
    carbohidratos: int
    grasas: int
    id_usuario: int