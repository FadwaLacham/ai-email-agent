from fastapi import APIRouter
from fastapi import Depends
from app.auth.dependencies import get_current_user
from app.database.models import AgentSetting
from app.database.database import SessionLocal
from app.database.models import Email
from app.database.models import Notification
from app.database.models import AgentLog
from app.database.database import SessionLocal
import pandas as pd
from fastapi import Query

from io import BytesIO

from fastapi.responses import StreamingResponse

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle



from sqlalchemy import func
from datetime import datetime


router = APIRouter()



@router.get("/emails")
def get_emails(
    
    current_user = Depends(get_current_user),
    
    search: str = None,

    priority: str = None,

    category: str = None,

    importance: str = None,

    urgency: str = None

):

    db = SessionLocal()


    query = db.query(Email)



    # Recherche texte

    if search:

        query = query.filter(

            Email.subject.ilike(
                f"%{search}%"
            )
            |
            Email.sender.ilike(
                f"%{search}%"
            )

        )



    # Filtre priorité

    if priority:

        query = query.filter(

            Email.priority == priority

        )



    # Filtre catégorie

    if category:

        query = query.filter(

            Email.category == category

        )



    # Filtre importance

    if importance:

        query = query.filter(

            Email.importance == importance

        )



    # Filtre urgence

    if urgency:

        query = query.filter(

            Email.urgency == urgency

        )



    emails = query.all()



    result = []


    for email in emails:

        result.append({

            "id": email.id,

            "sender": email.sender,

            "subject": email.subject,

            "category": email.category,

            "importance": email.importance,

            "urgency": email.urgency,

            "priority": email.priority,

            "score": email.score,

            "decision": email.decision

        })



    db.close()


    return result

@router.get("/statistics")
def get_statistics():

    db = SessionLocal()


    total = db.query(Email).count()


    high_priority = db.query(Email).filter(
        Email.priority == "HIGH"
    ).count()


    medium_priority = db.query(Email).filter(
        Email.priority == "MEDIUM"
    ).count()


    low_priority = db.query(Email).filter(
        Email.priority == "LOW"
    ).count()


    db.close()


    return {

        "total_emails": total,

        "high_priority": high_priority,

        "medium_priority": medium_priority,

        "low_priority": low_priority

    }



@router.get("/high-priority")
def get_high_priority_emails():

    db = SessionLocal()


    emails = db.query(Email).filter(
        Email.priority == "HIGH"
    ).all()


    result = []


    for email in emails:

        result.append({

            "sender": email.sender,

            "subject": email.subject,

            "score": email.score,

            "decision": email.decision

        })


    db.close()


    return result

@router.get("/categories")
def get_categories():

    db = SessionLocal()

    categories = (
        db.query(
            Email.category,
            func.count(Email.id)
        )
        .group_by(Email.category)
        .all()
    )

    db.close()

    return [
        {
            "category": category,
            "count": count
        }
        for category, count in categories
    ]

@router.get("/actions")
def get_actions():

    db = SessionLocal()

    actions = (
        db.query(
            Email.decision,
            func.count(Email.id)
        )
        .group_by(Email.decision)
        .all()
    )

    db.close()

    return [
        {
            "action": action,
            "count": count
        }
        for action, count in actions
    ]

@router.get("/recent")
def get_recent_emails():

    db = SessionLocal()

    emails = (
        db.query(Email)
        .order_by(Email.id.desc())
        .limit(10)
        .all()
    )

    db.close()

    return [
        {
            "sender": email.sender,
            "subject": email.subject,
            "priority": email.priority,
            "decision": email.decision
        }
        for email in emails
    ]

@router.get("/notifications")
def get_notifications():

    db = SessionLocal()

    notifications = (
        db.query(Notification)
        .order_by(Notification.id.desc())
        .all()
    )

    db.close()

    return [
        {
            "id": notification.id,
            "subject": notification.email_subject,
            "message": notification.message,
            "status": notification.status,
            "date": notification.created_at
        }
        for notification in notifications
    ]

@router.get("/monitoring")
def get_monitoring():

    db = SessionLocal()


    log = (
        db.query(AgentLog)
        .order_by(AgentLog.id.desc())
        .first()
    )


    db.close()


    if not log:

        return {
            "status": "NO DATA",
            "last_scan": "-",
            "processed_emails": 0,
            "last_action": "-",
            "processing_time": "-"
        }



    return {

        "status": log.status,

        "last_scan": log.last_scan,

        "processed_emails": log.processed_emails,

        "last_action": log.last_action,

        "processing_time": log.processing_time

    }

@router.get("/performance")
def get_performance():

    db = SessionLocal()


    total_emails = db.query(Email).count()


    high = db.query(Email).filter(
        Email.priority == "HIGH"
    ).count()


    medium = db.query(Email).filter(
        Email.priority == "MEDIUM"
    ).count()


    low = db.query(Email).filter(
        Email.priority == "LOW"
    ).count()



    db.close()


    return {

        "total_processed": total_emails,

        "priority_distribution": {

            "HIGH": high,

            "MEDIUM": medium,

            "LOW": low

        },

        "generated_at": str(datetime.now())

    }




