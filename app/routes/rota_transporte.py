from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import obter_horarios

transporte_router = APIRouter()

@transporte_router.get("/transporte/publico")
def obter_horarios_050(db: Session = Depends(get_db)):
    return obter_horarios(db, "municipal")

@transporte_router.get("/transporte/intercampi")
def obter_horarios_intercampi(db: Session = Depends(get_db)):
    return obter_horarios(db, "intercampi")