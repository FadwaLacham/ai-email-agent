from database.database import SessionLocal
from database.models import Email


db = SessionLocal()


emails = db.query(Email).all()


for email in emails:

    print(email.subject)
    print(email.category)
    print(email.priority)
    print(email.decision)
    print("----------------")