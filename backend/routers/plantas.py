from fastapi import APIRouter, HTTPException, status
from backend.BD.modelos.planta import PlantaDB, Planta
from backend.BD.modelos.entidad import cuadro_columna, cuadro_fila
router = APIRouter()

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

@router.put("/planta_a_DB")
async def put_conversion(plantadb: PlantaDB, columna: cuadro_columna, fila: cuadro_fila):
    # Usamos model_dump() en lugar de dict() (Pydantic v2)
    planta_plantada = Planta(**plantadb.model_dump(), columna=columna, fila=fila)
    
    # Buscamos y quitamos la planta de la lista DB por id (no por objeto, ya que son distintos)
    for i, p in enumerate(lista_plantasDB):
        if p.id == plantadb.id:
            del lista_plantasDB[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Planta no creada")

    lista_plantas.append(planta_plantada)
    return planta_plantada


#pasar planta  a planta db
@router.put("/plantadb_a_n")
async def put_conversion(planta: Planta):
    planta_desplantada=PlantaDB(id=planta.id, tipo=planta.tipo, nombre=planta.nombre, vida=planta.vida,
                                tmp_atac=planta.tmp_atac, danho=planta.danho,
                                nivel=planta.nivel, rango=planta.rango)
    for i, p in enumerate(lista_plantas):
        if p.id == planta.id:
            del lista_plantas[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Planta no creada")
    lista_plantasDB.append(planta_desplantada)
    return planta_desplantada