from fastapi import APIRouter, UploadFile, File
from model.ejercicios_connecction import EjercicioConnection
from schema.ejercicios_schema import EjercicioSchema
import os

router = APIRouter()
ejercicio_conn = EjercicioConnection()
UPLOAD_DIR = "uploads/"  # Directorio donde se guardarán las imágenes

# Asegúrate de que el directorio existe
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/ejercicios")
def get_Ejercicios():
    items = []
    for data in ejercicio_conn.read_all():
        dictionary = {
        "idejercicios": data[0],
        "idrutina": data[1],
        "nombre": data[2],
        "descripcion": data[3],
        "dificultad": data[4],
        "musculotrabajado": data[5],
        "imagen" : data[6]
        }
        items.append(dictionary)
    return items

@router.get("/ejerciciosbyRutine/{id}")
def get_ejercicio(id: int):
    items = []
    for data in ejercicio_conn.read_one(id):
        dictionary = {
        "idejercicios": data[0],
        "idrutina": data[1],
        "nombre": data[2],
        "descripcion": data[3],
        "dificultad": data[4],
        "musculotrabajado": data[5],
        "imagen" : data[6]
        }
        items.append(dictionary)
    return items
    
@router.post("/ejercicios")
async def insert_exercise(
    idrutina: int,
    nombre: str,
    descripcion: str,
    dificultad: str,
    musculotrabajado: str,
    imagen: UploadFile = File(None)
):
    image_url = None
    if imagen:
        image_filename = f"{UPLOAD_DIR}{imagen.filename}"
        with open(image_filename, "wb") as image_file:
            image_file.write(await imagen.read())
        # URL de acceso a la imagen (puedes ajustar esto según la URL base de tu servidor)
        image_url = f"/{image_filename}"

    data = {
        "idrutina": idrutina,
        "nombre": nombre,
        "descripcion": descripcion,
        "dificultad": dificultad,
        "musculotrabajado": musculotrabajado,
        "imagen": image_url
    }
    ejercicio_conn.write(data)
    return {
        "message": "Ejercicio added with image URL",
        "data" : data
        }


@router.put("/ejercicio/{id}")
def update_exercise(ejercicio_data: EjercicioSchema , id:int):
    data = ejercicio_data.dict()
    data["idejercicios"] = id
    ejercicio_conn.update(data)
    return {"message": "Ejercicio updated"}

@router.delete("/ejercicios/{id}")
def delete_exercise(id:int):
    ejercicio_conn.delete(id)
    return {"message": "Ejercicios deleted"}