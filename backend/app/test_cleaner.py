from tools.gmail import authenticate_gmail, get_emails
from agents.email_cleaner_agent import EmailCleanerAgent


service = authenticate_gmail()


emails = get_emails(
    service,
    max_results=3
)


cleaner = EmailCleanerAgent()


for email in emails:

    cleaned_email = cleaner.clean(
        email
    )


    print("\n================")
    print(
        cleaned_email["subject"]
    )

    print(
        cleaned_email["clean_body"][:500]
    )