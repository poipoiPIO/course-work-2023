from pydantic import BaseModel
from datetime import date
from typing import Optional, Any

class DBItemBase(BaseModel):
    id: Optional[int]

    class Config:
        orm_mode = True

class ClientInfo(DBItemBase):
    registration_date: date
    checkout_date: date
    
class Client(DBItemBase):
    name: str
    surname: str
    info: ClientInfo | None

class ClientInfoUpdate(DBItemBase):
    info: ClientInfo
    
class RoomForDB(DBItemBase):
    day_cost: int
    client_ids: list[int] | list[Any]

class Room(DBItemBase):
    day_cost: int
    clients: list[Client]

class Campus(DBItemBase):
    name: str
    address: str
    rooms: list[Room]
