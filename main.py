from fastapi import FastAPI
from db.database import init_db

from db.routes.documents import router as documents_router
from db.routes.audit import router as audit_router

app = FastAPI(title="Regulated Intake API")

init_db()

app.include_router(documents_router, prefix="/documents", tags=["Documents"])
app.include_router(audit_router, prefix="/audit", tags=["Audit"])
