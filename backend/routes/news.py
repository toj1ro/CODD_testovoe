from fastapi import APIRouter, Depends
from fastapi_utils.tasks import repeat_every

from backend.services.news import NewsService

router = APIRouter()


@router.get('/news/day/{days}')
async def get_news(days: int, service: NewsService = Depends(NewsService)):
    return await service.get(days=days)
