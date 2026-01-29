from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(String, index=True, nullable=False)
    domain = Column(String, nullable=False)

    raw_input = Column(Text, nullable=False)
    structured_output = Column(Text, nullable=True)

    status = Column(String, nullable=False)  # success / failed
    created_at = Column(DateTime, default=datetime.utcnow)
