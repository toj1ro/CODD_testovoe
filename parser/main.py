from parser.services.service import parse_news_from_mosday_metro, insert_data_to_news


def parser():
    data = parse_news_from_mosday_metro()
    insert_data_to_news(data)
