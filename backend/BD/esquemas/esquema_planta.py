"""
def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"]}


def users_schema(users) -> list:
    return [user_schema(user) for user in users]
"""

def planta_esquema(planta) -> dict:
    return {
        "id":str(planta["_id"]),
        "tipo" : planta["tipo"],
        "nombre" : planta["nombre"],
        "vida" : planta["vida"],
        "tmp_atac" : planta["tmp_atac"],
        "danho" : planta["danho"],
        "rango" : planta["rango"],
        "nivel" : planta["nivel"],
        "esta_plantado":planta["esta_plantado"],
        "columna" : planta["columna"],
        "fila" : planta["fila"]
    }
def plantas_esquema(plantas) -> list:
    return [planta_esquema(planta) for planta in plantas]