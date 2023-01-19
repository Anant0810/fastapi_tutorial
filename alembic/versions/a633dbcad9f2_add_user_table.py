"""add user table

Revision ID: a633dbcad9f2
Revises: 51105ef3ccb9
Create Date: 2023-01-19 20:41:23.068705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a633dbcad9f2'
down_revision = '51105ef3ccb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
                    sa.Column("email", sa.String(), nullable=False, unique=True), 
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default = sa.text("now()"), nullable=False))


def downgrade() -> None:
    op.drop_table('users')
