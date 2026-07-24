from services.llm_service import ask_llm


response = ask_llm(
    """
    You are an email assistant.

    Classify this email:

    Subject:
    Job interview invitation

    Content:
    We would like to invite you to an interview next week.
    """
)


print(response)