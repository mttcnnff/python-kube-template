import os
from typing import Optional, Dict, Any

from pydantic import BaseSettings, validator, PostgresDsn


class Settings(BaseSettings):
    PROJECT_NAME: str
    DEBUG: bool = False

    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_NAME: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASS"),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )

    class Config:
        case_sensitive = True


def inject_settings() -> Settings:
    return Settings(_env_file=f"./spend_api/{os.environ['APP_ENV']}.env")

