from cart import Cart
from product import Product

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/products")
def products():
	return render_template("products.html")

@app.route("/mycart")
def cart():
	return render_template("cart.html")

@app.route("/billing")
def billing():
	return render_template("payments.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")	


app.run(debug=True)

