from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///market.db" 
db = SQLAlchemy(app)

#database
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    
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
    items = Item.query.all()
    return render_template("market.html",my_items=items)

@app.route("/login") 
def login_page():
    return render_template("login.html")

@app.route("/register") 
def register_page():
    return render_template("register.html")
