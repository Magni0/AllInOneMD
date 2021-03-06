"""empty message

Revision ID: e2c61621b04a
Revises: 68f541872f81
Create Date: 2021-02-22 16:37:14.628417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2c61621b04a'
down_revision = '68f541872f81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('images')
    op.add_column('accounts', sa.Column('username', sa.String(), nullable=False))
    op.drop_constraint('accounts_email_key', 'accounts', type_='unique')
    op.create_unique_constraint(None, 'accounts', ['username'])
    op.drop_column('accounts', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'accounts', type_='unique')
    op.create_unique_constraint('accounts_email_key', 'accounts', ['email'])
    op.drop_column('accounts', 'username')
    op.create_table('images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('imagename', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('doc_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['doc_id'], ['documents.id'], name='images_doc_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    # ### end Alembic commands ###
