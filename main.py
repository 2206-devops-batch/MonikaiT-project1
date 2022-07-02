#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def calculate():
	budget = ''
	if request.method=='POST' and 'checking' in request.form and 'housing' in request.form and 'savings' in request.form and 'transportation' in request.form and 'bills' in request.form and 'food' in request.form and 'misc' in request.form:
		c = float(request.form.get('checking'))
		h = float(request.form.get('housing'))
		s = float(request.form.get('savings'))
		t = float(request.form.get('transportation'))
		b = float(request.form.get('bills'))
		f = float(request.form.get('food'))
		m = float(request.form.get('misc'))
		budget = round(c+h+s+t+b+f+m)	
	return render_template('index.html', budget=budget)
	
@app.route('/about/')
def about():
    return '<h3>This is a Flask web application intended to work cohesively with a CI/CD pipeline.</h3>'


