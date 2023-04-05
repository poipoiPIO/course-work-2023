from sqlalchemy import String, Integer, ForeignKey, Column, Date
from sqlalchemy.orm import relationship

from db.setup import Base

class Campus(Base):
    __tablename__ = "campuses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)

    rooms = relationship("Room", back_populates="campus")

    def __repr__(self) -> str:
        return "<Campus: id: {}, name: {}, address: {}>".format(
            self.id, self.name, self.address
        )

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    campus_id = Column(Integer, ForeignKey("campuses.id"))

    day_cost = Column(Integer)

    campus = relationship(
        "Campus", # relative ORM class name
        back_populates="rooms" # this field in related class  
    )

    clients = relationship("Client", back_populates="room")

    def __repr__(self) -> str:
        return "<Room: id: {}, day_cost: {}>".format(
            self.id, self.day_cost
        )

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    info_id = Column(Integer, ForeignKey("client_infos.id"), nullable=True, unique=True)

    name = Column(String)
    surname = Column(String)

    room = relationship("Room", back_populates="clients")
    info = relationship("ClientInfo", backref="clients")

    def __repr__(self) -> str:
        return "<Client: id: {}, name: {}, surname: {}>".format(
            self.id, self.name, self.surname
        )

class ClientInfo(Base):
    __tablename__ = "client_infos"

    id = Column(Integer, primary_key=True, index=True)

    registration_date = Column(Date, nullable=False)
    checkout_date = Column(Date, nullable=False)

    def __repr__(self) -> str:
        return "<ClientInfo: id: {}, registered: {}, checkout: {}>".format(
            self.id, self.registration_date, self.checkout_date
        )

class AppAdmin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, nullable=False)
    hashed_passwd = Column(String, nullable=False)

    def __repr__(self) -> str:
        return "<AppAdmin: id: {}, login: {}, password hash: {}>".format(
            self.id, self.login, self.hashed_passwd
        )
