from sqlalchemy.orm import Session
from db.models import Client

def get_all_clients(db: Session, skip, limit):
    return db.query(Client).offset(skip).limit(limit).all()

def get_client_by_id(db: Session, id):
    return db.query(Client).filter(Client.id == id).first()
