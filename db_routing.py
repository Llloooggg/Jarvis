from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask("Jarvis", static_folder="static", template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "Radius"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    tg_id = db.Column(db.String(80), unique=True)

    def __init__(self, username, password, tg_username=None):
        self.username = username
        self.password = password
        self.tg_username = tg_username

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.is_authenticated

    def get_id(self):
        return self.id

    def get_tg_id(self):
        return self.tg_id


class Trigger(db.Model):
    __tablename__ = "Triggers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def_name = db.Column(db.String(200))


class Action(db.Model):
    __tablename__ = "Actions"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def_name = db.Column(db.String(200))


class Scenario(db.Model):
    __tablename__ = "Scenarios"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, ForeignKey("Users.id"))
    scenario_name = db.Column(db.String(80), nullable=False)
    trigger_id = db.Column(db.Integer, ForeignKey("Triggers.id"))
    trigger_args = db.Column(db.String(200))
    action_id = db.Column(db.Integer, ForeignKey("Actions.id"))
    action_args = db.Column(db.String(200))


def add_user(user_name, passw_hash):
    if not get_user(username=user_name):
        new_user = User(username=user_name, password=passw_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    else:
        print("Логин занят")
        return False


def add_trigger(name, def_name):
    new_trigger = Trigger(name=name, def_name=def_name)
    db.session.add(new_trigger)
    db.session.commit()
    return new_trigger


def add_action(name, def_name):
    new_action = Action(name=name, def_name=def_name)
    db.session.add(new_action)
    db.session.commit()
    return new_action


def add_scenario(
    owner_id, scenario_name, trigger_id, trigger_args, action_id, action_args
):
    new_scenario = Scenario(
        owner_id=owner_id,
        scenario_name=scenario_name,
        trigger_id=trigger_id,
        trigger_args=trigger_args,
        action_id=action_id,
        action_args=action_args,
    )
    db.session.add(new_scenario)
    db.session.commit()
    return new_scenario


def get_user(id=None, username=None):
    if id:
        return User.query.filter_by(id=id).first()
    if username:
        return User.query.filter_by(username=username).first()


def get_trigers(id=None):
    if id is None:
        triggers_list = Trigger.query.all()
        return triggers_list
    else:
        trigger = Trigger.query.filter_by(id=id).first()
        return trigger


def get_actions(id=None):
    if id is None:
        actions_list = Action.query.all()
        return actions_list
    else:
        action = Action.query.filter_by(id=id).first()
        return action


def get_user_scripts(current_user_id):
    user_scripts_list = Scenario.query.filter_by(
        owner_id=current_user_id
    ).all()
    return user_scripts_list


def delete_scenario(scenario_id):
    scenario = Scenario.query.filter_by(id=scenario_id).first()
    db.session.delete(scenario)
    db.session.commit()


def tg_id_update(current_user_id, new_tg_username):
    current_user = User.query.filter_by(id=current_user_id).first()
    current_user.tg_id = new_tg_username
    db.session.commit()
