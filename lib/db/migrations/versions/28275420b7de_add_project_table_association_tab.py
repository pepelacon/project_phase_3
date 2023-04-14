"""Add project_table  Association Tab

Revision ID: 28275420b7de
Revises: 9df7d6d39b19
Create Date: 2023-04-14 15:15:21.220194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28275420b7de'
down_revision = '9df7d6d39b19'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('manager_id', sa.INTEGER(), nullable=True),
    sa.Column('employee_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['manager_id'], ['managers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
