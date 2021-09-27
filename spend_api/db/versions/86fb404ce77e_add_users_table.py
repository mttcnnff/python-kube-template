"""add users table

Revision ID: 86fb404ce77e
Revises: 
Create Date: 2021-09-26 18:14:51.049837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86fb404ce77e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
