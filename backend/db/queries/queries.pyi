from datetime import datetime

from asyncpg import Record, Connection


class NewsMixin:
    async def get_news(self, conn: Connection, date: datetime) -> list[Record]: ...


class Queries(NewsMixin): ...


queries: Queries
