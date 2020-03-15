from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    UserPassw = db.Column(db.String(120), nullable=False)


def add_user(user_name, passw_hash):
    if not find_user(user_name):
        new_user = User(UserName=user_name, UserPassw=passw_hash)
        db.session.add(new_user)
        db.session.commit()
    else:
        print('Логин занят')


def find_user(user_name):
    return User.query.filter_by(UserName=user_name).first()
