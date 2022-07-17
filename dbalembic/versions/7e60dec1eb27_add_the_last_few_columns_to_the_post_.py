"""add the last few columns to the post table

Revision ID: 7e60dec1eb27
Revises: 09ae7ba7d02b
Create Date: 2022-07-17 17:15:23.735420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e60dec1eb27'
down_revision = '09ae7ba7d02b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text("NOW()")))
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable = False, server_default = "True"))
    pass


def downgrade():
    op.drop_column("posts", "content")
    op.drop_column("posts", "published")
    pass
