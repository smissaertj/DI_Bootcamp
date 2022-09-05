"""empty message

Revision ID: bc9e872b580a
Revises: 
Create Date: 2022-08-24 20:28:47.221820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc9e872b580a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('race', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('human',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dogs',
    sa.Column('human_id', sa.Integer(), nullable=True),
    sa.Column('dog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['dog_id'], ['dog.id'], ),
    sa.ForeignKeyConstraint(['human_id'], ['human.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    op.drop_table('human')
    op.drop_table('dog')
    # ### end Alembic commands ###