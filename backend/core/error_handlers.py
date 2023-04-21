from typing import Union

from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from backend.core.errors import NotFoundObject


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"message": exc.detail}, status_code=exc.status_code)


async def http400_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    return JSONResponse(
        {"message": exc.errors()},
        status_code=HTTP_400_BAD_REQUEST,
    )


async def http404_error_handler(
        _: Request,
        exc: Union[NotFoundObject],
) -> JSONResponse:
    return JSONResponse(
        {"message": str(exc)},
        status_code=HTTP_404_NOT_FOUND,
    )
