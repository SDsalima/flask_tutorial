from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__)

bc= Bcrypt(app)

app.config["SECRET_KEY"] = (
    "7b5081f25289ba32128e3326472466f49f6a1b37ad18d5ab0b622cdc3337628f268e15210de0613a"
)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonic.db"

db = SQLAlchemy(app)
app.app_context().push()
migrat= Migrate(app, db)

login_manager= LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category='info'
from flask_app import routes