@router.get("/monitoring/status")
def monitoring_status():

    db = SessionLocal()


    last_log = (
        db.query(AgentLog)
        .order_by(AgentLog.id.desc())
        .first()
    )


    db.close()


    if not last_log:

        return {
            "status": "STOPPED",
            "last_scan": None,
            "processed_emails": 0,
            "last_action": "None",
            "processing_time": "0s",
            "errors": 0
        }



    return {

        "status": last_log.status,

        "last_scan": last_log.last_scan,

        "processed_emails": last_log.processed_emails,

        "last_action": last_log.last_action,

        "processing_time": last_log.processing_time,

        "errors": 0
    }

@router.get("/analytics")
def analytics():

    db = SessionLocal()

    total_emails = db.query(Email).count()

    high_priority = db.query(Email).filter(
        Email.priority == "HIGH"
    ).count()

    medium_priority = db.query(Email).filter(
        Email.priority == "MEDIUM"
    ).count()

    low_priority = db.query(Email).filter(
        Email.priority == "LOW"
    ).count()

    total_logs = db.query(AgentLog).count()

    completed_logs = db.query(AgentLog).filter(
        AgentLog.status == "COMPLETED"
    ).count()

    success_rate = (
        round((completed_logs / total_logs) * 100, 2)
        if total_logs
        else 0
    )

    avg_time = 0

    logs = db.query(AgentLog).all()

    if logs:

        values = []

        for log in logs:

            try:
                values.append(
                    float(
                        log.processing_time.replace("s", "")
                    )
                )

            except Exception:
                pass

        if values:
            avg_time = round(
                sum(values) / len(values),
                2
            )

    top_category = db.query(

        Email.category,
        func.count(Email.id)

    ).group_by(
        Email.category

    ).order_by(

        func.count(Email.id).desc()

    ).first()

    top_action = db.query(

        Email.decision,
        func.count(Email.id)

    ).group_by(

        Email.decision

    ).order_by(

        func.count(Email.id).desc()

    ).first()

    db.close()

    return {

        "total_emails": total_emails,

        "average_processing_time": avg_time,

        "success_rate": success_rate,

        "high_priority": high_priority,

        "medium_priority": medium_priority,

        "low_priority": low_priority,

        "top_category": top_category[0] if top_category else None,

        "top_action": top_action[0] if top_action else None

    }

# =========================
# EXPORT EXCEL
# =========================

@router.get("/export/emails/excel")
def export_emails_excel():

    db = SessionLocal()

    emails = db.query(Email).all()


    data = []


    for email in emails:

        data.append({

            "Sender": email.sender,

            "Subject": email.subject,

            "Category": email.category,

            "Importance": email.importance,

            "Urgency": email.urgency,

            "Priority": email.priority,

            "Score": email.score,

            "Decision": email.decision

        })


    db.close()


    df = pd.DataFrame(data)


    output = BytesIO()


    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Emails"
        )


    output.seek(0)


    return StreamingResponse(

        output,

        media_type=
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

        headers={

            "Content-Disposition":
            "attachment; filename=emails.xlsx"

        }

    )



# =========================
# EXPORT PDF
# =========================

@router.get("/export/emails/pdf")
def export_emails_pdf():

    db = SessionLocal()


    emails = db.query(Email).all()


    output = BytesIO()


    pdf = SimpleDocTemplate(
        output
    )


    data = [

        [
            "Sender",
            "Subject",
            "Priority",
            "Decision"
        ]

    ]



    for email in emails:

        data.append(

            [

                email.sender,

                email.subject,

                email.priority,

                email.decision

            ]

        )



    table = Table(data)


    table.setStyle(

        TableStyle(

            [

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    None
                )

            ]

        )

    )


    pdf.build(
        [table]
    )


    db.close()


    output.seek(0)



    return StreamingResponse(

        output,

        media_type="application/pdf",

        headers={

            "Content-Disposition":
            "attachment; filename=emails.pdf"

        }

    )


@router.get("/settings")
def get_settings():

    db = SessionLocal()


    settings = (
        db.query(AgentSetting)
        .first()
    )


    db.close()


    if not settings:

        return {

            "model":"gemini",

            "temperature":0.7,

            "max_emails":100,

            "auto_action":True

        }



    return {

        "model":settings.model,

        "temperature":settings.temperature,

        "max_emails":settings.max_emails,

        "auto_action":settings.auto_action

    }



@router.put("/settings")
def update_settings(data:dict):

    db = SessionLocal()


    settings = (
        db.query(AgentSetting)
        .first()
    )


    if not settings:

        settings = AgentSetting()

        db.add(settings)



    settings.model = data["model"]

    settings.temperature = data["temperature"]

    settings.max_emails = data["max_emails"]

    settings.auto_action = data["auto_action"]


    db.commit()


    db.close()


    return {

        "message":
        "Settings updated"

    }