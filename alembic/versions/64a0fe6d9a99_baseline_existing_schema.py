"""baseline existing schema

Revision ID: 64a0fe6d9a99
Revises: 
Create Date: 2026-11-19 22:08:05.049033

"""
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = '64a0fe6d9a99'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
