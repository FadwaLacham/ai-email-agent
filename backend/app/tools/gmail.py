import os
import base64
import re

from bs4 import BeautifulSoup

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build


# Permission nécessaire pour lire + modifier les emails
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]


# =========================
# Gmail Authentication
# =========================

def authenticate_gmail():

    print("1 - Starting Gmail authentication")

    creds = None


    if os.path.exists("token.json"):

        print("2 - Existing token found")

        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )


    if not creds or not creds.valid:

        print("3 - Need authentication")


        if creds and creds.expired and creds.refresh_token:

            print("4 - Refreshing token")

            creds.refresh(Request())


        else:

            print("5 - Opening Google login")


            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )


            creds = flow.run_local_server(
                port=0
            )


            print("6 - Google authentication finished")



        with open(
            "token.json",
            "w"
        ) as token:

            token.write(
                creds.to_json()
            )


        print("7 - token.json created")



    service = build(
        "gmail",
        "v1",
        credentials=creds
    )


    print("8 - Gmail service created")


    return service





# =========================
# Cleaning
# =========================

def clean_body(text):

    """
    Clean email body:
    - Remove HTML
    - Remove extra spaces
    """


    if not text:

        return ""


    soup = BeautifulSoup(
        text,
        "html.parser"
    )


    text = soup.get_text(
        separator=" "
    )


    text = re.sub(
        r"\s+",
        " ",
        text
    )


    return text.strip()





# =========================
# Extract Body
# =========================

def extract_body(payload):

    """
    Extract readable email body
    """


    body = ""


    # Simple email

    if payload.get("body", {}).get("data"):

        body = payload["body"]["data"]



    # Multipart email

    elif "parts" in payload:


        for part in payload["parts"]:


            mime_type = part.get(
                "mimeType"
            )


            if mime_type == "text/plain":

                body = part["body"].get(
                    "data",
                    ""
                )

                break



            elif mime_type == "text/html":

                body = part["body"].get(
                    "data",
                    ""
                )



    if body:

        try:

            decoded = base64.urlsafe_b64decode(
                body
            ).decode(
                "utf-8",
                errors="ignore"
            )


            return clean_body(
                decoded
            )


        except Exception as e:

            print(
                "Body decoding error:",
                e
            )


    return ""





# =========================
# Get Unread Emails
# =========================

def get_emails(
        service,
        max_results=10
):

    """
    Retrieve only unread emails from Gmail
    """


    results = service.users().messages().list(

        userId="me",

        q="is:unread",

        maxResults=max_results

    ).execute()



    messages = results.get(
        "messages",
        []
    )



    emails = []



    print(
        f"📩 {len(messages)} unread emails found"
    )



    for message in messages:


        msg = service.users().messages().get(

            userId="me",

            id=message["id"],

            format="full"

        ).execute()



        headers = msg["payload"]["headers"]



        email_data = {

            "message_id": message["id"],

            "sender": "",

            "subject": "",

            "date": "",

            "body": ""

        }




        for header in headers:


            name = header["name"].lower()



            if name == "from":

                email_data["sender"] = header["value"]



            elif name == "subject":

                email_data["subject"] = header["value"]



            elif name == "date":

                email_data["date"] = header["value"]





        email_data["body"] = extract_body(

            msg["payload"]

        )



        emails.append(
            email_data
        )



    return emails





# =========================
# Mark email as read
# =========================

def mark_as_read(service, message_id):

    response = service.users().messages().modify(
        userId="me",
        id=message_id,
        body={
            "removeLabelIds": ["UNREAD"]
        }
    ).execute()

    print("📖 Gmail response:", response)

# =========================
# Gmail Actions
# =========================


def archive_email(service, message_id):

    service.users().messages().modify(

        userId="me",

        id=message_id,

        body={
            "removeLabelIds": ["INBOX"]
        }

    ).execute()


    print("📂 Email archived")





def add_review_label(service, message_id):


    # Créer le label si nécessaire
    labels = service.users().labels().list(
        userId="me"
    ).execute()


    label_id = None


    for label in labels.get("labels", []):

        if label["name"] == "AI_REVIEW":

            label_id = label["id"]



    if not label_id:


        new_label = service.users().labels().create(

            userId="me",

            body={
                "name": "AI_REVIEW"
            }

        ).execute()


        label_id = new_label["id"]



    service.users().messages().modify(

        userId="me",

        id=message_id,

        body={
            "addLabelIds":[label_id]
        }

    ).execute()



    print("📌 Email marked for review")





def send_notification(email):

    print(
        "🔔 Notification:",
        email["subject"]
    )

def create_label(service, label_name):

    labels = service.users().labels().list(
        userId="me"
    ).execute()


    existing_labels = labels.get(
        "labels",
        []
    )


    for label in existing_labels:

        if label["name"] == label_name:
            return label["id"]



    label = service.users().labels().create(

        userId="me",

        body={
            "name": label_name
        }

    ).execute()


    return label["id"]




def add_label(service, message_id, label_name):

    label_id = create_label(
        service,
        label_name
    )


    service.users().messages().modify(

        userId="me",

        id=message_id,

        body={

            "addLabelIds": [
                label_id
            ]

        }

    ).execute()



def mark_as_read(service, message_id):

    service.users().messages().modify(

        userId="me",

        id=message_id,

        body={

            "removeLabelIds": [
                "UNREAD"
            ]

        }

    ).execute()