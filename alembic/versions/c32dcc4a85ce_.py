"""empty message

Revision ID: c32dcc4a85ce
Revises: ce8389dd0a0e
Create Date: 2019-06-23 13:03:11.440740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c32dcc4a85ce'
down_revision = 'ce8389dd0a0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'cart', ['id'])
    op.create_unique_constraint(None, 'item', ['id'])
    op.create_unique_constraint(None, 'purchase', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'purchase', type_='unique')
    op.drop_constraint(None, 'item', type_='unique')
    op.drop_constraint(None, 'cart', type_='unique')
    # ### end Alembic commands ###
