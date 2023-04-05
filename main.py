#! env/bin/python3

from fastapi import FastAPI
from sqladmin import Admin

import uvicorn

from settings import settings
from db.setup import db_engine
from admin.models import CampusAdmin, RoomAdmin, ClientAdmin, ClientInfoAdmin 
from admin.auth import AdminAuth 
from router import router

app = FastAPI()
admin = Admin(app, db_engine, authentication_backend=AdminAuth(
    secret_key=settings.admin_passwd))

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(router)

# __ Admin Views __
admin.add_view(CampusAdmin)
admin.add_view(RoomAdmin)
admin.add_view(ClientAdmin)
admin.add_view(ClientInfoAdmin)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=settings.serve_port)
