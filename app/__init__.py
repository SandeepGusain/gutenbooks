import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# get folder containing .env file and load environment variables
project_folder = os.getcwd()
load_dotenv(os.path.join(project_folder, '.env'))

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.views.views import mod_book as book_module

app.register_blueprint(book_module)