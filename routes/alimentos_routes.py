from fastapi import APIRouter, UploadFile, File
from model.alimentos_conn import AlimentosConnection
from schema.alimentos_schema import AlimentosSchema
import os

router = APIRouter()
alimentos_conn = AlimentosConnection()
UPLOAD_DIR = "uploads/"  # Directorio donde se guardarán las imágenes

# Asegúrate de que el directorio existe
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/alimentos")
def get_alimentos():
    items = []
    for data in alimentos_conn.read_all():
        dictionary = {
            "idalimentos": data[0],
            "id_usuario": data[1],
            "nombre": data[2],
            "marca": data[3],
            "calorias": data[4],
            "proteina": data[5],
            "carbohidratos": data[6],
            "grasa": data[7],
            "tamañoporcion": data[8],
            "tipomedida": data[9],
            "imagen": data[10]
        }
        items.append(dictionary)
    return items

@router.get("/alimentos/{id}")
def get_alimento(id: int):
    data = alimentos_conn.read_one(id)
    if data:
        return {
            "idalimentos": data[0],
            "id_usuario": data[1],
            "nombre": data[2],
            "marca": data[3],
            "calorias": data[4],
            "proteina": data[5],
            "carbohidratos": data[6],
            "grasa": data[7],
            "tamañoporcion": data[8],
            "tipomedida": data[9],
            "imagen": data[10]
        }
    else:
        return {"error": "Alimento not found"}

@router.post("/alimentos")
async def insert_alimento(
    id_usuario: int,
    nombre: str,
    calorias: int,
    proteina: int,
    carbohidratos: int,
    grasa: int,
    tamañoporcion: int,
    tipomedida: str,
    imagen: UploadFile = File(None),
    marca: str = None
):
    image_url = None
    if imagen:
        image_filename = f"{UPLOAD_DIR}{imagen.filename}"
        with open(image_filename, "wb") as image_file:
            image_file.write(await imagen.read())
        # URL de acceso a la imagen (ajustar según la URL base del servidor)
        image_url = f"/{image_filename}"

    data = {
        "id_usuario": id_usuario,
        "nombre": nombre,
        "marca": marca,
        "calorias": calorias,
        "proteina": proteina,
        "carbohidratos": carbohidratos,
        "grasa": grasa,
        "tamañoporcion": tamañoporcion,
        "tipomedida": tipomedida,
        "imagen": image_url
    }
    alimentos_conn.write(data)
    return {"message": "Alimento added with image URL"}

@router.put("/alimentos/{id}")
def update_alimento(alimento_data: AlimentosSchema, id: int):
    data = alimento_data.dict()
    data["idalimentos"] = id
    alimentos_conn.update(data)
    return {"message": "Alimento updated"}

@router.delete("/alimentos/{id}")
def delete_alimento(id: int):
    alimentos_conn.delete(id)
    return {"message": "Alimento deleted"}
