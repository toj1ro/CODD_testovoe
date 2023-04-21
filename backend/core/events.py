import asyncio
from typing import Callable

from fastapi import FastAPI

from backend.core.settings.app import AppSettings
from backend.db.db_utils import close_db_connection, connect_to_db


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:  # type: ignore
    async def start_app() -> None:
        await asyncio.gather(connect_to_db(app, settings))

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
