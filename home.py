from flask import Flask
from flask import render_template,request,redirect,url_for,session,flash,jsonify

from model import *

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/user_sign_up")
def signup():
	return render_template('user_sign_up.html')

@app.route("/admin_login")
def admin():
	return render_template('admin_login.html')

@app.route("/bookmark")
def bookmark():
	return render_template('bookmark.html')

@app.route("/ask_question")
def ask_question():
	return render_template('ask_question.html')

@app.route("/todo")
def todo():
	return render_template('todo.html')

@app.route("/about_us")
def about_us():
	return render_template('about_us.html')

@app.route("/contact_us")
def contact():
	return render_template('contact_us.html')

if __name__=='__main__':
	app.run(port=5000,debug=True,threaded=True,host="127.0.0.1")