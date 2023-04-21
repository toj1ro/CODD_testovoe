from datetime import timedelta, datetime

from fastapi import Depends

from backend.core.errors import NotFoundObject
from backend.repositories.news import NewsRepository


class NewsService:
    def __init__(
            self,
            metro_repo: NewsRepository = Depends(
                NewsRepository
            )
    ):
        self.metro_repo = metro_repo

    async def get(self, days):
        date = datetime.today() - timedelta(days=days)
        news = await self.metro_repo.get(date=date)
        if not news:
            raise NotFoundObject("News not found")
        return news
