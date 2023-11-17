"""'Init'

Revision ID: fd553fbde050
Revises: 
Create Date: 2023-11-06 01:18:11.333476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd553fbde050'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('phone_number', sa.ARRAY(sa.Integer()), nullable=False),
    sa.Column('additional_data', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts')
    # ### end Alembic commands ###