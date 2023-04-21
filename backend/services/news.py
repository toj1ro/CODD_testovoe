from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends

from backend.core.errors import NotFoundObject
from backend.repositories.news import NewsRepository
from backend.schemas.news import News


class NewsService:
    def __init__(self, metro_repo: NewsRepository = Depends(NewsRepository)):
        self.metro_repo = metro_repo

    async def get(self, days: int) -> list[News]:
        date = datetime.today() - timedelta(days=days)
        news = await self.metro_repo.get(date=date)
        if not news:
            raise NotFoundObject("News not found")
        return news
