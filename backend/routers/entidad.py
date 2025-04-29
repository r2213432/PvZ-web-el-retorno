from fastapi import APIRouter, HTTPException, status
from backend.BD.cliente import cliente_pvz
from backend.BD.modelos.entidad import Entidad
from backend.BD.esquemas.esquema_entidad import entidad_esquema, entidades_esquema
from bson import ObjectId

router=APIRouter(prefix="/entidad", tags=["Entidad"])
cliente_entidad = cliente_pvz.entidades


def buscar_entidad(campo: str, clave):
    try:
        entidad = cliente_entidad.find_one({campo: clave})
        return Entidad(**entidad_esquema(entidad)) #User(**user_schema(user))
    except:
        return {"error": f"No se ha encontrado la entidad con los valores {campo} y {clave}"}
@router.get("/")
async def get_entidades():
    return entidades_esquema(cliente_pvz.entidades.find()) #devuelve una lista de entidades en formato json borja

@router.get("/{id}") #por path
async def get_entidad_id(id:str):
    return buscar_entidad("_id", ObjectId(id))

@router.get("/") #por query
async def get_entidad_id_query(id:str):
    return buscar_entidad("_id", ObjectId(id))

@router.post("/", response_model=Entidad, status_code=201) #por query
async def post_entidad(entidad: Entidad):
    if type(buscar_entidad("_id", ObjectId(entidad.id))) == Entidad:
        raise HTTPException(status_code=404, detail=f"La entidad con id {entidad.id} ya existe")
    entidad_dict = dict(entidad)
    del entidad_dict["id"] #Me aseguro que no tenga el atributo id

    id = cliente_entidad.insert_one(entidad_dict).inserted_id

    new_entidad = entidad_esquema(cliente_entidad.find_one({"_id":id}))
    return Entidad(**new_entidad)


@router.put("/", response_model=Entidad)
async def put_entidad(entidad: Entidad): #Por query
    entidad_dict = dict(entidad)
    del entidad_dict["id"]
    try:
        cliente_entidad.find_one_and_replace(
            {"_id": ObjectId(entidad.id)}, entidad_dict)
    except:
        return {"error": "No se ha actualizado la entidad"}
    return buscar_entidad("_id", ObjectId(entidad.id))

@router.delete("/{id}", status_code=204)
async def delete_entidad(id:str):
    encontrado = cliente_entidad.find_one_and_delete({"_id": ObjectId(id)})
    if not encontrado:
        return {"error": "Entidad no eliminada"}


