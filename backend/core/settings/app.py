from typing import Any, Optional

from pydantic import BaseSettings, validator


class AppSettings(BaseSettings):
    project_name: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str
    database_url: Optional[str]

    class Config:
        env_file = ".env"

    @validator("database_url")
    def set_database_url(cls, _: Any, values: Any) -> Any:
        if values.get("postgres_host") == "db":
            values["postgres_port"] = "5432"
        return (
            f"postgresql://{values.get('postgres_user')}:"
            f"{values.get('postgres_password')}@"
            f"{values.get('postgres_host')}"
            f":{values.get('postgres_port')}/{values.get('postgres_db')}"
        )
