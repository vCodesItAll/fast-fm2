import sys
from pathlib import Path

# Add the path to the utils module to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'utils'))

from database import Base
from sqlalchemy import Column, Integer, String, Date

class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_date = Column(Date)