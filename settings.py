from pydantic import BaseSettings

class Settings(BaseSettings):
    db_url: str
    serve_port: int

settings = Settings(
    db_url="sqlite:///db.sqlite",
    serve_port=8000
)
