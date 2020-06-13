"""empty message

Revision ID: 00e85017bf2c
Revises: 
Create Date: 2020-06-13 17:58:42.049840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00e85017bf2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('movie_snapshot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('director', sa.String(length=250), nullable=True),
    sa.Column('release_date', sa.Date(), nullable=True),
    sa.Column('release_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_snapshot_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=20), nullable=True),
    sa.Column('source', sa.String(length=250), nullable=True),
    sa.Column('movie_snapshot_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_snapshot_id'], ['movie_snapshot.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('movie_snapshot_rating')
    op.drop_table('movie_snapshot')
