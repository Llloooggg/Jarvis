from flask import render_template, request, redirect
import db_routing
from flask_login import LoginManager, current_user, login_user, login_required
from db_routing import app, db
import os
import hashlib

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    userID = db_routing.find_user(id=user_id).UserID
    return userID


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userName = request.form['RegUserLogin']
        userPassw = request.form['RegUserPassw']
        if db_routing.add_user(userName, passw_hash(userPassw)):
            login_user(db_routing.find_user(username=userName))
            return redirect('content.html')
    return render_template('registration.html')


@app.route('/login', methods=['POST'])
def login():
    userName = request.form['LogUserLogin']
    userPassw = request.form['LogUserPassw']
    user = verify_password(userName, userPassw)
    if user:
        login_user(user)
        return render_template('content.html')


@app.route('/content', methods=['GET'])
@login_required
def content():
    return render_template('content.html')


# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404


def passw_hash(user_passw, salt=os.urandom(32)):
    key = hashlib.pbkdf2_hmac('sha256', user_passw.encode('utf-8'), salt, 100000)
    storage = salt + key
    # salt_from_storage = storage[:32]  # 32 длина соли
    # key_from_storage = storage[32:]
    return storage


def verify_password(username, password):
    User = db_routing.find_user(username=username)
    if User:
        userSalt = User.password[:32]
        if passw_hash(password, userSalt) == User.password:
            return User
    else:
        print('Неверный пароль')
        return False


if __name__ == '__main__':
    if not os.path.exists('./data.db'):
        db.create_all()
    app.run()
