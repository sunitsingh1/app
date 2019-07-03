"""empty message

Revision ID: 551c4e6d4a8b
Revises: 590d89f981c0
Create Date: 2019-07-03 11:53:54.619764

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '551c4e6d4a8b'
down_revision = '590d89f981c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scope')
    op.drop_table('client_scope')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_scope',
    sa.Column('client_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('scope_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], name='client_scope_client_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['scope_id'], ['scope.id'], name='client_scope_scope_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('client_id', 'scope_id', name='client_scope_pkey')
    )
    op.create_table('scope',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='scope_pkey'),
    sa.UniqueConstraint('name', name='scope_name_key')
    )
    # ### end Alembic commands ###