from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/root") #decorator 
def root_page():
    return "<h1>Hello, World!</h1>"

@app.route("/user")
def user_page():
    return "<h1>Hello, USER!</h1>"

@app.route("/about")
def about_page():
    return "<h1>Hello to about page!</h1>"

"""dynamic route"""

@app.route("/about/<user_name>")
def dynamic_about_page(user_name):
    return f"<h1>Hello about {user_name}!</h1>"

"""accessing index files"""
@app.route("/") 
def home_page():
    return render_template("home.html")

@app.route("/market") 
def market_page():
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
]
    return render_template("market.html",my_items=items)

@app.route("/login") 
def login_page():
    return render_template("login.html")

@app.route("/register") 
def register_page():
    return render_template("register.html")
