def calculate_priority(email, classification):

    importance = classification.get(
        "importance",
        "LOW"
    )

    category = classification.get(
        "category",
        ""
    )


    score = 0


    # Importance from LLM
    if importance == "HIGH":
        score += 70

    elif importance == "MEDIUM":
        score += 40

    else:
        score += 10


    # Rules based on category
    if "Interview" in category:
        score += 20

    elif "Job" in category:
        score += 10


    # Convert score to label

    if score >= 80:
        priority = "HIGH"

    elif score >= 40:
        priority = "MEDIUM"

    else:
        priority = "LOW"


    return {
        "priority": priority,
        "score": score
    }