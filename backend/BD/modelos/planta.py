from backend.BD.modelos.entidad import Entidad, cuadro_fila, cuadro_columna

class PlantaDB(Entidad):
        rango: int

class Planta(PlantaDB):
    columna: cuadro_columna
    fila: cuadro_fila