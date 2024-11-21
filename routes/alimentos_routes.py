from fastapi import APIRouter, UploadFile, File
from model.alimentos_conn import AlimentosConnection
from schema.alimentos_schema import AlimentosSchema
import os

router = APIRouter()
alimentos_conn = AlimentosConnection()

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
            "porcion": data[8],
            "tipomedida": data[9]
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
            "porcion": data[8],
            "tipomedida": data[9]
        }
    else:
        return {"error": "Alimento not found"}

@router.post("/alimentos")
def insert_alimento(alimento_data: AlimentosSchema):
    # Preparar el diccionario de dat
    data = alimento_data.dict()

    # Llamar al método para insertar los datos en la base de datos
    alimentos_conn.write(data)

    # Retornar mensaje con éxito
    return {
        "message": "Alimento added successfully",
        "data": data  # Devuelve los datos insertados para referencia
    }


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
