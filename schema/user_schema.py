from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    idusuario: Optional[int]
    nombre: str
    userpassword : str
    email: str
    edad: int
    peso: int
    estatura: int
    sexo: str
    indiceactividad: int 
    