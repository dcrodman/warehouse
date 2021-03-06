# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
uploaded_via field for Release and Files

Revision ID: b00323b3efd8
Revises: f2a453c96ded
Create Date: 2018-07-25 17:29:01.995083
"""

from alembic import op
import sqlalchemy as sa


revision = "b00323b3efd8"
down_revision = "f2a453c96ded"


def upgrade():
    op.add_column("release_files", sa.Column("uploaded_via", sa.Text(), nullable=True))
    op.add_column("releases", sa.Column("uploaded_via", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("releases", "uploaded_via")
    op.drop_column("release_files", "uploaded_via")
