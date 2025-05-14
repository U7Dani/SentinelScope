from fastapi import APIRouter
from backend.connectors.hibp_api import check_email

router = APIRouter()

@router.get("/leaks/{email}")
async def get_leaks(email: str):
    results = check_email(email)
    return {"email": email, "results": results}
