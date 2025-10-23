import os
from dotenv import load_dotenv

load_dotenv()

# Environment variable name used for the Gemini / Google Generative AI key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def configure_genai():
    try:
        import google.generativeai as genai
    except Exception:
        print("google.generativeai not installed - skip genai configuration")
        return

    if GEMINI_API_KEY:
        genai.configure(api_key=GEMINI_API_KEY)
    else:
        print("Warning: GEMINI_API_KEY not found in environment. Set it in a local .env file or export it.")
