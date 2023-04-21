FROM python:3.10.10-slim as base

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app



RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/timezone && \
     ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime

COPY poetry.lock pyproject.toml ./

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --only main

COPY . ./


FROM base as build
CMD poetry run uvicorn --host=0.0.0.0 backend.main:app


FROM base as build_with_migrations
CMD poetry run alembic upgrade head && \
    poetry run uvicorn --host=0.0.0.0 backend.main:app