from tools.gmail import authenticate_gmail


service = authenticate_gmail()


results = service.users().messages().list(
    userId="me",
    maxResults=5
).execute()


messages = results.get(
    "messages",
    []
)


print(messages)