"""user extra

Revision ID: 6da21148b92a
Revises: 
Create Date: 2023-12-21 06:21:36.098993

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql



# revision identifiers, used by Alembic.
revision = '6da21148b92a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        u"user_extra",
        sa.Column(u"id", sa.UnicodeText, primary_key=True),
        sa.Column(u"user_id", sa.UnicodeText, sa.ForeignKey(u"user.id")),
        sa.Column(u"country", sa.UnicodeText, nullable=True),
        sa.Column(u"affiliation", sa.UnicodeText, nullable=True),
        sa.Column(u"agreement", sa.Boolean, nullable=True),
        sa.Column(u"advertisement", sa.Boolean, nullable=True),
        sa.Column(u"reviewer", sa.Boolean, nullable=True),
    )


def downgrade():
    op.drop_table(u"user_extra")
