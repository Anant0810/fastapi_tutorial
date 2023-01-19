"""add content column to post table

Revision ID: 51105ef3ccb9
Revises: 587ad3a82995
Create Date: 2023-01-19 20:37:04.701302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51105ef3ccb9'
down_revision = '587ad3a82995'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
