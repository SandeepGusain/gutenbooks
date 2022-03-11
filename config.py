import os


class Config:
    """
        Stores the configurations such as Database URI, Secret Key
        Generate a random string using [openssl rand -base64 32]
    """
    SECRET_KEY = 'B8M4BNUc7HeYdRacuvWWCe42Kx7XxIcPdyK/5VtiigI='
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(Config):
    """
        Stores the settings related to Flask dev. server
    """
    DEVELOPMENT = True
    DEBUG = True
