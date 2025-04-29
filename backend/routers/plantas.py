from fastapi import APIRouter, HTTPException, status
from backend.BD.cliente import cliente_pvz
from backend.BD.modelos.planta import PlantaDB, Planta
from backend.BD.esquemas.esquema_planta import planta_esquema, plantas_esquema, plantaBD_esquema, plantasBD_esquema


router = APIRouter(tags=["Plantas"])
cliente_planta = cliente_pvz.plantas
"""

# Lista simulada de base de datos
lista_plantasDB = [
    PlantaDB(id=1, tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, rango=3, nivel=1),
    PlantaDB(id=2, tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, rango=3, nivel=1),
    PlantaDB(id=3, tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, rango=3, nivel=2),
]

# Función de búsqueda
def buscar_plantaDB(id: int):
    for plantaDB in lista_plantasDB:
        if plantaDB.id == id:
            return plantaDB
    return None

# Obtener todas las plantas
@router.get("/plantasDB")
async def get_plantasDB():
    return lista_plantasDB

# Obtener una planta por ID
@router.get("/plantaDB/{id}")
async def get_plantaDB(id: int):
    planta = buscar_plantaDB(id)
    if not planta:
        raise HTTPException(status_code=404, detail="Planta no encontrada")
    return planta

# Crear una nueva planta
@router.post("/plantaDB", response_model=PlantaDB, status_code=201)
async def post_plantaDB(plantadb: PlantaDB):
    if buscar_plantaDB(plantadb.id):
        raise HTTPException(status_code=400, detail="PlantaDB ya existente")
    lista_plantasDB.append(plantadb)
    return plantadb

# Actualizar una planta existente
@router.put("/plantaDB", response_model=PlantaDB)
async def put_plantaDB(plantadb: PlantaDB):
    for index, plantaDB_guardada in enumerate(lista_plantasDB):
        if plantaDB_guardada.id == plantadb.id:
            lista_plantasDB[index] = plantadb
            return plantadb
    raise HTTPException(status_code=404, detail="Planta no encontrada")

# Eliminar una planta
@router.delete("/plantaDB/{id}")
async def delete_plantaDB(id: int):
    for index, planta_guardada in enumerate(lista_plantasDB):
        if planta_guardada.id == id:
            del lista_plantasDB[index]
            return {"detail": "Planta eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Planta no encontrada")

"""
def buscar_planta(campo: str, clave):
    try:
        planta = cliente_planta.find_one({campo: clave})
        return PlantaDB(**plantaBD_esquema(planta))
    except:
        return {"error": f"No se ha encontrado la plantaBD con los valores {campo} y {clave}"}
    
@router.get("/plantasBD")
async def get_plantasBD():
    return plantasBD_esquema(cliente_planta.find())
#Estas seran las plantas que se crearan para el jugador
# Lista simulada de base de datos
lista_plantas = [
    Planta(id=1, tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, rango=3, nivel=1, columna=1, fila=1),
    Planta(id=2, tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, rango=3, nivel=1,columna=2, fila=3),
    Planta(id=3, tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, rango=3, nivel=2,columna=1, fila=2),
]

# Función de búsqueda
def buscar_planta(id: int):
    for planta in lista_plantas:
        if planta.id == id:
            return planta
    return None

# Obtener todas las plantas
@router.get("/plantas")
async def get_plantas():
    return lista_plantas

# Obtener una planta por ID
@router.get("/planta/{id}")
async def get_planta(id: int):
    planta = buscar_planta(id)
    if not planta:
        raise HTTPException(status_code=404, detail="Planta no encontrada")
    return planta

# Crear una nueva planta
@router.post("/planta", response_model=PlantaDB, status_code=201)
async def post_planta(planta: Planta):
    if buscar_planta(planta.id):
        raise HTTPException(status_code=400, detail="Planta ya existente")
    lista_plantas.append(planta)
    return planta

# Actualizar una planta existente
@router.put("/planta", response_model=Planta)
async def put_planta(planta: Planta):
    for index, planta_guardada in enumerate(lista_plantas):
        if planta_guardada.id == planta.id:
            lista_plantas[index] = planta
            return planta
    raise HTTPException(status_code=404, detail="Planta no encontrada")

# Eliminar una planta
@router.delete("/planta/{id}")
async def delete_planta(id: int):
    for index, planta_guardada in enumerate(lista_plantas):
        if planta_guardada.id == id:
            del lista_plantas[index]
            return {"detail": "Planta eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Planta no encontrada")

