from flask import render_template, request, redirect, url_for
import db_routing
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from db_routing import app, db
import os
import hashlib
from re import match

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return db_routing.get_user(id=user_id)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        userName = request.form['RegUserLogin']
        userPassw = request.form['RegUserPassw']
        if string_check(userName) and string_check(userPassw):
            print('попытка регистрации')
            if db_routing.add_user(userName, passw_hash(userPassw)):
                print(db_routing.get_user(username=userName))
                login_user(db_routing.get_user(username=userName))
                return redirect(url_for('workshop'))
    return render_template('registration.html')


@app.route('/login', methods=['POST'])
def login():
    userName = request.form['LogUserLogin']
    userPassw = request.form['LogUserPassw']
    if string_check(userName) and string_check(userPassw):
        user = verify_password(userName, userPassw)
        if user:
            login_user(user)
            return redirect(url_for('workshop'))
        else:
            return redirect(url_for('registration'))

    else:
        return redirect(url_for('registration'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/workshop', methods=['GET', 'POST'])
@login_required
def workshop():
    """
    if request.method == 'POST':
        if request.form['NewSceanrio']:

        if request.form['NewSceanrio']:

        if request.form['NewSceanrio']:
    """

    triggers_list = db_routing.get_trigers()
    actions_list = db_routing.get_actions()
    user_scripts_list = db_routing.get_user_scripts(current_user.get_id())
    return render_template('workshop.html', triggers_list=triggers_list, actions_list=actions_list,
                           user_scripts_list=user_scripts_list)


# @app.errorhandler(Exception)
# def universal_error(error):
#     return render_template('error.html'), 404


def string_check(string):
    if 2 < len(string) < 7:
        if match('^[0-9A-Za-z]*$', string) and not ('\\' in string):
            return True
    else:
        print(
            'Некорректный ввод! Строка должно включать только английские буквы или цифры. Содержать не менее 3 и не '
            'более 6 символов')
        return False


def passw_hash(user_passw, salt=os.urandom(32)):
    key = hashlib.pbkdf2_hmac('sha256', user_passw.encode('utf-8'), salt, 100000)
    storage = salt + key
    # salt_from_storage = storage[:32]  # 32 длина соли
    # key_from_storage = storage[32:]
    return storage


def verify_password(username, password):
    User = db_routing.get_user(username=username)
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
