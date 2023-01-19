"""create post table

Revision ID: 587ad3a82995
Revises: 
Create Date: 2023-01-19 20:29:25.050809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '587ad3a82995'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
            sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
