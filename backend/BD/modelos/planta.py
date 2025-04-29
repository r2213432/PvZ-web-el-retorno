from backend.BD.modelos.entidad import Entidad, cuadro_fila, cuadro_columna

class PlantaDB(Entidad):
    rango: int

class Planta(PlantaDB):
    esta_plantado: bool
    columna: cuadro_columna
    fila: cuadro_fila