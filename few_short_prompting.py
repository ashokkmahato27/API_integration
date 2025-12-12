import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel("gemini-2.5-flash")
gemini_response = gemini_model.generate_content("""Example 1:
Q: What is photosynthesis?
A: Plants make food from sunlight.

Example 2:
Q: What is gravity?
A: A force that pulls objects toward Earth.

Q: In the same style, what is condensation?""")

print("gemini_response:\n", gemini_response.text)