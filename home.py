from flask import Flask
from flask import render_template,request,redirect,url_for,session,flash,jsonify

from model import *

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/user_sign_in")
def user_signin():
	email = request.form['email']
	password = request.form['password']
	usr = user.query.filter_by(email_id=email,password=password).first()
	if user is NULL:
		pass
	else:
		return render_template('index.html')

@app.route("/user_sign_up")
def user_signup():
	return render_template('user_sign_up.html')

@app.route("/user_sign_up_1",methods=['POST'])
def user_signup_1():
	email = request.form['email']
	password = request.form['password']
	first = request.form['fname']
	middle = request.form['mname']
	last = request.form['lname']
	gender = request.form['gn']
	mobile = request.form['mobile']
	country = request.form['country']
	current_pos = request.form['cur_pos']
	college = request.form['collegename']
	dob = request.form['date']
	dd=datetime.utcnow()

	for f in request.files.getlist("file"):
		if f.filename=='':
			destination='Default.jpg'
		else:
			target=os.path.join('/home/vatsal/Documents/IIIT/SCE_Assignments/SCE_Project/static','Img/')
			filename=f.filename
			ext=filename.split(".")
			destination = "/".join([target,filename])
			f.save(destination)
			destination=filename

	usr = user(first_name=first,middle_name=middle,last_name=last,email_id=email,password=password,gender=gender,mobile_no=mobile,country=country,current_position=current_pos,college=college,date_of_birth=dob,date_of_reg=dd,profile_pic=destination)
	db.session.add(usr)
	db.session.commit()
	return redirect(url_for('.user_signup'))
	
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