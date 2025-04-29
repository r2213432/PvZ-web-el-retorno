from fastapi import APIRouter, HTTPException, status
from backend.BD.modelos.planta import PlantaDB, Planta
from enum import Enum

router = APIRouter()

lista_plantasDB = [
    PlantaDB(id="1", tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, rango=3, nivel=1),
    PlantaDB(id="2", tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, rango=3, nivel=1),
    PlantaDB(id="3", tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, rango=3, nivel=2),
]

@router.get("/plantasDB")
async def get_plantasDB():
    return lista_plantasDB

@router.get("/plantaDB/{id}")
async def get_plantaDB(id: int):
    planta = buscar_plantaDB(id)
    if isinstance(planta, dict) and "error" in planta:
        raise HTTPException(status_code=404, detail=planta["error"])
    return planta

@router.post("/plantaDB", response_model=PlantaDB, status_code=201)
async def post_plantaDB(plantadb: PlantaDB):
    if buscar_plantaDB(plantadb.id):
        raise HTTPException(status_code=400, detail="plantadb ya existente")
    lista_plantasDB.append(plantadb)
    return plantadb

@router.put("/plantaDB")
async def put_plantaDB(plantadb: PlantaDB):
    for index, plantaDB_guardada in enumerate(lista_plantasDB):
        if plantaDB_guardada.id == plantadb.id:
            lista_plantasDB[index] = plantadb
            return plantadb
    raise HTTPException(status_code=404, detail="Planta no encontrada")

@router.delete("/plantaDB/{id}")
async def delete_plantaDB(id: int):
    for index, planta_guardada in enumerate(lista_plantasDB):
        if planta_guardada.id == id:
            del lista_plantasDB[index]
            return {"detail": "Planta eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Planta no encontrada")

def buscar_plantaDB(id: int):
    for plantaDB in lista_plantasDB:
        if plantaDB.id == id:
            return plantaDB
    return {"error": "Planta no encontrada"}