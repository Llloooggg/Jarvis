from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/registration", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        UserLogin = request.form['login']
        UserPass = request.form['password']

        #db.session.add(UserLogin, UserPass)
        #db.session.commit()

        #return redirect(url_for(""))

        print(UserLogin, ' ', UserPass)

    return render_template("registration.html")


# @app.route('/login', methods=['GET'])
# def login():
#    return render_template('login.html')


if __name__ == "__main__":
    app.run()
