import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
