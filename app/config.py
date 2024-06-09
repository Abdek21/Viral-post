import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')  # Default to SQLite for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')  # Default to local Redis for development
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')
