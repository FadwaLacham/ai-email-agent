from agents.email_classifier_agent import classify_email



email = {

    "sender": "linkedin@gmail.com",

    "subject": "Développeur Java/JEE (H/F) at Inetum",

    "body": """
    Your job alert for Développeur web in Rabat.
    New jobs match your preferences.
    """
}



result = classify_email(email)


print(result)