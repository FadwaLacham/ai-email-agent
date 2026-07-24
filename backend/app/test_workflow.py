from tools.gmail import authenticate_gmail, get_emails
from workflows.email_workflow import process_email



print("🔐 Connecting to Gmail...")

service = authenticate_gmail()


print("📩 Fetching emails...")


emails = get_emails(
    service,
    max_results=5
)


print(f"Found {len(emails)} emails")


for email in emails:

    print("\n======================")

    print("Processing email:")
    print(email["subject"])


    result = process_email(email)


    print("\nFINAL RESULT")

    print(result)