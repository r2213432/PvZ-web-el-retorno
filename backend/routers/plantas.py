from fastapi import APIRouter, HTTPException, status


from BD.cliente import cliente_pvz
from BD.modelos.planta import PlantaDB, Planta, cuadro_columna, cuadro_fila
from BD.esquemas.esquema_planta import planta_esquema, plantas_esquema, plantaBD_esquema, plantasBD_esquema
from bson import ObjectId


router = APIRouter(tags=["Plantas"])
cliente_planta = cliente_pvz.plantas

def buscar_plantadb(campo: str, clave):
    try:
        planta = cliente_planta.find_one({campo: clave})
        print(f"{planta}")
        return PlantaDB(**plantaBD_esquema(planta)) #User(**user_schema(user))
    except:
        return {"error": f"No se ha encontrado la entidad con los valores {campo} y {clave}"}

@router.get("/plantasDB")
async def get_plantas():
    return plantasBD_esquema(cliente_pvz.plantas.find()) #devuelve una lista de entidades en formato json borja

@router.get("/plantaDB/{id}") #por path
async def get_plants_id(id:str):
    return buscar_plantadb("_id", ObjectId(id))

@router.get("/plantaDB/") #por query
async def get_plants_id_query(id:str):
    return buscar_plantadb("_id", ObjectId(id))

@router.post("/plantaDB/", response_model=PlantaDB, status_code=201) #por query
async def post_planta(planta: PlantaDB):
    if type(buscar_plantadb("_id", ObjectId(planta.id))) == PlantaDB:
        raise HTTPException(status_code=404, detail=f"La planta con id {planta.id} ya existe")
    planta_dict = dict(planta)
    del planta_dict["id"] #Me aseguro que no tenga el atributo id

    id = cliente_planta.insert_one(planta_dict).inserted_id

    new_planta = plantaBD_esquema(cliente_planta.find_one({"_id":id}))
    return PlantaDB(**new_planta)


@router.put("/plantaDB/", response_model=PlantaDB)
async def put_planta(planta: PlantaDB): #Por query
    planta_dict = dict(planta)
    del planta_dict["id"]
    try:
        cliente_planta.find_one_and_replace(
            {"_id": ObjectId(planta.id)}, planta_dict)
    except:
        return {"error": "No se ha actualizado la entidad"}
    return buscar_plantadb("_id", ObjectId(planta.id))

@router.delete("/plantaDB/{id}", status_code=204)
async def delete_planta(id:str):
    encontrado = cliente_planta.find_one_and_delete({"_id": ObjectId(id)})
    if not encontrado:
        return {"error": "Planta no eliminada"}



    

#Estas seran las plantas que se crearan para el jugador
# Lista simulada de base de datos
lista_plantas = [
    Planta(id="", tipo="macaco", nombre="aitor", vida=1, tmp_atac=9, danho=2, rango=3, nivel=1, columna=1, fila=1),
    Planta(id="", tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9, danho=2, rango=3, nivel=1,columna=2, fila=3),
    Planta(id="", tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9, danho=2, rango=3, nivel=2,columna=1, fila=2),
]

# Función de búsqueda
def buscar_planta(id: str):
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

