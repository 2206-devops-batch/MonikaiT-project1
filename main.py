#!/usr/bin/env python3
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

@app.route('/')
def home_welcome():
	return '<h1>Welcome!</h1>'
	return '<h2>Ready to do?</h2.>'
@app.route('/budget/',  methods =["GET", "POST"])
def budget():
    return "<h1>Let's get budgeting!!</h1>"
def do_calculations(housing, savings, bills, transportation, food, misc):
	if request.method == "POST":
       # getting input with name = fname in HTML form
		checking = request.form.get("Checking: ")
		housing = request.form.get("Housing: ")
		savings = request.form.get("Savings: ")
		bills = request.form.get("Bills: ")
		transportation = request.form.get("Transportation: ")
		food = request.form.get("Food: ")
		misc = request.form.get("Misc: ")
	return housing + savings + bills + transportation + food + misc

@app.route('/about/')
def about():
    return '<h3>This is a Flask web application intended to work cohesively with a CI/CD pipeline.</h3>'


