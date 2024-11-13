from fastapi import APIRouter
from model.ejercicios_connecction import EjercicioConnection
from schema.ejercicios_schema import EjercicioSchema

router = APIRouter()
ejercicio_conn = EjercicioConnection()

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
        "musculotrabajado": data[5]
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
        "musculotrabajado": data[5]
        }
        items.append(dictionary)
    return items
    
@router.post("/ejercicios")
def insert_exercise(ejercicio_data : EjercicioSchema):
    data = ejercicio_data.dict()
    ejercicio_conn.write(data)
    return {"message" : "Ejercicio added"}


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