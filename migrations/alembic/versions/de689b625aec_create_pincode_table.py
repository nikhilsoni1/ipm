"""Create pincode table

Revision ID: de689b625aec
Revises: 
Create Date: 2022-05-19 12:38:30.080046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2fc50c1510fc"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "pincode",
        sa.Column("officename", sa.VARCHAR, nullable=False, primary_key=True),  # PK
        sa.Column("pincode", sa.INTEGER, nullable=False, primary_key=True),  # PK
        sa.Column("officetype", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("deliverystatus", sa.VARCHAR, nullable=False, primary_key=True),  # PK
        sa.Column("divisionname", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("regionname", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("circlename", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("taluk", sa.VARCHAR, nullable=False, primary_key=True),  # PK
        sa.Column("districtname", sa.VARCHAR, nullable=False, primary_key=True),  # PK
        sa.Column("statename", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("telephone", sa.VARCHAR, nullable=False, primary_key=True),  # PK
        sa.Column("relatedsuboffice", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("relatedheadoffice", sa.VARCHAR, nullable=True, primary_key=False),
        sa.Column("longitude", sa.FLOAT, nullable=True, primary_key=False),
        sa.Column("latitude", sa.FLOAT, nullable=True, primary_key=False),
    )


def downgrade():
    op.drop_table("pincode")
