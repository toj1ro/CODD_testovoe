"""init_database

Revision ID: 86cadd165924
Revises:
Create Date: 2023-04-21 02:02:23.417135

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "86cadd165924"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """create table if not exists news
(
    id           serial
        constraint news_pk
            primary key,
    preview_url  varchar,
    title        varchar,
    publish_date date
);"""
    )


def downgrade() -> None:
    op.execute("drop table if exists news;")
