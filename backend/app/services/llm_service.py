
"""
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_llm(prompt):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text

"""

from groq import Groq
import os
from dotenv import load_dotenv


# Charger les variables du fichier .env
load_dotenv()


# Créer le client Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def ask_llm(prompt):

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )


    return response.choices[0].message.content


