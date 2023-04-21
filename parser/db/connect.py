from typing import Any

import psycopg2


class Database:
    def __init__(self, host, database, user, password, port):
        self.__conn = psycopg2.connect(host=host,
                                       database=database,
                                       user=user,
                                       port=port,
                                       password=password)
        self.__cur = self.__conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cur.close()

    def execute_many(self, query: str, data: list[Any]):
        self.__cur.executemany(query, data)
        self.__conn.commit()
