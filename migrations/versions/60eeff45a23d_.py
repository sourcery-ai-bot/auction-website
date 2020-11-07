"""empty message

Revision ID: 60eeff45a23d
Revises: 036bc17fc4a6
Create Date: 2020-10-17 06:09:01.791976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60eeff45a23d'
down_revision = '036bc17fc4a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('starting_bid', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'starting_bid')
    # ### end Alembic commands ###