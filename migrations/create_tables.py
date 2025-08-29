"""Initial migration - create all tables"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.database import engine
from lib.models import Base

def upgrade():
    """Create all tables"""
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")

def downgrade():
    """Drop all tables"""
    Base.metadata.drop_all(bind=engine)
    print("Tables dropped successfully")

if __name__ == "__main__":
    upgrade()