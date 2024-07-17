from flask import Flask


app = Flask(__name__)  # Flask("main.py")


@app.route("/")
def hello_world():
    return "<p>Hello world</p>"


@app.route("/about")
def about_page():
    return "<p>About page</p>"


