from fastapi import APIRouter,Depends
from model.user_connection import UserConnection
from schema.user_schema import UserSchema
from routes.auth_routes import get_current_user
router = APIRouter()
user_conn = UserConnection()

@router.get("/users")
def get_users(#current_user: dict = Depends(get_current_user)
              ):
    items = []
    for data in user_conn.read_all():
        dictionary = {
            "idusuario": data[0],
            "nombre": data[1],
            "userpassword": data[2],
            "email": data[3],
            "edad": data[4],
            "peso": data[5],    
            "estatura": data[6],
            "sexo": data[7],
            "indiceactividad": data[8]
        }
        items.append(dictionary)
    return items

@router.get("/user/{id}")
def get_user(id: int):
    data = user_conn.read_one(id)
    if data:
        return {
            "idusuario": data[0],
            "nombre": data[1],
            "userpassword": data[2],
            "email": data[3],
            "edad": data[4],
            "peso": data[5],
            "estatura": data[6],
            "sexo": data[7],
            "indiceactividad": data[8]
        }
    else:
        return {"error": "User not found"}

@router.post("/user")
def insert_user(user_data: UserSchema):
    data = user_data.dict()
    user_conn.write(data)
    return {"message": "User added successfully"}

@router.put("/user/{id}")
def update_user(user_data: UserSchema, id: int):
    data = user_data.dict()
    data["idusuario"] = id
    user_conn.update(data)
    return {"message": "User updated successfully"}

@router.delete("/user/{id}")
def delete_user(id: int):
    user_conn.delete(id)
    return {"message": "User deleted successfully"}
