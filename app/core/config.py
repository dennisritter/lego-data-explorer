# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_name: str
    database_username: str
    database_password: str
    echo_sql: bool = True
    test: bool = False
    project_name: str = "Lego Data Explorer"

    class Config:
        env_file = ".env"


settings = Settings()
