from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.users_routes import router as users_router
from routes.alimentos_routes import router as alimentos_router
from routes.consumo_routes import router as consumos_router
from routes.rutina_routes import router as rutine_router
from routes.macros_routes import router as macros_router
from routes.ejercicios_routes import router as ejerc_router
from routes.lista_routes import router as list_router
from routes.auth_routes import router as auth_router

app = FastAPI()

# Esto es crucial para habilitar CORS correctamente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Específica dominios en producción
    allow_credentials=True,
    allow_methods=["*"],  # O especifica métodos: ['GET', 'POST']
    allow_headers=["*"],
)

# Montar la carpeta `uploads` para servir archivos estáticos
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
# Registra las rutas
app.include_router(users_router, prefix="/api", tags=["Usuarios"])
app.include_router(alimentos_router, prefix="/api", tags=["Alimentos"])
app.include_router(consumos_router, prefix="/api", tags=["Consumo Alimentos"])
app.include_router(rutine_router, prefix="/api", tags=["Rutinas"])
app.include_router(macros_router, prefix="/api", tags=["Macros"])
app.include_router(ejerc_router, prefix="/api",tags=["Ejercicios"])
app.include_router(list_router, prefix="/api", tags=["Lista Alimentos"])
app.include_router(auth_router, prefix="/api", tags=["Auth"])

@app.get("/")
def main():
    return {"message": "Welcome to Macrofusion"}
