from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager
import asyncio

from app.database.database import Base, engine
from app.database import models

from app.auth.routes import router as auth_router
from app.api.routes import router
from app.api.scheduler_routes import router as scheduler_router

from app.scheduler.email_scheduler import check_emails


# =========================
# Database
# =========================

Base.metadata.create_all(bind=engine)


# =========================
# Background Email Scheduler
# =========================

async def scheduler_loop():

    print("🚀 Email Agent scheduler started")
    print("⏱️ Gmail will be checked every 5 minutes")

    while True:

        try:

            print("\n🔎 Starting automatic Gmail scan...")

            # check_emails() is synchronous,
            # so run it in a separate thread
            await asyncio.to_thread(
                check_emails
            )

        except Exception as e:

            print(
                "❌ Scheduler error:",
                e
            )

        print(
            "💤 Next Gmail check in 5 minutes..."
        )

        # Wait 5 minutes before the next scan
        await asyncio.sleep(300)


# =========================
# FastAPI Lifespan
# =========================

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Start background scheduler
    scheduler_task = asyncio.create_task(
        scheduler_loop()
    )

    print(
        "✅ Background email scheduler started"
    )

    yield

    # =========================
    # Shutdown
    # =========================

    print(
        "🛑 Stopping email scheduler..."
    )

    scheduler_task.cancel()

    try:

        await scheduler_task

    except asyncio.CancelledError:

        print(
            "🛑 Email scheduler stopped"
        )


# =========================
# FastAPI Application
# =========================

app = FastAPI(
    title="AI Email Agent API",
    lifespan=lifespan
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

app.include_router(
    router
)


# =========================
# Scheduler API
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