from datetime import date
from typing import Optional

from pydantic import BaseModel, AnyUrl


class News(BaseModel):
    title: str
    preview_url: Optional[AnyUrl]
    publish_date: date
