from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():  # redirect to
    return "<h2>This is the home page</h2>"


@app.route("/admin")
def admin():
    return redirect(url_for("home"))  # string the function


if __name__ == "__main__":
    app.run()
