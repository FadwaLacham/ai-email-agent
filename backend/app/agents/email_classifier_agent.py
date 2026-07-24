import json

from app.services.llm_service import ask_llm



def classify_email(email):

    prompt = f"""

You are an AI email classification agent specialized in email prioritization.

Analyze the email carefully and classify it.

You MUST return ONLY valid JSON.
Do not add markdown or explanations.


Allowed categories:

- Job Alert
- Interview
- Work
- Finance
- Personal
- Marketing
- Security
- Notification
- Other


Email:

Sender:
{email['sender']}


Subject:
{email['subject']}


Body:
{email['body']}



Classification format:

{{
    "importance": "HIGH | MEDIUM | LOW",
    "category": "",
    "urgency": "HIGH | MEDIUM | LOW",
    "summary": "",
    "action": ""
}}



Classification rules:


CATEGORY RULES:

1. Job Alert:
Use "Job Alert" when:
- LinkedIn job alerts
- recruitment emails
- job opportunities
- job matching preferences
- company hiring notifications


2. Interview:
Use "Interview" when:
- interview invitation
- interview scheduling
- recruiter asking for availability


3. Work:
Use "Work" when:
- professional requests
- tasks
- meetings
- company communication


4. Security:
Use "Security" when:
- password changes
- suspicious login
- account security alerts



IMPORTANCE RULES:

HIGH:
- Interview invitation
- Urgent work request
- Security alert
- Important personal message


MEDIUM:
- Job alerts
- Professional notifications
- Newsletters that may be useful


LOW:
- Advertising
- Promotions
- Marketing campaigns



URGENCY RULES:

HIGH:
- Requires immediate action
- Deadline approaching


MEDIUM:
- Requires attention but not immediately


LOW:
- Informational emails



Return JSON only.

"""


    response = ask_llm(prompt)


    # Remove possible markdown from LLM response
    response = response.replace("```json", "")
    response = response.replace("```", "")
    response = response.strip()


    result = json.loads(response)


    return result