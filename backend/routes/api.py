from fastapi import APIRouter

from backend.routes import news

router = APIRouter()

router.include_router(news.router, tags=["Metro news"], prefix="/metro")
