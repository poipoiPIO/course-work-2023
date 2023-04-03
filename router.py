from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.setup import session
from models import models

import crud

router = APIRouter()

def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()

@router.get("/clients/{id}", response_model=models.Client)
async def get_client_by_id(id: int, db: Session = Depends(get_db)):
    query = crud.get_client_by_id(db, id)

    if query is None:
        message = "User with id: {}, not found".format(id)
        raise HTTPException(status_code=404, detail=message)
    return query

@router.get("/clients", response_model=list[models.Client])
async def get_all_clients(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = crud.get_all_clients(db, skip, limit)
    return query
