from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.users.dao.user import User

app = Flask(__name__)
app. config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main_base.db"

db = SQLAlchemy(app)

users_blueprint = Blueprint('users_blueprint', __name__)

User()

db.create_all()













