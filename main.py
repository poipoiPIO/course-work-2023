#! env/bin/python3

from fastapi import FastAPI
from sqladmin import Admin

import uvicorn

from settings import settings
from db.setup import db_engine
from admin import models as m, auth as a 
from router import router

app = FastAPI()
admin = Admin(app, db_engine, authentication_backend=a.AdminAuth(
    secret_key=settings.admin_passwd))

@app.on_event("startup")
async def startup():
    pass

@app.on_event("shutdown")
async def shutdown():
    pass

app.include_router(router)

# __ Admin Views __
admin.add_view(m.CampusAdmin)
admin.add_view(m.RoomAdmin)
admin.add_view(m.ClientAdmin)
admin.add_view(m.ClientInfoAdmin)
admin.add_view(m.AppAdminAdmin)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=settings.serve_port)
