from fastapi import APIRouter
from backend.api import auth
from backend.core import osint_worker

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(osint_worker.router, prefix="/osint", tags=["osint"])
