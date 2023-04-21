import asyncpg
from asyncpg import Pool
from fastapi import FastAPI
from starlette.requests import Request

from backend.core.settings.app import AppSettings


async def connect_to_db(app: FastAPI, settings: AppSettings) -> None:
    app.state.pool = await asyncpg.create_pool(
        str(settings.database_url),
        max_size=50,
    )


async def close_db_connection(app: FastAPI) -> None:
    await app.state.pool.close()


def get_db_pool(request: Request) -> Pool:
    return request.app.state.pool
