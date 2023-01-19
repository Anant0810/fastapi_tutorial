"""add foriegn key to posts table

Revision ID: d731969f548b
Revises: a633dbcad9f2
Create Date: 2023-01-19 20:51:49.846598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd731969f548b'
down_revision = 'a633dbcad9f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk",source_table='posts', referent_table="users", local_cols=['owner_id'], remote_cols=['id'],
                         ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')

