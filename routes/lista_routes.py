from fastapi import APIRouter
from model.list_connection import ListaConnection
from schema.lista_schema import ListSchema
from model.alimentos_conn import AlimentosConnection

router = APIRouter()
list_conn = ListaConnection()
alimentos_conn = AlimentosConnection()
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
    
    idalimento = lista_data.idalimento
    porcion = lista_data.porcion

    
    alimento_data = alimentos_conn.read_one(idalimento)
    if not alimento_data:
        return {"error": "Alimento no encontrado"}

    
    factor = porcion / alimento_data[8]  
    calorias = alimento_data[4] * factor
    proteina = alimento_data[5] * factor
    carbohidratos = alimento_data[6] * factor
    grasa = alimento_data[7] * factor

    data = {
        "idcomida": lista_data.idcomida,
        "idalimento": idalimento,
        "nombre": alimento_data[2],  
        "marca": alimento_data[3],  
        "calorias": calorias,
        "proteina": proteina,
        "carbohidratos": carbohidratos,
        "grasa": grasa,
        "porcion": porcion,
        "tipomedida": alimento_data[9],  
        "categoriacomida": lista_data.categoriacomida,  
    }

    
    list_conn.write(data)

    return {"message": "Lista added successfully", "data": data}


@router.put("/lista/{id}")
def update_lista(id: int, lista_data: ListSchema):
    try:
        data = lista_data.dict()
        data['idlistaalimentos'] = id  

        
        list_conn.update(data)

        return {"message": "Lista updated successfully", "data": data}
    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": "An unexpected error occurred", "details": str(e)}


@router.delete("/list/{id}")
def delete_list(id: int):
    list_conn.delete(id)
    return {"message": "Lista deleted"}