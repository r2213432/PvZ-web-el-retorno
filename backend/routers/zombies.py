from fastapi import APIRouter, HTTPException
from backend.BD.modelos.zombie import ZombieDB, Zombie
from backend.BD.modelos.entidad import cuadro_columna, cuadro_fila

router = APIRouter()

# Lista de zombis simulada como base de datos
lista_zombiesDB = [
    ZombieDB(id="", tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, velocidad=3, nivel=1),
    ZombieDB(id="", tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, velocidad=3, nivel=1),
    ZombieDB(id="", tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, velocidad=3, nivel=2),
]

# Buscar zombie por ID
def buscar_zombieDB(id: int):
    for zombieDB in lista_zombiesDB:
        if zombieDB.id == id:
            return zombieDB
    return None

# GET todos los zombis
@router.get("/zombiesDB")
async def get_zombiesDB():
    return lista_zombiesDB

# GET un zombi por ID
@router.get("/zombieDB/{id}")
async def get_zombieDB(id: int):
    zombie = buscar_zombieDB(id)
    if not zombie:
        raise HTTPException(status_code=404, detail="Zombie no encontrado")
    return zombie

# POST - agregar un nuevo zombi
@router.post("/zombieDB", response_model=ZombieDB, status_code=201)
async def post_zombieDB(zombiedb: ZombieDB):
    if buscar_zombieDB(zombiedb.id):
        raise HTTPException(status_code=400, detail="ZombieDB ya existente")
    lista_zombiesDB.append(zombiedb)
    return zombiedb

# PUT - actualizar un zombi existente
@router.put("/zombieDB", response_model=ZombieDB)
async def put_zombieDB(zombiedb: ZombieDB):
    for index, zombieDB_guardada in enumerate(lista_zombiesDB):
        if zombieDB_guardada.id == zombiedb.id:
            lista_zombiesDB[index] = zombiedb
            return zombiedb
    raise HTTPException(status_code=404, detail="Zombie no encontrado")

# DELETE - eliminar un zombi por ID
@router.delete("/zombieDB/{id}")
async def delete_zombieDB(id: int):
    for index, zombie_guardada in enumerate(lista_zombiesDB):
        if zombie_guardada.id == id:
            del lista_zombiesDB[index]
            return {"detail": "Zombie eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Zombie no encontrado")

# Lista de zombis simulada como base de datos
lista_zombies = [
    Zombie(id="", tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, velocidad=3, nivel=1, columna=1, fila=1),
    Zombie(id="", tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, velocidad=3, nivel=1, columna=1, fila=2),
    Zombie(id="", tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, velocidad=3, nivel=2, columna=1, fila=3),
]

# Buscar zombie por ID
def buscar_zombie(id: int):
    for zombie in lista_zombies:
        if zombie.id == id:
            return zombie
    return None

# GET todos los zombis
@router.get("/zombies")
async def get_zombies():
    return lista_zombies

# GET un zombi por ID
@router.get("/zombie/{id}")
async def get_zombie(id: int):
    zombie = buscar_zombie(id)
    if not zombie:
        raise HTTPException(status_code=404, detail="Zombie no encontrado")
    return zombie

# POST - agregar un nuevo zombi
@router.post("/zombie", response_model=Zombie, status_code=201)
async def post_zombie(zombie: Zombie):
    if buscar_zombie(zombie.id):
        raise HTTPException(status_code=400, detail="ZombieDB ya existente")
    lista_zombies.append(zombie)
    return zombie

# PUT - actualizar un zombi existente
@router.put("/zombie", response_model=Zombie)
async def put_zombie(zombie: Zombie):
    for index, zombie_guardada in enumerate(lista_zombies):
        if zombie_guardada.id == zombie.id:
            lista_zombies[index] = zombie
            return zombie
    raise HTTPException(status_code=404, detail="Zombie no encontrado")

# DELETE - eliminar un zombi por ID
@router.delete("/zombie/{id}")
async def delete_zombie(id: int):
    for index, zombie_guardada in enumerate(lista_zombies):
        if zombie_guardada.id == id:
            del lista_zombies[index]
            return {"detail": "Zombie eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Zombie no encontrado")


@router.put("/zombie_a_DB")
async def put_conversion(zombiedb: ZombieDB, columna: cuadro_columna, fila: cuadro_fila):
    # Usamos model_dump() en lugar de dict() (Pydantic v2)
    zombie_colocado = Zombie(**zombiedb.model_dump(), columna=columna, fila=fila)
    
    # Buscamos y quitamos el zombie de la lista DB por id (no por objeto, ya que son distintos)
    for i, p in enumerate(lista_zombiesDB):
        if p.id == zombiedb.id:
            del lista_zombiesDB[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Zombie no creada")

    lista_zombies.append(zombie_colocado)
    return zombie_colocado


#pasar Zombie  a Zombie db
@router.put("/zombiedb_a_n")
async def put_conversion(zombie: Zombie):
    zombie_descolocado=ZombieDB(id=zombie.id, tipo=zombie.tipo, nombre=zombie.nombre, vida=zombie.vida,
                                tmp_atac=zombie.tmp_atac, danho=zombie.danho,
                                nivel=zombie.nivel, velocidad=zombie.velocidad)
    for i, p in enumerate(lista_zombies):
        if p.id == zombie.id:
            del lista_zombies[i]
            break
    else:
        raise HTTPException(status_code=404, detail="Zombie no creada")
    lista_zombiesDB.append(zombie_descolocado)
    return zombie_descolocado