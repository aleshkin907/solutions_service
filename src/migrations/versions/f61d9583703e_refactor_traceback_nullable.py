"""Refactor traceback nullable

Revision ID: f61d9583703e
Revises: e7d6bea961e4
Create Date: 2024-05-25 13:19:03.462060

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f61d9583703e'
down_revision: Union[str, None] = 'e7d6bea961e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('solutions', 'traceback',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('solutions', 'traceback',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
