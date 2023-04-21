from asyncpg import Pool
from fastapi import Depends

from backend.db.db_utils import get_db_pool
from backend.db.queries.queries import queries
from backend.schemas.news import News


class NewsRepository:
    def __init__(self, pool: Pool = Depends(get_db_pool)) -> None:
        self.pool = pool

    async def get(self, date):
        async with self.pool.acquire() as conn:
            news = await queries.get_news(conn=conn, date=date)
        if not news:
            return None
        return [News(**n) for n in news]
