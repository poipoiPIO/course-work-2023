from sqladmin.authentication import AuthenticationBackend
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from hashlib import sha256

from db.models import AppAdmin
from db.setup import session

def hash(string: str) -> str:
    m = sha256()
    m.update(string.encode())
    return m.hexdigest()

def auth(db: Session, hashed_pass, login: str) -> bool:
    query = db.query(AppAdmin).where(
        AppAdmin.login == login and
        AppAdmin.hash_passwd == hashed_pass
    ).first()

    return bool(query)

class AdminAuth(AuthenticationBackend):
    async def login(self, request):
        form = await request.form()
        uname, passwd = form["username"], form["password"]

        if type(passwd) == str and type(uname) == str:
            hashed_pass = hash(passwd)

            if auth(session(), hashed_pass, uname):
                # TODO : Unsecure thingy
                request.session.update({"token": hashed_pass})
                return True
        return False

    async def logout(self, request):
        request.session.clear()
        return True

    async def authenticate(self, request):
        token = request.session.get("token")

        if not token:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)
