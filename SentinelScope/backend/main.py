from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import api_router
from backend.db.database import create_db_and_tables

app = FastAPI(title="SentinelScope OSINT API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await create_db_and_tables()

app.include_router(api_router)
