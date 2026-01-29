from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from datetime import datetime
from db.database import Base

class ExtractedRecord(Base):
    __tablename__ = "extracted_records"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    field_name = Column(String, nullable=False)
    field_value = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
