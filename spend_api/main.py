import pydevd_pycharm
from fastapi import FastAPI

from spend_api.api.router import root_router
from spend_api.core.config import inject_settings


def init_app() -> FastAPI:
    settings = inject_settings()

    if settings.DEBUG:
        pydevd_pycharm.settrace('host.minikube.internal',
                                port=5555,
                                stdoutToServer=True,
                                stderrToServer=True)

    app = FastAPI(
        title=settings.PROJECT_NAME
    )
    app.include_router(root_router)
    return app
