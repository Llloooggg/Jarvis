from flask import Flask, render_template, request
import db_routing
from flask_httpauth import HTTPBasicAuth
import os
import hashlib


app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


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
        if db_routing.add_user(userLogin, passw_hash(userPassw)):
            return render_template('content.html')
    return render_template('registration.html')


@auth.verify_password
def verify_password(user_login, user_passw):
    User = db_routing.find_user(user_login)
    if User:
        userSalt = User.UserPassw[:32]
        if passw_hash(user_passw, userSalt) == User.UserPassw:
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
    app.run()
