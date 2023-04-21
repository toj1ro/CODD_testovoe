import os

from dotenv import load_dotenv

load_dotenv()

postgres_host = os.getenv("POSTGRES_HOST")
postgres_database = os.getenv("POSTGRES_DB")
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_port = os.getenv("POSTGRES_PORT")
