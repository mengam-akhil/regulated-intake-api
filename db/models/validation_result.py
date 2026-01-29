from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from db.database import Base

class ValidationResult(Base):
    __tablename__ = "validation_results"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    rule_name = Column(String, nullable=False)
    passed = Column(Boolean, nullable=False)
    message = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
