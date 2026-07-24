from tools.gmail import authenticate_gmail, get_emails


service = authenticate_gmail()


emails = get_emails(
    service,
    max_results=5
)


for email in emails:

    print("\n===================")
    print("FROM:", email["sender"])
    print("SUBJECT:", email["subject"])
    print("DATE:", email["date"])
    print("BODY:", email["body"][:300])