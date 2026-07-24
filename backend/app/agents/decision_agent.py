def make_decision(email, classification, priority):

    score = priority["score"]

    subject = email["subject"].lower()
    body = email["body"].lower()

    
    decision = {
        "action": "",
        "reason": ""
    }


    # ==================================
    # Règle 1 : Emails très importants
    # ==================================

    important_keywords = [
        "interview",
        "entretien",
        "meeting",
        "appointment",
        "urgent",
        "schedule",
        "invitation"
    ]


    for keyword in important_keywords:

        if (
            keyword in subject
            or keyword in body
        ):

            decision["action"] = "NOTIFY_USER"

            decision["reason"] = (
                f"Important keyword detected: {keyword}"
            )

            return decision



    # ==================================
    # Règle 2 : Score élevé
    # ==================================

    if score >= 80:


        decision["action"] = "NOTIFY_USER"

        decision["reason"] = (
            "High priority email requires immediate attention"
        )



    # ==================================
    # Règle 3 : Score moyen
    # ==================================

    elif score >= 40:


        decision["action"] = "SAVE_AND_REVIEW"

        decision["reason"] = (
            "Medium priority email should be reviewed"
        )



    # ==================================
    # Règle 4 : Score faible
    # ==================================

    else:


        decision["action"] = "ARCHIVE"

        decision["reason"] = (
            "Low priority email can be archived"
        )



    return decision