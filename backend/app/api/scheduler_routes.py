import os

from fastapi import APIRouter, Header, HTTPException

from app.scheduler.email_scheduler import (
    check_emails,
    get_agent_status
)


router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"]
)


@router.post("/run")
def run_scheduler(
    x_scheduler_secret: str | None = Header(default=None)
):

    expected_secret = os.getenv("SCHEDULER_SECRET")

    if not expected_secret:

        raise HTTPException(
            status_code=500,
            detail="SCHEDULER_SECRET is not configured"
        )

    if x_scheduler_secret != expected_secret:

        raise HTTPException(
            status_code=401,
            detail="Invalid scheduler secret"
        )

    try:

        result = check_emails()

        return {
            "success": True,
            "message": "Email scheduler executed successfully",
            "result": result
        }

    except Exception as e:

        print("❌ Scheduler error:", e)

        raise HTTPException(
            status_code=500,
            detail="Scheduler execution failed"
        )


@router.get("/status")
def scheduler_status():

    return get_agent_status()