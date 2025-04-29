# uvicorn main:app --reload
from fastapi import FastAPI
from backend.routers import plantas, entidad, zombies
from fastapi.staticfiles import StaticFiles

app = FastAPI() 

app.include_router(plantas.router)
app.include_router(zombies.router)
app.include_router(entidad.router)