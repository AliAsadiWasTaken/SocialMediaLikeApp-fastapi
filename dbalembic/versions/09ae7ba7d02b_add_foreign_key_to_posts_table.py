"""add_foreign_key_to_posts_table

Revision ID: 09ae7ba7d02b
Revises: 88eda2adce2e
Create Date: 2022-07-17 17:06:42.724395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09ae7ba7d02b'
down_revision = '88eda2adce2e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable = False))
    op.create_foreign_key("post_users_fk", source_table = "posts", referent_table= "users", local_cols = ["owner_id"], remote_cols = ["id"], ondelete = "CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name = "posts")
    op.drop_column("posts", "owner_id")
    pass
