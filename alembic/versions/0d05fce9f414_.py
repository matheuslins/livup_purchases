"""empty message

Revision ID: 0d05fce9f414
Revises: 
Create Date: 2019-06-23 17:31:41.026894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d05fce9f414'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.String(length=30), nullable=False),
    sa.Column('user', sa.String(length=30), nullable=False),
    sa.Column('distribution_center_id', sa.String(length=30), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('delivery_status', sa.String(length=30), nullable=False),
    sa.Column('payment_status', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.String(length=30), nullable=False),
    sa.Column('status', sa.String(length=30), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.Column('subtotal', sa.Float(), nullable=False),
    sa.Column('delivery', sa.Float(), nullable=False),
    sa.Column('delivery_cost', sa.Float(), nullable=False),
    sa.Column('kind', sa.String(length=30), nullable=False),
    sa.Column('distribution_center', sa.String(length=30), nullable=False),
    sa.Column('purchase_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchase.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('_id', sa.String(length=30), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('kind', sa.String(length=30), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('unit', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    op.drop_table('cart')
    op.drop_table('purchase')
    # ### end Alembic commands ###