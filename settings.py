from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    admin_passwd: str
    serve_port: int

settings = Settings(
    db_url="sqlite:///db.sqlite",
    admin_passwd="password",
    serve_port=8000
)
