from parser import main as parser

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_utils.tasks import repeat_every
from starlette.exceptions import HTTPException

from backend.core.config import get_app_settings
from backend.core.error_handlers import (
    http400_error_handler,
    http404_error_handler,
    http_error_handler,
)
from backend.core.errors import NotFoundObject
from backend.core.events import (
    create_start_app_handler,
    create_stop_app_handler,
)
from backend.routes.api import router

settings = get_app_settings()


def get_application() -> FastAPI:
    application = FastAPI(title=settings.project_name)
    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(
        RequestValidationError, http400_error_handler
    )
    application.add_exception_handler(NotFoundObject, http404_error_handler)
    application.include_router(router)
    return application


app = get_application()


@app.on_event("startup")
@repeat_every(seconds=60 * 10)
def parse() -> None:
    parser.parser()
