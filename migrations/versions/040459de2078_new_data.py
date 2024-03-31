"""new data

Revision ID: 040459de2078
Revises: 1bf2213f38c5
Create Date: 2024-03-31 12:12:08.734947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '040459de2078'
down_revision: Union[str, None] = '1bf2213f38c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
