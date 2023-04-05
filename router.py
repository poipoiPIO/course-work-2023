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
        message = "Client with id: {}, not found".format(id)
        raise HTTPException(status_code=404, detail=message)
    return query

@router.get("/clients", response_model=list[models.Client])
async def get_all_clients(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = crud.get_all_clients(db, skip, limit)
    return query

@router.post("/clients", response_model=models.Client)
async def add_client(
    client: models.Client, db: Session = Depends(get_db)):
    
    if client.info is not None:
        query = crud.add_new_client(
            db, client.name, client.surname,
            client.info.registration_date, client.info.checkout_date)

    query = crud.add_new_client(
        db, client.name, client.surname)

    return query

@router.put("/clients/info", response_model=models.Client)
async def update_client_info(
        client: models.ClientInfoUpdate , db: Session = Depends(get_db)):

    if client.id is None:
        message = "Please provide 'id' for client to update info!"
        raise HTTPException(status_code=400, detail=message)

    query = crud.update_client_info(
        db, client.id,
        client.info.registration_date,
        client.info.checkout_date
    )

    if query is None:
        message = "Client with id: {}, not found".format(id)
        raise HTTPException(status_code=404, detail=message)

    return query

@router.post("/rooms", response_model=models.Room)
async def add_new_room(
    room: models.RoomForDB, db: Session = Depends(get_db)):
    query = crud.add_new_room(
        db, room.day_cost, room.client_ids)

    return query

@router.get("/rooms", response_model=list[models.Room])
async def get_all_rooms(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    query = crud.get_all_rooms(db, skip, limit)

    return query

@router.get("/rooms/{id}", response_model=models.Room)
async def get_room_by_id(id: int, db: Session = Depends(get_db)):
    query = crud.get_room_by_id(db, id)

    if query is None:
        message = "Room with id: {}, not found".format(id)
        raise HTTPException(status_code=404, detail=message)
    return query

@router.put("/rooms", response_model=models.Room)
async def update_room_clients(
    room: models.RoomForDB, db: Session = Depends(get_db)):

    if room.id is None:
        message = "Id is not provided, cannot update the room"
        raise HTTPException(status_code=400, detail=message)

    query = crud.update_room_clients(db, room.id, room.client_ids)

    if query is None:
        message = "Room with id: {}, not found".format(id)
        raise HTTPException(status_code=404, detail=message)

    return query
