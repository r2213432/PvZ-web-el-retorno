def zombie_esquema(zombie) -> dict:
    return {
        "id":str(zombie["_id"]),
        "tipo" : zombie["tipo"],
        "nombre" : zombie["nombre"],
        "vida" : zombie["vida"],
        "tmp_atac" : zombie["tmp_atac"],
        "danho" : zombie["danho"],
        "nivel" : zombie["nivel"],
        "velocidad":zombie["velocidad"],
        "columna" : zombie["columna"],
        "fila" : zombie["fila"]
    }
def zombies_esquema(zombies) -> list:
    return [zombie_esquema(zombie) for zombie in zombies]