from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from db.models import Client, ClientInfo, Room
from datetime import date

def get_all_clients(db: Session, skip, limit):
    return db.query(Client).offset(skip).limit(limit).all()

def get_client_by_id(db: Session, id):
    return db.query(Client).filter(Client.id == id).first()

def add_new_client_info(db: Session, reg, checkout: date):
    db_client_info = ClientInfo(
        registration_date=reg, checkout_date=checkout)
    
    db.add(db_client_info)
    db.commit()

    db.refresh(db_client_info)
    return db_client_info

def add_new_client(
    db: Session, name, surname: str,
    reg: date | None = None, checkout: date | None = None):
    if not (checkout is None or reg is None):
        db_client_info = add_new_client_info(db, reg, checkout)

        client = Client(
            name=name, surname=surname, info_id=db_client_info.id)

    client = Client(
        name=name, surname=surname, info_id=None)

    db.add(client)
    db.commit()

    db.refresh(client)
    return client

def delete_client_info_by_id(db: Session, id: int):
    query = delete(ClientInfo).where(ClientInfo.id == id)
    db.execute(query)
    db.commit()

def update_client_info(db: Session, id: int, reg, checkout: date):
    delete_client_info_by_id(db, id)
    db_client_info = add_new_client_info(db, reg, checkout)

    query = update(Client).filter(
            Client.id == id
    ).values(info_id = db_client_info.id)
    db.execute(query)

    updated = db.query(Client).where(Client.id == id).first()
    db.commit()

    return updated

def get_all_rooms(db: Session, skip, limit):
    return db.query(Room).offset(skip).limit(limit).all()

def get_room_by_id(db: Session, id: int):
    return db.query(Room).where(Room.id == id).first()
    
def add_new_room(db: Session, cost_per_day: int, client_ids: list[int]):
    db_room = Room(day_cost=cost_per_day)

    db.add(db_room)
    db.commit()

    db.refresh(db_room)
    query = update(Client).filter(
        Client.id.in_(client_ids)
    ).values(room_id = db_room.id)

    db.execute(query)
    db.commit()

    db.refresh(db_room)
    return db_room
    
def update_room_clients(db: Session, id: int, client_ids):
    db_room = db.query(Room).where(Room.id == id).first()
    db.refresh(db_room)

    if db_room.clients != []:
        delete_current_room_bindings = update(Client).filter(
            Client.id.in_((c.id for c in db_room.clients))
        ).values(room_id = None)
        db.execute(delete_current_room_bindings)

    
    if client_ids != []:
        add_requested_clients_to_room = update(Client).filter(
            Client.id.in_(client_ids)
        ).values(room_id = id)
        db.execute(add_requested_clients_to_room)

    db.commit()

    db.refresh(db_room)
    return db_room
    
