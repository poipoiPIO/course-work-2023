"""Added new table

Revision ID: 8788278a726b
Revises: ef15410bc578
Create Date: 2023-04-05 12:33:18.531682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8788278a726b'
down_revision = 'ef15410bc578'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('hashed_passwd', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admins_id'), 'admins', ['id'], unique=False)
    op.create_table('campuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_campuses_id'), 'campuses', ['id'], unique=False)
    op.create_table('client_infos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('registration_date', sa.Date(), nullable=False),
    sa.Column('checkout_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_infos_id'), 'client_infos', ['id'], unique=False)
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('campus_id', sa.Integer(), nullable=True),
    sa.Column('day_cost', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['campus_id'], ['campuses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rooms_id'), 'rooms', ['id'], unique=False)
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('info_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['info_id'], ['client_infos.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('info_id')
    )
    op.create_index(op.f('ix_clients_id'), 'clients', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_clients_id'), table_name='clients')
    op.drop_table('clients')
    op.drop_index(op.f('ix_rooms_id'), table_name='rooms')
    op.drop_table('rooms')
    op.drop_index(op.f('ix_client_infos_id'), table_name='client_infos')
    op.drop_table('client_infos')
    op.drop_index(op.f('ix_campuses_id'), table_name='campuses')
    op.drop_table('campuses')
    op.drop_index(op.f('ix_admins_id'), table_name='admins')
    op.drop_table('admins')
    # ### end Alembic commands ###
