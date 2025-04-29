from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from backend.routers import entidad
from enum import Enum

router = APIRouter()

class cuadro_columna(Enum):
    COLUMNA1 = 1
    COLUMNA2 = 2
    COLUMNA3 = 3
    COLUMNA4 = 4
    COLUMNA5 = 5

class cuadro_fila(Enum):
    FILA1 = 1
    FILA2 = 1
    FILA3 = 1
    FILA4 = 1
    FILA5 = 1
    FILA6 = 1
    FILA7 = 1
    FILA8 = 1
    FILA9 = 1

class PlantaDB(entidad.Entidad):
    rango: int
    nivel: int

class Planta(PlantaDB):
    esta_plantado: bool
    columna: cuadro_columna
    fila: cuadro_fila

lista_plantasDB = [
    PlantaDB(id=1, tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, rango=3, nivel=1),
    PlantaDB(id=2, tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, rango=3, nivel=1),
    PlantaDB(id=3, tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, rango=3, nivel=2),
]

@router.get("/plantasDB")
async def get_plantasDB():
    return lista_plantasDB

@router.get("/plantaDB/{id}")
async def get_plantaDB(id: int):
    return buscar_plantaDB(id)

@router.post("/plantaDB", response_model=PlantaDB, status_code=201)
async def post_plantaDB(plantadb: PlantaDB):
    if type(buscar_plantaDB(plantadb.id)) == PlantaDB:
        raise HTTPException(status_code=204, detail="plantadb ya existente")
    lista_plantasDB.append(plantadb)
    return plantadb

@router.put("/plantaDB")
async def put_plantaDB(plantadb: PlantaDB):
    found=False
    for index, plantaDB_guardada in enumerate(lista_plantasDB):
        if plantaDB_guardada.id == plantadb.id:
            lista_plantasDB[index] = plantadb
            found = True
        if not found:
            raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                                 detail="no se ha actualizado")
        else:
            return plantadb

@router.delete("/plantaDB/{id}")
async def delete_plantaDB(id:int):
    found = False 
    for index,  planta_guardada in enumerate(lista_plantasDB):
        if planta_guardada.id == id:
            del lista_plantasDB[index] 
            found = True
            raise HTTPException(status_code=status.HTTP_200_OK)
    if found == False:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="no modificado")
    



def buscar_plantaDB(id: int):
    plantasDB = filter(lambda plantaDB: plantaDB.id == id, lista_plantasDB)
    try:
        return list(plantasDB)[0]
    except:
        return {"error": "no se ha encontrado el usuario"}
    