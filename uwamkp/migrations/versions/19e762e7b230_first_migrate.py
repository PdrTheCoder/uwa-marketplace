"""first migrate

Revision ID: 19e762e7b230
Revises: 4494ece58d4b
Create Date: 2024-05-03 22:50:57.448697

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '19e762e7b230'
down_revision = '4494ece58d4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('category_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('desc', sa.TEXT(), nullable=False),
    sa.Column('created_at', sqlite.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category_name')
    )
    op.create_table('listing',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=60), nullable=False),
    sa.Column('condition', sa.SMALLINT(), nullable=False),
    sa.Column('price', sa.DECIMAL(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.Column('suspended', sa.BOOLEAN(), nullable=False),
    sa.Column('sold', sa.BOOLEAN(), nullable=False),
    sa.Column('deleted', sa.BOOLEAN(), nullable=False),
    sa.Column('created_at', sqlite.DATETIME(), nullable=False),
    sa.Column('updated_at', sqlite.DATETIME(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reply',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('message', sa.TEXT(), nullable=False),
    sa.Column('from_user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sqlite.DATETIME(), nullable=False),
    sa.Column('listing_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['from_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['listing_id'], ['listing.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reply')
    op.drop_table('listing')
    op.drop_table('category')
    # ### end Alembic commands ###