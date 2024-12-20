from fastapi import APIRouter
from model.consumo_alimentos import ConsumoConnec
from schema.consumo_schema import ConsumoSchema

router = APIRouter()
consumos_conn = ConsumoConnec()

@router.get("/consumo")
def get_consumos():
    items = []
    for data in consumos_conn.read_all():
        dictionary ={
            "idconsumo": data[0],
            "id_usuario" : data[1],
            "fecha": data[2],
        }
        items.append(dictionary)
    return items

@router.get("/consumo/{id}")
def get_consumo(id: int):
    data = consumos_conn.read_one(id)
    if data:
        return {
            "idconsumo": data[0],
            "id_usuario": data[1],
            "fecha": data[2]
        }
    else: 
        return {"error": "Alimento not found"}
    
@router.get("/consumo/dia/{id_usuario}")
def get_consumo_dia_actual(id_usuario: int):
    idconsumo = consumos_conn.get_or_create_daily_consumo(id_usuario)
    return {"idconsumo": idconsumo}

@router.get("/consumo/historial/{id_usuario}")
def get_historial_consumos(id_usuario: int):
    items = []
    for data in consumos_conn.get_all_by_user(id_usuario):
        dictionary = {
            "idconsumo": data[0],
            "id_usuario": data[1],
            "fecha": data[2]
        }
        items.append(dictionary)
    return items

    
@router.post("/consumo")
def insert_consumo(consumo_data: ConsumoSchema):
    data = consumo_data.dict()
    idconsumo = consumos_conn.write(data)
    return {
        "message": "Consumo alimentos added successfully",
        "idconsumo": idconsumo
    }


@router.put("/consumo/{id}")
def update_consumo(consumo_data: ConsumoSchema, id: int):
    data  = consumo_data.dict()
    data["idconsumo"] = id
    consumos_conn.update(data)
    return {"message: Consumo alimentos updated successfully"}

@router.delete("/consumo/{id}")
def delete_consumo(id : int):
    consumos_conn.delete(id)
    return {"message: Consumo alimentos deleted successfully"}