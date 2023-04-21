import datetime
import re
from parser.db.connect import Database
from parser.settings import (
    postgres_database,
    postgres_host,
    postgres_password,
    postgres_port,
    postgres_user,
)
from typing import Any
from urllib.request import urlopen

from bs4 import BeautifulSoup


def parse_news_from_mosday_metro() -> list[Any]:
    data = []
    html = get_web_page("https://mosday.ru/news/tags.php?metro")
    soup = BeautifulSoup(html, "lxml")
    for child_link in soup.find_all(
        "a", href=lambda x: x and "tags=metro" in x
    ):
        news_block = child_link.parent.parent.parent
        title = child_link.b.text
        publish_date = datetime.datetime.strptime(
            news_block.font.b.text, "%d.%m.%Y"
        )
        preview_url = (
            None
            if not news_block.parent.img
            else "https://mosday.ru/news/" + news_block.parent.img["src"]
        )
        news_id = int(re.search("\d{7}", child_link["href"]).group())  # type: ignore
        data.append((news_id, title, str(publish_date), preview_url))
    return data


def get_web_page(url: str) -> Any:
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("windows-1251")
    return html


def insert_data_to_news_table(data: list[Any]) -> None:
    with Database(
        host=postgres_host,
        database=postgres_database,
        user=postgres_user,
        port=postgres_port,
        password=postgres_password,
    ) as conn:
        conn.execute_many(
            "INSERT INTO news (id, title, publish_date, preview_url) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO UPDATE SET (title, publish_date, preview_url) = (EXCLUDED.title, EXCLUDED.publish_date, EXCLUDED.preview_url);",
            data,
        )
