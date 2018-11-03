from flask import Flask
from flask import render_template,request,redirect,url_for,session,flash,jsonify

from model import *
from datetime import datetime
import os

@app.route("/")
def index():
	set_questions_obj = questions.query.all()
	set_questions = [{}]
	for item in set_questions_obj:
		tg_id = que_tag.query.filter_by(question_id=item.question_id)
		tagName = []
		for it in tg_id:
			tgNameObj=tag.query.filter_by(tag_id=it.tag_id).first()
			tagName.append(tgNameObj.tag_name)
		usr = user.query.filter_by(user_id = item.user_id).first()
		#book = bookmark.query.filter_by(user_id = id,question_id=item.question_id).first()
		set_questions.append({'id':item.question_id,'title':item.title,'votes':item.votes,\
		'views':item.views,'date':item.que_date,'fname':usr.first_name,'lname':usr.last_name,\
		'tags':tagName,'BID':1})
	return render_template('index.html',name="xyz",questionList=set_questions)

@app.route("/user_sign_in_1",methods=['POST'])
def user_sign_in_1():
	email = request.form['email']
	password = request.form['password']
	usr = user.query.filter_by(email_id=email,password=password).first()
	if usr:
		return "success"
	else:
		return "wrong"

@app.route("/user_sign_in",methods=['POST'])
def user_sign_in():
	return render_template('index.html')

@app.route("/user_sign_up")
def user_sign_up():
	return render_template('user_sign_up.html')

@app.route("/user_sign_up_1",methods=['POST'])
def user_sign_up_1():

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
	destination='Default.jpg'
	for f in request.files.getlist("file"):
		if f.filename=='':
			break
		else:
			
			target=os.path.join('/home/vatsal/Documents/IIIT/SCE_Assignemnts/SCE_Project/static','Img/')
			filename=f.filename
			ext=filename.split(".")
			destination = "/".join([target,filename])
			f.save(destination)
			destination=filename
	
	usr = user(first_name=first,middle_name=middle,last_name=last,email_id=email,password=password,gender=gender,mobile_no=mobile,country=country,current_position=current_pos,college=college,date_of_birth=dob,date_of_reg=dd,profile_pic=destination)
	db.session.add(usr)
	db.session.commit()
	return redirect(url_for('.index'))

@app.route('/validate_email_user',methods=['POST'])
def validate_email_user():

		x=0
		email = request.form['email']
		usr = user.query.all()
		for data in usr:
			if data.email_id == email:
				x=1
		
		if x==1:
			return "wrong"
		else:
			return "success"

@app.route("/admin_login")
def admin():
	return render_template('admin_login.html')

@app.route("/bookmark")
def bookmark():
	return render_template('bookmark.html')

@app.route("/que_page")
def que_page():
	return render_template('que_page.html')

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