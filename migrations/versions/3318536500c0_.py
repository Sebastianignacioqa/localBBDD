"""empty message

Revision ID: 3318536500c0
Revises: 2e98c9b61a72
Create Date: 2021-10-03 18:50:12.779388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3318536500c0'
down_revision = '2e98c9b61a72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seller', sa.String(length=50), nullable=False),
    sa.Column('buyer', sa.String(length=50), nullable=False),
    sa.Column('amount', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    # ### end Alembic commands ###
