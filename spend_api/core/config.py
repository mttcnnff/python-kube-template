import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str

    class Config:
        case_sensitive = True


def inject_settings() -> Settings:
    return Settings(_env_file=f"./{os.environ['APP_ENV']}.env")
