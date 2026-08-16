from app.tools.gmail import (
    authenticate_gmail,
    get_emails
)

from app.agents.memory_agent import email_exists
from app.workflows.email_workflow import process_email

from app.database.database import SessionLocal
from app.database.models import AgentLog

from datetime import datetime
import time


# ==============================
# AGENT STATUS
# ==============================

agent_status = {
    "status": "STOPPED",
    "last_scan": None,
    "processed_emails": 0,
    "last_action": "NONE",
    "processing_time": "0s",
    "errors": 0
}


# ==============================
# SAVE LOG
# ==============================

def save_agent_log(
    status,
    processed_emails,
    last_action,
    processing_time
):

    db = SessionLocal()

    try:

        log = AgentLog(
            status=status,
            last_scan=str(datetime.now()),
            processed_emails=processed_emails,
            last_action=last_action,
            processing_time=processing_time
        )

        db.add(log)
        db.commit()

    finally:

        db.close()


# ==============================
# CHECK GMAIL
# ==============================

def check_emails():

    start_time = time.time()

    agent_status["status"] = "RUNNING"

    try:

        print("\n🔎 Checking Gmail...")

        # =========================
        # Gmail authentication
        # =========================

        service = authenticate_gmail()

        # =========================
        # Get unread emails
        # =========================

        emails = get_emails(
            service,
            max_results=5
        )

        print(
            f"📩 {len(emails)} emails found"
        )

        processed_count = 0
        last_action = "NONE"

        # =========================
        # Process emails
        # =========================

        for email in emails:

            print(
                "\nProcessing:",
                email["subject"]
            )

            # Already processed?
            if email_exists(
                email["message_id"]
            ):

                print(
                    "⏩ Email already processed"
                )

                continue

            # =========================
            # AI Workflow
            # =========================

            result = process_email(
                email,
                service
            )

            processed_count += 1

            # =========================
            # Get action
            # =========================

            if result:

                action_result = result.get(
                    "action",
                    {}
                )

                last_action = action_result.get(
                    "executed_action",
                    "UNKNOWN"
                )

        # =========================
        # Processing time
        # =========================

        processing_time = round(
            time.time() - start_time,
            2
        )

        # =========================
        # Update status
        # =========================

        agent_status["status"] = "COMPLETED"

        agent_status["last_scan"] = str(
            datetime.now()
        )

        agent_status["processed_emails"] += (
            processed_count
        )

        agent_status["last_action"] = (
            last_action
        )

        agent_status["processing_time"] = (
            f"{processing_time}s"
        )

        # =========================
        # Save monitoring log
        # =========================

        save_agent_log(
            status="COMPLETED",
            processed_emails=processed_count,
            last_action=last_action,
            processing_time=f"{processing_time}s"
        )

        print(
            "\n📡 Monitoring log saved"
        )

        print(
            "✅ Email scan completed"
        )

        return {
            "success": True,
            "processed_emails": processed_count,
            "last_action": last_action,
            "processing_time": f"{processing_time}s"
        }

    except Exception as e:

        print(
            "❌ Agent Error:",
            e
        )

        agent_status["status"] = "ERROR"
        agent_status["errors"] += 1

        save_agent_log(
            status="ERROR",
            processed_emails=0,
            last_action="ERROR",
            processing_time="0s"
        )

        # Très important :
        # on retourne l'erreur au lieu de la cacher

        raise

    finally:

        if agent_status["status"] == "RUNNING":

            agent_status["status"] = "STOPPED"


# ==============================
# GET CURRENT STATUS
# ==============================

def get_agent_status():

    return agent_status