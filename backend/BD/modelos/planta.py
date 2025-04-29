from enum import Enum
from entidad import Entidad
class cuadro_columna(Enum):
    COLUMNA1=1
    COLUMNA2=2
    COLUMNA3=3
    COLUMNA4=4
    COLUMNA5=5
    COLUMNA6=6
    COLUMNA7=7
    COLUMNA8=8
    COLUMNA9=9
    
#Estan alreves XD
class cuadro_fila(Enum):
    FILA1=1
    FILA2=2
    FILA3=3
    FILA4=4
    FILA5=5
    
class PlantaDB(Entidad):
    rango:int
    nivel:int
# 5x9
class Planta(PlantaDB):
    esta_plantado:bool
    columna:cuadro_columna
    fila:cuadro_fila

