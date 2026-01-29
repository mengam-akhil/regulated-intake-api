from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db
from db.models.documents import Document

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("/{document_id}")
def get_document(document_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == document_id).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "id": doc.id,
        "request_id": doc.request_id,
        "domain": doc.domain,
        "status": doc.status,
        "created_at": doc.created_at,
        "raw_input": doc.raw_input,
        "structured_output": doc.structured_output,
    }
