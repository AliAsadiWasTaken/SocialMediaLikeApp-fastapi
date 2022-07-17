"""add content column to posts table

Revision ID: 5bf8e850f039
Revises: 0bcd971c7b37
Create Date: 2022-07-17 13:24:23.542392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bf8e850f039'
down_revision = '0bcd971c7b37'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
