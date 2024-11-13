from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union


class Usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int
    password: str
    correo: str


app = FastAPI()

usuarios = [

]


@app.get("/")
def main():
    return {"message": "Hello Welcome to MACROFUSION"}


@app.post("/usuario")
def crearUsuario(usuario: Usuario):

    try:
        id = len(usuarios) + 1
        usuarios.append({
            "id": len(usuarios) + 1,
            "nombre": usuario.nombre,
            "apellido": usuario.apellido,
            "edad": usuario.password,
            "password": usuario.password,
            "correo": usuario.correo
        })

        return {
            "message": "El usuario ha sido creado",
            "usuario": {
                "id": len(usuarios)+1,
                "usuario": usuario.nombre
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/usuarios")
def obtenerUsuarios(id: Union[int, None] = None):
    try:

        if id is not None:
            if id < 0 or id > len(usuarios):
                raise HTTPException(
                    status_code=404, detail="El usuario no exite")
            return {
                "message": "Usuario encontrado",
                "usuario": usuarios[id-1]
            }
        return {
            "message": "Lista de usuarios",
            "usuarios": usuarios
        }
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))


@app.put("/usuarios/{id}")
def modificarUsuario(id: int, nombre: str):
    try:
        if id <= 0 or id > len(usuarios):
            raise HTTPException(status_code=400, detail="el usuario no existe")
        else:
            usuarios[id-1]["nombre"] = nombre
        return {
            "message": "Usuarios actualizado",
            "usuario": usuarios[id-1]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/usuarios/{id}")
def deleteUserbyId(id: int):
    try:
        if id < 0 or id > len(usuarios):
            raise HTTPException(
                status_code=404, detail="El usuario no exite")
        else:
            usuarios.remove(usuarios[id-1])
            return {
                "message": "Ususario eliminado",
                "id": id
            }
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
