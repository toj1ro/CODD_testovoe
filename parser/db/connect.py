from typing import Any, Optional

import psycopg2


class Database:
    def __init__(
        self,
        host: Optional[str],
        database: Optional[str],
        user: Optional[str],
        password: Optional[str],
        port: Optional[str],
    ) -> None:
        self.__conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            port=port,
            password=password,
        )
        self.__cur = self.__conn.cursor()

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # type: ignore
        self.__cur.close()

    def execute_many(self, query: str, data: list[Any]) -> None:
        self.__cur.executemany(query, data)
        self.__conn.commit()
