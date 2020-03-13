from flask import Flask, render_template

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
