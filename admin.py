from sqladmin import ModelView

from db.models import *

class FullAdminBase(ModelView):
    can_create = True
    can_edit = True
    can_delete = True

class CampusAdmin(FullAdminBase, model=Campus):
    pass

class RoomAdmin(FullAdminBase, model=Room):
    pass

class ClientAdmin(FullAdminBase, model=Client):
    pass

class ClientInfoAdmin(FullAdminBase, model=ClientInfo):
    pass
