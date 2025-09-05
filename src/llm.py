import os
from dotenv import load_dotenv
import time
# from src.prompt import MINI_MASTER_SYSTEM_PROMPT as SYSTEM_PROMPT
from src.json_prompt import json_prompt as SYSTEM_PROMPT

# Configuration For GEMINI
import google.generativeai as genai
load_dotenv()
try:
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
except KeyError:
    print("API ERROR")

# Function to get response 
def get_response(user_message, chat_session):
    retries = 3
    for i in range(retries):
        try:
            response = chat_session.send_message(user_message)
            return response.text
        except Exception as e:
            print(f"Error communicating with Gemini API: {e}")
            if i < retries - 1:
                print(f"Retrying in {2**(i+1)} seconds...")
                time.sleep(2**(i+1))
            else:
                return "I'm sorry, I'm having trouble connecting right now. Please try again later."


#nitialize chat session with system prompt
def initialize_chat_session():
    """
    Initializes and returns a new Gemini chat session,
    preloaded with the system prompt so that the assistant
    always behaves like the AIMIT enquiry chatbot.
    """
    return model.start_chat(
        history=[
            {"role": "user", "parts": [SYSTEM_PROMPT]}
        ]
    )


#Configuration For GROQ


# from groq import Groq

# # Load environment variables
# load_dotenv()
# 
# print("Loaded GROQ_API_KEY:", "FOUND" if api_key else "MISSING")
# if not api_key:
#     raise KeyError("GROQ_API_KEY not found in environment variables.")

# # Configure Groq client
# client = Groq(api_key=api_key)


# # Function to get response from Groq API
# def get_response(user_message, chat_session, model: str = "llama-3.3-70b-versatile"):
#     """
#     Sends user message + history to Groq model and returns assistant response text.
#     """
#     retries = 3
#     for i in range(retries):
#         try:
#             # Build messages (session history + new message)
#             messages = chat_session + [{"role": "user", "content": user_message}]

#             response = client.chat.completions.create(
#                 model=model,
#                 messages=messages
#             )

#             reply = response.choices[0].message.content

#             # Update history with assistant reply
#             chat_session.append({"role": "user", "content": user_message})
#             chat_session.append({"role": "assistant", "content": reply})

#             return reply
#         except Exception as e:
#             print(f"Error communicating with Groq API: {e}")
#             if i < retries - 1:
#                 wait = 2 ** (i + 1)
#                 print(f"Retrying in {wait} seconds...")
#                 time.sleep(wait)
#             else:
#                 return "I'm sorry, I'm having trouble connecting right now. Please try again later."

# # Initialize chat session
# def initialize_chat_session():
#     """
#     Returns an initial chat history list seeded with the system prompt.
#     This matches the structure expected by app.py.
#     """
#     return [{"role": "system", "content": SYSTEM_PROMPT}]

