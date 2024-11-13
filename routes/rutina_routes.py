from fastapi import APIRouter
from model.rutina_connec import RutinaConnection
from schema.rutina_schema import RutinaSchema

router = APIRouter()
rutina_conn = RutinaConnection()


@router.get("/rutinas")
def get_Rutinas():
    items = []
    for data in rutina_conn.read_all():
        dictionary = {
            "idrutina": data[0],
            "progresion": data[1],
            "tiempo": data[2],
            "fecha": data[3]
        }
        items.append(dictionary)
    return items


@router.get("/rutina/{id}")
def get_rutina(id: int):
    data = rutina_conn.read_one(id)
    if data: 
        return {
            "idrutina": data[0],
            "progresion": data[1],
            "tiempo": data[2],
            "fecha": data[3] 
        }
    else:
        return {"error: Rutina not found"}

@router.post("/rutina")
def insert_rutina(rutina_data: RutinaSchema):
    data = rutina_data.dict()
    rutina_conn.write(data)
    return {"message": "Rutina added successfully"}

@router.put("/rutina/{id}")
def update_rutine(rutine_data: RutinaSchema, id: int):
    data = rutine_data.dict()
    data["idrutina"] = id
    rutina_conn.update(data)
    return {"message": "Rutina updated successfully"}

@router.delete("/rutina/{id}")
def delete_rutine(id: int):
    rutina_conn.delete(id)
    return {"message": "Rutina deleted successfully"}