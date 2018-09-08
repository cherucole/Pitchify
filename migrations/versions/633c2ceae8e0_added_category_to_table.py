"""added category to table

Revision ID: 633c2ceae8e0
Revises: d135e35afdf2
Create Date: 2018-09-07 16:57:51.676168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '633c2ceae8e0'
down_revision = 'd135e35afdf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_category', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'pitch_category')
    # ### end Alembic commands ###