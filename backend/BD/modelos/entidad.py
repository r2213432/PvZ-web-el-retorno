from pydantic import BaseModel
from enum import Enum

class cuadro_columna(int, Enum):
    COLUMNA1 = 1
    COLUMNA2 = 2
    COLUMNA3 = 3
    COLUMNA4 = 4
    COLUMNA5 = 5
    COLUMNA6 = 6
    COLUMNA7 = 7
    COLUMNA8 = 8
    COLUMNA9 = 9

class cuadro_fila(int, Enum):
    FILA1 = 1
    FILA2 = 2
    FILA3 = 3
    FILA4 = 4
    FILA5 = 5

class Entidad(BaseModel):
    id: int 
    tipo: str
    nombre: str
    vida: int
    tmp_atac: int
    danho: int
    nivel: int