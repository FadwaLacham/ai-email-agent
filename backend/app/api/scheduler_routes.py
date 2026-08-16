import os

from fastapi import (
    APIRouter,
    Header,
    HTTPException
)

from app.scheduler.email_scheduler import (
    check_emails,
    get_agent_status
)


# =========================
# ROUTER
# =========================

router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"]
)


# =========================
# RUN SCHEDULER
# =========================

@router.post("/run")
def run_scheduler(
    x_scheduler_secret: str | None = Header(
        default=None
    )
):

    # =========================
    # Get secret from environment
    # =========================

    expected_secret = os.getenv(
        "SCHEDULER_SECRET"
    )

    if not expected_secret:

        raise HTTPException(
            status_code=500,
            detail="SCHEDULER_SECRET is not configured"
        )

    # =========================
    # Validate secret
    # =========================

    if not x_scheduler_secret:

        raise HTTPException(
            status_code=401,
            detail="Scheduler secret is required"
        )

    if x_scheduler_secret != expected_secret:

        raise HTTPException(
            status_code=401,
            detail="Invalid scheduler secret"
        )

    # =========================
    # Run email agent
    # =========================

    try:

        print("🚀 Scheduler triggered")

        result = check_emails()

        print("✅ Scheduler completed")

        return {
            "success": True,
            "message": "Email scheduler executed successfully",
            "result": result
        }

    except Exception as e:

        print(
            "❌ Scheduler error:",
            repr(e)
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =========================
# SCHEDULER STATUS
# =========================

@router.get("/status")
def scheduler_status():

    return get_agent_status()