from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
from model.user_connection import UserConnection

# Configuración del JWT
SECRET_KEY = "mysecretkey"  # Cambiar por un valor seguro en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Instancia de la conexión a la base de datos
user_conn = UserConnection()
router = APIRouter()

# Modelos Pydantic para los endpoints
class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    nombre: str
    userpassword: str  # Contraseña sin encriptar (solo para demostración)
    email: str
    edad: int
    peso: int
    estatura: int
    sexo: str
    indiceactividad: int

# Función para crear un token de acceso
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Endpoint para el registro de usuario
@router.post("/register")
def register_user(user: UserRegister):
    existing_user = user_conn.get_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_data = user.dict()
    user_conn.write(user_data)
    return {"message": "User registered successfully"}

# Endpoint para el inicio de sesión
@router.post("/login")
def login_user(user: UserLogin):
    db_user = user_conn.get_by_email(user.email)
    if not db_user or db_user[2] != user.password:  # Verifica directamente la contraseña
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

# Dependencia para proteger rutas
def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = user_conn.get_by_email(email)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
