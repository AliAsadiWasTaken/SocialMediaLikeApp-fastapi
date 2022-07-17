"""add_user_table

Revision ID: 88eda2adce2e
Revises: 5bf8e850f039
Create Date: 2022-07-17 14:08:03.752910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88eda2adce2e'
down_revision = '5bf8e850f039'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column("id", sa.Integer(), nullable = False)
                    , sa.Column("email", sa.String(), nullable = False)
                    , sa.Column("password", sa.String(), nullable = False)
                    , sa.Column("created_at", sa.TIMESTAMP(timezone=False), server_default=sa.text("now()"), nullable = False),
                    sa.PrimaryKeyConstraint("id"), sa.UniqueConstraint("email"))
    pass


def downgrade():
    op.drop_table("users")
    pass 
