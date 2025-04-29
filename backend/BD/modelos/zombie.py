from backend.BD.modelos.entidad import Entidad, cuadro_columna, cuadro_fila

class ZombieDB(Entidad):
    velocidad: int

class Zombie(ZombieDB):
    columna: cuadro_columna
    fila: cuadro_fila