from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy
import os
import hashlib
import sqlite3

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/registraion', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        UserLogin = request.form['UserLogin']
        UserPass = request.form['UserPass']
        if not find_user_copy(UserLogin):
            db.session.add(UserLogin, passw_hash(UserPass))
            db.session.commit()
    return render_template('registration.html')


@app.route('/content', methods=['GET'])
def content():
    return render_template('content.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


def find_user_copy(user_login):
    con = sqlite3.connect('data.db')
    with con:
        cur = con.cursor()
        exist = cur.execute('SELECT EXISTS ( SELECT UserLogin FROM Users Where UserLogin = ' + user_login + ' LIMIT 1')
    return exist


def passw_hash(user_passw):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', user_passw.encode('utf-8'), salt, 100000)
    storage = salt + key
    # salt_from_storage = storage[:32]  # 32 длина соли
    # key_from_storage = storage[32:]
    return storage

# @app.route('/login', methods=['GET'])
# def login():
#    return render_template('login.html')


if __name__ == '__main__':
    app.run()
