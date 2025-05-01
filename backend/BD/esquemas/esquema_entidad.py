#Aqui deberia de crear un esquema para la entidad
#aunque no creo que haga falta

def entidad_esquema(entidad)-> dict : #Devuelve un diccionario a modo de json borja
    return {
        "id":str(entidad["_id"]),
        "tipo" : entidad["tipo"],
        "nombre" : entidad["nombre"],
        "vida" : entidad["vida"],
        "tmp_atac" : entidad["tmp_atac"],
        "danho" : entidad["danho"],
        "nivel": entidad["nivel"]
    }

def entidades_esquema(entidades)-> list: #Devuelve una lista de json de entidades
    return [entidad_esquema(entidad) for entidad in entidades]