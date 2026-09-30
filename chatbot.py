import json
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
if os.path.exists("history.json"):
    with open("history.json", "r") as file:
        history = json.load(file)
else:
    history = []
    
while True:
    user_input = input("You: ")
    if user_input=='exit':
        break
    history.append(
    {
        "role": "user",
        "parts": [
            {
                "text": user_input
            }
        ]
    }
)
    response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=history
    )
    print("AI:", response.text)
    history.append(
    {
        "role": "model",
        "parts": [
            {
                "text": response.text
            }
        ]
    }
)
    with open("history.json", "w") as file:


        json.dump(history, file, indent=4)
