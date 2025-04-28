from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router=APIRouter()

class Entidad(BaseModel):
    id:int
    tipo:str
    nombre:str
    vida:int
    tmp_atac:int
    danho:int



