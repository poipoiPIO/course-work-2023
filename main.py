from fastapi import FastAPI
from sqladmin import Admin

import uvicorn

from settings import settings
from db.setup import db_engine, Base
from admin import CampusAdmin, RoomAdmin, ClientAdmin, ClientInfoAdmin 

app = FastAPI()
admin = Admin(app, db_engine)

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

# app.include_router(_) # TODO : ADD ROUTER

# __ Admin Views __
admin.add_view(CampusAdmin)
admin.add_view(RoomAdmin)
admin.add_view(ClientAdmin)
admin.add_view(ClientInfoAdmin)

if __name__ == "__main__":
    Base.metadata.create_all(db_engine) # create tables
    uvicorn.run(app, host="localhost", port=settings.serve_port)
