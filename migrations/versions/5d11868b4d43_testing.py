"""testing

Revision ID: 5d11868b4d43
Revises: 0148ab274a3e
Create Date: 2023-10-06 15:19:34.162786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d11868b4d43'
down_revision: Union[str, None] = '0148ab274a3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('test', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'todos', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='unique')
    op.drop_column('todos', 'test')
    # ### end Alembic commands ###