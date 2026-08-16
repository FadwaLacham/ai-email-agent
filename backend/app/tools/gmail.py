import os
import json
import base64
import re

from bs4 import BeautifulSoup

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build


# ============================================================
# Gmail Permissions
# ============================================================

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
]


# ============================================================
# Gmail Authentication
# ============================================================

def authenticate_gmail():

    print("🔐 Starting Gmail authentication")

    creds = None

    # ========================================================
    # PRODUCTION
    # Read token from environment variable
    # ========================================================

    token_json = os.getenv("GMAIL_TOKEN_JSON")

    if token_json:

        print("☁️ Loading Gmail token from environment")

        try:

            token_data = json.loads(token_json)

            creds = Credentials.from_authorized_user_info(
                token_data,
                SCOPES
            )

            print("✅ Gmail token loaded from environment")

        except Exception as e:

            print(
                "❌ Error loading GMAIL_TOKEN_JSON:",
                e
            )

            raise

    # ========================================================
    # LOCAL
    # Read token.json
    # ========================================================

    elif os.path.exists("token.json"):

        print("💻 Existing token.json found")

        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    # ========================================================
    # Refresh token
    # ========================================================

    if creds and creds.expired and creds.refresh_token:

        print("🔄 Refreshing Gmail token")

        try:

            creds.refresh(Request())

            print("✅ Gmail token refreshed")

        except Exception as e:

            print(
                "❌ Error refreshing Gmail token:",
                e
            )

            raise

    # ========================================================
    # Invalid credentials
    # ========================================================

    if not creds or not creds.valid:

        print("⚠️ Gmail authentication required")

        # ----------------------------------------------------
        # Production
        # ----------------------------------------------------

        if os.getenv("GMAIL_TOKEN_JSON"):

            raise RuntimeError(
                "Gmail token is invalid or expired. "
                "Please update GMAIL_TOKEN_JSON."
            )

        # ----------------------------------------------------
        # Local development
        # ----------------------------------------------------

        if not os.path.exists("credentials.json"):

            raise FileNotFoundError(
                "credentials.json not found."
            )

        print("🌐 Opening Google login")

        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(
            port=0
        )

        print("✅ Google authentication finished")

        # Save token locally

        with open(
            "token.json",
            "w"
        ) as token:

            token.write(
                creds.to_json()
            )

        print("💾 token.json created")

    # ========================================================
    # Build Gmail API service
    # ========================================================

    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    print("✅ Gmail service created")

    return service


# ============================================================
# Cleaning
# ============================================================

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


# ============================================================
# Extract Email Body
# ============================================================

def extract_body(payload):

    """
    Extract readable email body.
    Supports simple and multipart emails.
    """

    body = ""

    # ========================================================
    # Simple email
    # ========================================================

    if payload.get(
        "body",
        {}
    ).get("data"):

        body = payload["body"]["data"]

    # ========================================================
    # Multipart email
    # ========================================================

    elif "parts" in payload:

        for part in payload["parts"]:

            mime_type = part.get(
                "mimeType"
            )

            part_body = part.get(
                "body",
                {}
            )

            if mime_type == "text/plain":

                body = part_body.get(
                    "data",
                    ""
                )

                break

            elif mime_type == "text/html":

                body = part_body.get(
                    "data",
                    ""
                )

    # ========================================================
    # Decode
    # ========================================================

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
                "❌ Body decoding error:",
                e
            )

    return ""


# ============================================================
# Get Unread Emails
# ============================================================

def get_emails(
    service,
    max_results=10
):

    """
    Retrieve unread emails from Gmail.
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

    # ========================================================
    # Process emails
    # ========================================================

    for message in messages:

        message_id = message["id"]

        msg = service.users().messages().get(

            userId="me",

            id=message_id,

            format="full"

        ).execute()

        payload = msg.get(
            "payload",
            {}
        )

        headers = payload.get(
            "headers",
            []
        )

        email_data = {

            "message_id": message_id,

            "sender": "",

            "subject": "",

            "date": "",

            "body": ""

        }

        # ====================================================
        # Extract headers
        # ====================================================

        for header in headers:

            name = header.get(
                "name",
                ""
            ).lower()

            value = header.get(
                "value",
                ""
            )

            if name == "from":

                email_data["sender"] = value

            elif name == "subject":

                email_data["subject"] = value

            elif name == "date":

                email_data["date"] = value

        # ====================================================
        # Extract body
        # ====================================================

        email_data["body"] = extract_body(
            payload
        )

        emails.append(
            email_data
        )

    return emails


# ============================================================
# Mark Email as Read
# ============================================================

def mark_as_read(
    service,
    message_id
):

    response = service.users().messages().modify(

        userId="me",

        id=message_id,

        body={
            "removeLabelIds": [
                "UNREAD"
            ]
        }

    ).execute()

    print(
        "📖 Gmail response:",
        response
    )


# ============================================================
# Archive Email
# ============================================================

def archive_email(
    service,
    message_id
):

    service.users().messages().modify(

        userId="me",

        id=message_id,

        body={
            "removeLabelIds": [
                "INBOX"
            ]
        }

    ).execute()

    print(
        "📂 Email archived"
    )


# ============================================================
# Create Gmail Label
# ============================================================

def create_label(
    service,
    label_name
):

    labels = service.users().labels().list(

        userId="me"

    ).execute()

    existing_labels = labels.get(
        "labels",
        []
    )

    # ========================================================
    # Check existing label
    # ========================================================

    for label in existing_labels:

        if label["name"] == label_name:

            return label["id"]

    # ========================================================
    # Create new label
    # ========================================================

    label = service.users().labels().create(

        userId="me",

        body={
            "name": label_name
        }

    ).execute()

    return label["id"]


# ============================================================
# Add Label
# ============================================================

def add_label(
    service,
    message_id,
    label_name
):

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

    print(
        f"🏷️ Label '{label_name}' added"
    )


# ============================================================
# AI Review Label
# ============================================================

def add_review_label(
    service,
    message_id
):

    add_label(
        service,
        message_id,
        "AI_REVIEW"
    )

    print(
        "📌 Email marked for review"
    )


# ============================================================
# Send Notification
# ============================================================

def send_notification(email):

    print(
        "🔔 Notification:",
        email.get(
            "subject",
            "No subject"
        )
    )