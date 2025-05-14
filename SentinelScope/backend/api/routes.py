from fastapi import APIRouter
from api import auth
from core import osint_worker

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(osint_worker.router, prefix="/osint", tags=["osint"])
