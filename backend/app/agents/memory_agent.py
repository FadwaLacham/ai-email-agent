from app.database.database import SessionLocal
from app.database.models import Email


def email_exists(message_id):

    db = SessionLocal()

    try:

        email = db.query(Email).filter(
            Email.message_id == message_id
        ).first()

        return email is not None


    except Exception as e:

        print(
            "❌ Error checking email:",
            e
        )

        return False


    finally:

        db.close()



def save_email(result):

    db = SessionLocal()

    try:

        email = result["email"]

        classification = result["classification"]

        priority = result["priority"]

        decision = result["decision"]


        if email_exists(email["message_id"]):

            print("⚠️ Email already exists in database")

            return False



        new_email = Email(

            message_id=email["message_id"],

            sender=email["sender"],

            subject=email["subject"],

            body=email["body"],


            category=classification["category"],

            importance=classification["importance"],

            urgency=classification["urgency"],


            priority=priority["priority"],

            score=priority["score"],


            decision=decision["action"]

        )


        db.add(new_email)

        db.commit()


        print("💾 Email saved in database")

        return True



    except Exception as e:

        db.rollback()

        print(
            "❌ Database error:",
            e
        )

        return False


    finally:

        db.close()