import os
import secrets


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///traffic_infraction_tracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = Config
