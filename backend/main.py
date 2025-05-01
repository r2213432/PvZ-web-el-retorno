# uvicorn main:app --reload
from fastapi import FastAPI
from routers import plantas, entidad, zombies
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

#Para permitir que otros puertos puedan acceder a la API

origins = [
    "http://127.0.0.1:5500",  # Tu frontend de desarrollo con Live Server
    "*",                      # Permitir todos los orígenes (solo para desarrollo, ¡cuidado en producción!)
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"],  # Permite todos los encabezados HTTP
)


app.include_router(plantas.router)
app.include_router(zombies.router)
app.include_router(entidad.router)
