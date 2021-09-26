import pydevd_pycharm
from fastapi import FastAPI
from sqlalchemy import create_engine

from spend_api.api.router import root_router
from spend_api.core.config import inject_settings


def init_app() -> FastAPI:
    settings = inject_settings()

    if settings.DEBUG:
        pydevd_pycharm.settrace('host.minikube.internal',
                                port=5555,
                                stdoutToServer=True,
                                stderrToServer=True)

    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

    app = FastAPI(
        title=settings.PROJECT_NAME
    )
    app.include_router(root_router)
    return app
