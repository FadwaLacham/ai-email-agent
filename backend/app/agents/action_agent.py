import base64

from email.mime.text import MIMEText

from app.tools.gmail import (
    add_label,
    mark_as_read
)

from app.database.database import SessionLocal
from app.database.models import Notification




def save_notification(subject, message, status="SENT"):


    db = SessionLocal()


    notification = Notification(

        email_subject=subject,

        message=message,

        status=status

    )


    db.add(notification)

    db.commit()

    db.close()


    print("💾 Notification saved in database")





def send_notification(service, subject, message):


    email = MIMEText(message)


    email["to"] = "fadwa.lacham@gmail.com"

    email["subject"] = subject



    encoded_message = base64.urlsafe_b64encode(
        email.as_bytes()
    ).decode()



    service.users().messages().send(

        userId="me",

        body={
            "raw": encoded_message
        }

    ).execute()



    print("🔔 Notification email sent")







def archive_email(service, message_id):


    service.users().messages().modify(

        userId="me",

        id=message_id,

        body={

            "removeLabelIds":[
                "INBOX"
            ]

        }

    ).execute()



    print("📂 Email archived")







def execute_action(service, email, decision):


    action = decision["action"]



    result = {

        "executed_action":"",

        "status":""

    }





    # ==========================
    # HIGH PRIORITY
    # ==========================


    if action == "NOTIFY_USER":



        subject = "AI Email Agent Alert"


        message = f"""
An important email has been detected.

Subject:
{email['subject']}


Sender:
{email['sender']}
"""



        send_notification(

            service,

            subject,

            message

        )



        save_notification(

            email["subject"],

            message,

            "SENT"

        )



        add_label(

            service,

            email["message_id"],

            "AI_HIGH_PRIORITY"

        )



        mark_as_read(

            service,

            email["message_id"]

        )



        result["executed_action"] = (

            "Notification sent + saved + label added"

        )


        result["status"] = "DONE"



        print("🏷️ Label AI_HIGH_PRIORITY added")

        print("📖 Email marked as read")







    # ==========================
    # MEDIUM PRIORITY
    # ==========================


    elif action == "SAVE_AND_REVIEW":



        add_label(

            service,

            email["message_id"],

            "AI_REVIEW"

        )



        mark_as_read(

            service,

            email["message_id"]

        )



        result["executed_action"] = (

            "Email labeled for review"

        )


        result["status"] = "DONE"



        print("📌 Email marked for review")

        print("📖 Email marked as read")








    # ==========================
    # LOW PRIORITY
    # ==========================


    elif action == "ARCHIVE":



        archive_email(

            service,

            email["message_id"]

        )



        add_label(

            service,

            email["message_id"],

            "AI_ARCHIVED"

        )



        mark_as_read(

            service,

            email["message_id"]

        )



        result["executed_action"] = (

            "Email archived"

        )



        result["status"] = "DONE"



        print("🏷️ Label AI_ARCHIVED added")

        print("📖 Email marked as read")








    else:


        result["executed_action"] = "No action"


        result["status"] = "FAILED"


        print("❌ Unknown action")





    return result