from sqladmin import ModelView

from db import models

class FullAdminBase(ModelView):
    can_create = True
    can_edit = True
    can_delete = True

class CampusAdmin(FullAdminBase, model=models.Campus):
    pass

class RoomAdmin(FullAdminBase, model=models.Room):
    pass

class ClientAdmin(FullAdminBase, model=models.Client):
    pass

class ClientInfoAdmin(FullAdminBase, model=models.ClientInfo):
    pass

class AppAdminAdmin(FullAdminBase, model=models.AppAdmin):
    pass
