from fastapi import APIRouter, Depends
from fastapi_utils.tasks import repeat_every

from backend.schemas.news import News
from backend.services.news import NewsService

router = APIRouter()


@router.get("/news/day/{days}")
async def get_news(
    days: int, service: NewsService = Depends(NewsService)
) -> list[News]:
    return await service.get(days=days)
