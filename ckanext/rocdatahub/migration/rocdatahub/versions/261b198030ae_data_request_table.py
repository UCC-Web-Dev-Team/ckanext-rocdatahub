"""data request table

Revision ID: 261b198030ae
Revises: 6da21148b92a
Create Date: 2024-01-24 08:36:46.167327

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision = '261b198030ae'
down_revision = '6da21148b92a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        u"data_request",
        sa.Column(u"id", sa.UnicodeText, primary_key=True),
        sa.Column(u"user_id", sa.UnicodeText, sa.ForeignKey(u"user.id")),
        sa.Column(u"package_id", sa.UnicodeText, sa.ForeignKey(u"package.id")),
        sa.Column(u"status", sa.String, nullable=True),
        sa.Column(u"requested_at", sa.DateTime, server_default=func.now()),
        sa.Column(u"approved_at", sa.DateTime, nullable=True),
    )


def downgrade():
    op.drop_table(u"data_request")
