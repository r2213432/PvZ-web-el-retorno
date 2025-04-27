# uvicorn main:app --reload
from fastapi import FastAPI
from routers import plantas, entidad
from fastapi.staticfiles import StaticFiles

app = FastAPI() 

app.include_router(plantas.router)
app.include_router(entidad.router)