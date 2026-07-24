from app.agents.email_classifier_agent import classify_email
from app.tools.priority_scorer import calculate_priority
from app.agents.memory_agent import save_email
from app.agents.decision_agent import make_decision
from app.agents.action_agent import execute_action



def process_email(email, gmail_service):

    print("📩 Step 1: Email received")


    print("🤖 Step 2: Classification Agent running")

    classification = classify_email(email)



    print("⚡ Step 3: Priority Agent running")

    priority = calculate_priority(
        email,
        classification
    )



    print("🧠 Step 4: Decision Agent running")

    decision = make_decision(
        email,
        classification,
        priority
    )



    print("🚀 Step 5: Action Agent running")

    action = execute_action(
        gmail_service,
        email,
        decision
    )



    print("💾 Step 6: Memory Agent running")


    final_result = {

        "email": email,

        "classification": classification,

        "priority": priority,

        "decision": decision,

        "action": action,

        # Pour le monitoring scheduler
        "executed_action": action.get(
            "executed_action",
            "UNKNOWN"
        ),

        "status": action.get(
            "status",
            "UNKNOWN"
        )

    }


    save_email(final_result)



    print("✅ Workflow completed")


    return final_result