from pydantic import BaseModel

#Aqui deberia de crear la clase entidad y demas funciones necesarias
"""
class User(BaseModel):
    id: Optional[str]
    username: str
    email: str
"""
class Entidad(BaseModel):
    id:str = None #Necesito que la id sea un str
    tipo:str
    nombre:str
    vida:int
    tmp_atac:int
    danho:int 


