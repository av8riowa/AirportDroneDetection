# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/drone_data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EMAIL_SENDER = 'your_email@example.com'
    EMAIL_RECIPIENTS = ['recipient@example.com']
    EMAIL_SERVER = 'smtp.example.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_USERNAME = 'your_email@example.com'
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
