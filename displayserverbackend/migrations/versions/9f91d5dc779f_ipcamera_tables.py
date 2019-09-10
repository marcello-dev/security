"""IPCamera tables

Revision ID: 9f91d5dc779f
Revises: 
Create Date: 2019-08-13 19:02:00.195043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f91d5dc779f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ip_camera',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('ftp', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ip_camera_host'), 'ip_camera', ['host'], unique=True)
    op.create_index(op.f('ix_ip_camera_name'), 'ip_camera', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_ip_camera_name'), table_name='ip_camera')
    op.drop_index(op.f('ix_ip_camera_host'), table_name='ip_camera')
    op.drop_table('ip_camera')
    # ### end Alembic commands ###