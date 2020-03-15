from flask import render_template, request
from db_routing import app
import db_routing
from flask_httpauth import HTTPBasicAuth
import os
import hashlib


if not os.path.exists('./data.db'):
    db_routing.db.create_all()
auth = HTTPBasicAuth()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        userLogin = request.form['UserLogin']
        userPassw = request.form['UserPassw']
        db_routing.add_user(userLogin, passw_hash(userPassw))
    else:
        print('Логин занят')
    return render_template('registration.html')


@auth.verify_password
def verify_password(user_login, user_passw):
    user = db_routing.find_user(user_login)
    if user:
        userSalt = user[2][:32]
        if passw_hash(user_passw, userSalt) == user[2]:
            return True
    else:
        return False


@app.route('/content', methods=['GET'])
@auth.login_required
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


if __name__ == '__main__':
    db_routing.app.run()
