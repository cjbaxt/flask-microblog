"""
Initialising the app module.

Notes:
-import Flask class from flask
-define app variable which is instance of class Flask
-import routes (adding import at end of file fixes circular import problems)
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes