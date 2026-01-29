from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from db.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)

    action = Column(String, nullable=False)
    actor = Column(String, default="system")
    timestamp = Column(DateTime, default=datetime.utcnow)
