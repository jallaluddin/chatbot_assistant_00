import google.generativeai as genai
import os
from dotenv import  load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in enviroment variables")

genai.configure(api_key=GEMINI_API_KEY)

system_prompt = """
You are Smart Student Agent Assistant 🧠.
Your job is to:
- Help with academic questions.
- Give useful study tips.
- Summarize short text.
Respond in simple and clear language for students.
"""
model = genai.GenerativeModel("gemini-1.5-flash")
print("🎓 Smart Student Agent Assistant 🧠")
print("Type 'exit' to end the chat.")
print("="*40)

while True:
    user_input = input("👨‍🎓 You:: ")
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Goodbye and happy studying!")
        break

    response = model.generate_content(system_prompt + "\nUser: " + user_input)
    print(f"🤖 Assistant: {response.text}\n")