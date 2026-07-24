from app.tools.gmail import (
    authenticate_gmail,
    get_emails
)

from app.agents.memory_agent import email_exists

from app.workflows.email_workflow import process_email

from app.database.database import SessionLocal
from app.database.models import AgentLog

from datetime import datetime
import schedule
import time



# ==============================
# REAL TIME AGENT STATUS
# ==============================

agent_status = {

    "status": "STOPPED",

    "last_scan": None,

    "processed_emails": 0,

    "last_action": "NONE",

    "processing_time": "0s",

    "errors": 0

}




def save_agent_log(
    status,
    processed_emails,
    last_action,
    processing_time
):

    db = SessionLocal()


    log = AgentLog(

        status=status,

        last_scan=str(datetime.now()),

        processed_emails=processed_emails,

        last_action=last_action,

        processing_time=processing_time

    )


    db.add(log)

    db.commit()

    db.close()





def check_emails():

    start_time = time.time()


    agent_status["status"] = "RUNNING"



    try:


        print("\n🔎 Checking Gmail...")



        service = authenticate_gmail()



        emails = get_emails(

            service,

            max_results=5

        )



        print(
            f"📩 {len(emails)} emails found"
        )



        processed_count = 0

        last_action = "NONE"



        for email in emails:


            print(
                "\nProcessing:",
                email["subject"]
            )



            if email_exists(
                email["message_id"]
            ):


                print(
                    "⏩ Email already processed"
                )

                continue




            result = process_email(

                email,

                service

            )



            processed_count += 1



            if result:


                action_result = result.get(
                    "action",
                    {}
                )


                last_action = action_result.get(

                    "executed_action",

                    "UNKNOWN"

                )



        processing_time = round(

            time.time() - start_time,

            2

        )



        # Mise à jour monitoring temps réel

        agent_status["status"] = "COMPLETED"

        agent_status["last_scan"] = str(
            datetime.now()
        )

        agent_status["processed_emails"] += processed_count

        agent_status["last_action"] = last_action

        agent_status["processing_time"] = (
            f"{processing_time}s"
        )



        save_agent_log(

            status="COMPLETED",

            processed_emails=processed_count,

            last_action=last_action,

            processing_time=f"{processing_time}s"

        )



        print(
            "\n📡 Monitoring log saved"
        )



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



    finally:


        if agent_status["status"] == "RUNNING":

            agent_status["status"] = "STOPPED"







def start_scheduler():


    print(
        "🚀 Email Agent started"
    )



    schedule.every(5).minutes.do(

        check_emails

    )



    # Premier scan immédiat

    check_emails()



    while True:


        schedule.run_pending()


        time.sleep(1)







if __name__ == "__main__":


    start_scheduler()