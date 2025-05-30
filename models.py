from sqlalchemy import Column, Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    