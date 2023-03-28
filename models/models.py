from pydantic import BaseModel
from datetime import date

class DBItemBase(BaseModel):
    id: int

    class Config:
        orm_mode = True

class ClientInfo(DBItemBase):
    registration_date: date
    checkout_date: date
    
class Client(DBItemBase):
    name: str
    surname: str
    info: ClientInfo
    
class Room(DBItemBase):
    day_cost: int
    clients: list[Client]

class Campus(DBItemBase):
    name: str
    address: str
    rooms: list[Room]
