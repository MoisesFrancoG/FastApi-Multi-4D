from fastapi import APIRouter
from model.macros_connecction import MacrosConnecction
from schema.macros_schema import MacroSchema

router = APIRouter()
macros_conn = MacrosConnecction()

@router.get("/macros")
def get_Macros():
    items = []
    for data in macros_conn.read_all():
        dictionary = {
            "calorias": data[0],
            "proteina": data[1],
            "carbohidratos": data[2],
            "grasas": data[3],
            "id_usuario": data[4] 
        }
        items.append(dictionary)
    return items

@router.get("/macros/{id}")
def get_MacroUser(id: int):
    data = macros_conn.read_one(id)
    if data:
        return{
            "calorias": data[0],
            "proteina": data[1],
            "carbohidratos": data[2],
            "grasas": data[3],
            "id_usuario": data[4]
        }
    else: 
        return {"error": "Macros by id_usuario not found"}
    
@router.post("/macros")
def insert_macros(macros_data: MacroSchema):
    data = macros_data.dict()
    macros_conn.write(data)
    return {"message": "Macros added successfully"}

@router.put("/macros/{id}")
def update_macros(macros_data: MacroSchema,id :int):
    data = macros_data.dict()
    data["id_usuario"] = id
    macros_conn.update(data)
    return {"message": "Macros updated successfully"}

@router.delete("/macros/{id}")
def delete_macros(id: int):
    macros_conn.delete(id)
    return {"message": "Macros deleted successfully"}