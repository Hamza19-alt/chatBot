import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///chat_history.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = "VOPENAI"  
