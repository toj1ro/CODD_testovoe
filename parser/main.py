from parser.services.service import (
    insert_data_to_news_table,
    parse_news_from_mosday_metro,
)


def parser() -> None:
    data = parse_news_from_mosday_metro()
    insert_data_to_news_table(data)
