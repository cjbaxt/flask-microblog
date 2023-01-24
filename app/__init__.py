"""
Initialising the app module.

Notes:
-import Flask class from flask
-define app variable which is instance of class Flask
-import routes (adding import at end of file fixes circular import problems)
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models