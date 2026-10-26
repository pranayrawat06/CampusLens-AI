import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "paste_your_real_api_key_here":
    raise SystemExit("API key missing. Check your .env file.")

client = genai.Client(api_key=api_key)

print("Connecting to Gemma 4...")

try:
    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents=(
            "You are CampusLens AI, a college announcement "
            "assistant. Reply with: CampusLens AI is connected!"
        ),
    )

    if response.text:
        print("\nSUCCESS!")
        print(response.text)
    else:
        print("The model returned no text. Check the API response.")

except Exception as error:
    print("\nConnection failed.")
    print("Error type:", type(error).__name__)
    print("Error details:", str(error))