from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.database import models

from app.auth.routes import router as auth_router
from app.api.routes import router
from app.api.scheduler_routes import router as scheduler_router


# =========================
# Database
# =========================

Base.metadata.create_all(bind=engine)


# =========================
# FastAPI Application
# =========================

app = FastAPI(
    title="AI Email Agent API"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://ai-email-agent-dashboard.netlify.app"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)


# =========================
# Authentication
# =========================

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)


# =========================
# API
# =========================

app.include_router(router)


# =========================
# Scheduler
# =========================

app.include_router(
    scheduler_router
)


# =========================
# Health Check
# =========================

@app.get("/")
def home():

    return {
        "message": "AI Email Agent API running"
    }