from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask('Jarvis', static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Users'
    UserID = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(80), unique=True, nullable=False)
    UserPassw = db.Column(db.String(120), nullable=False)


class Trigger(db.Model):
    __tablename__ = 'Triggers'
    TriggerID = db.Column(db.Integer, primary_key=True)
    TriggerName = db.Column(db.String(80), unique=True, nullable=False)
    TriggerArgs = db.Column(db.String(200))


class Action(db.Model):
    __tablename__ = 'Actions'
    ActionID = db.Column(db.Integer, primary_key=True)
    ActionName = db.Column(db.String(80), unique=True, nullable=False)
    ActionArgs = db.Column(db.String(200))


class Scenario(db.Model):
    __tablename__ = 'Scenarios'
    ScenarioID = db.Column(db.Integer, primary_key=True)
    ScenarioTrigger = db.Column(db.Integer, nullable=False)
    ScenarioAction = db.Column(db.Integer, nullable=False)


def add_user(user_name, passw_hash):
    if not find_user(user_name):
        new_user = User(UserName=user_name, UserPassw=passw_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    else:
        print('Логин занят')
        return False


def find_user(user_name):
    return User.query.filter_by(UserName=user_name).first()
