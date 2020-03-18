from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import Flask

app = Flask('Jarvis', static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'Radius'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    telegram_username = db.Column(db.String(80), unique=True)

    def __init__(self, username, password, telegram_username=None):
        self.username = username
        self.password = password
        self.telegram_username = telegram_username

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.is_authenticated

    def get_id(self):
        return self.id


class Trigger(db.Model):
    __tablename__ = 'Triggers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def_name = db.Column(db.String(200))


class Action(db.Model):
    __tablename__ = 'Actions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def_name = db.Column(db.String(200))


class Scenario(db.Model):
    __tablename__ = 'Scenarios'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, ForeignKey('Users.id'))
    trigger_id = db.Column(db.Integer, ForeignKey('Triggers.id'))
    trigger_args = db.Column(db.String(200))
    action_id = db.Column(db.Integer, ForeignKey('Actions.id'))
    action_args = db.Column(db.String(200))


def add_user(user_name, passw_hash):
    if not get_user(user_name):
        new_user = User(username=user_name, password=passw_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    else:
        print('Логин занят')
        return False


def get_user(id=None, username=None):
    if id:
        return User.query.filter_by(id=id).first()
    if username:
        return User.query.filter_by(username=username).first()


def get_trigers():
    triggers_list = Trigger.query.all()
    return triggers_list


def get_actions():
    actions_list = Action.query.all()
    return actions_list


def get_user_scripts(current_user_id):
    user_scripts_list = Scenario.query.filter_by(owner_id=current_user_id).all()
    return user_scripts_list
