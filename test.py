from dotenv import load_dotenv
import os
load_dotenv()

# Get gemini_key from .env
GOOGLE_API_KEY = os.getenv("KEY")

print(GOOGLE_API_KEY)