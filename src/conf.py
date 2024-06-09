import os
import secrets

SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'


class Config:
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config
