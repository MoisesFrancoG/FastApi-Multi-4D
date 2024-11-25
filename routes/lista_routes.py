from fastapi import APIRouter
from model.list_connection import ListaConnection
from schema.lista_schema import ListSchema

router = APIRouter()
list_conn = ListaConnection()

@router.get("/listaalimentos")
def getListas():
    items = []
    for data in list_conn.read_all():
        dictionary = {
            "idlistaalimentos": data[0],
            "idcomida": data[1],
            "idalimento": data[2],
            "nombre": data[3],
            "marca": data[4],
            "calorias": data[5],
            "proteina":data[6],
            "carbohidratos":data[7],
            "grasa": data[8],
            "porcion": data[9],
            "tipomedida": data[10],
            "categoriacomida": data[11]
        }
        items.append(dictionary)
    return items


@router.get("/listaalimentos/{id}")
def get_lista(id: int):
    items = []
    for data in list_conn.read_one(id):
        dictionary = {
            "idlistaalimentos": data[0],
            "idcomida": data[1],
            "idalimento": data[2],
            "nombre": data[3],
            "marca": data[4],
            "calorias": data[5],
            "proteina":data[6],
            "carbohidratos":data[7],
            "grasa": data[8],
            "porcion": data[9],
            "tipomedida": data[10],
            "categoriacomida": data[11]
        }
        items.append(dictionary)
    return items

@router.post("/lista")
def insert_lista(lista_data: ListSchema):
    data  = lista_data.dict()
    list_conn.write(data)
    return {"message": "Lista added"}

@router.put("/lista/{id}")
def update_lista(lista_data: ListSchema, id: int):
    data = lista_data.dict()
    data["idlistaalimentos"] = id
    list_conn.update(data)
    return {"message": "Lista updated"}

@router.delete("/list/{id}")
def delete_list(id: int):
    list_conn.delete(id)
    return {"message": "Lista deleted"}