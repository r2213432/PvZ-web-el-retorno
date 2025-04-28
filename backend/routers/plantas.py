from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from routers import entidad
from enum import Enum

router=APIRouter()

class cuadro_columna(Enum):
    COLUMNA1=1
    COLUMNA2=2
    COLUMNA3=3
    COLUMNA4=4
    COLUMNA5=5

class cuadro_fila(Enum):
    FILA1=1
    FILA2=1
    FILA3=1
    FILA4=1
    FILA5=1
    FILA6=1
    FILA7=1
    FILA8=1
    FILA9=1
    
class PlantaDB(entidad.Entidad):
    rango:int
    nivel:int
# 5x9
class Planta(PlantaDB):
    esta_plantado:bool
    columna:cuadro_columna
    fila:cuadro_fila

lista_usuarios=[       PlantaDB(id=1, tipo="macaco", nombre="aitor", vida=1, tmp_atac=9,
                       danho=2, rango=3, nivel=1),
                       PlantaDB(id=2, tipo="macaco2", nombre="aitor2", vida=2, tmp_atac=9,
                       danho=2, rango=3, nivel=1),
                       PlantaDB(id=3, tipo="macaco3", nombre="aitor3", vida=1, tmp_atac=9,
                       danho=2, rango=3, nivel=2),]

@router.get("/plantasDB")
async def get_plantasDB():
    return lista_usuarios



    