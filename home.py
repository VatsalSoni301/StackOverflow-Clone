from flask import Flask
from flask import render_template,request,redirect,url_for,session,flash,jsonify

from model import *
from datetime import datetime
import os

@app.route("/")
def index():
	return render_template('index.html',name="xyz")

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

@app.route("/ask_question")
def ask_question():
	return render_template('ask_question.html')

@app.route("/ask_question_1",methods=['POST'])
def ask_question_1():
	title = request.form['title']
	sn = request.form['editordata']
	tag1 = request.form['tag_1']
	tag2 = request.form['tag_2']
	tag3 = request.form['tag_3']
	tag4 = request.form['tag_4']
	tag5 = request.form['tag_5']
	date_of_question = datetime.utcnow()
	tagid1 = None
	tagid2 = None
	tagid3 = None
	tagid4 = None
	tagid5 = None

	tg = tag.query.filter_by(tag_name=tag1).first()
	if tg==None:
		tg = tag(tag_name=tag1)
		db.session.add(tg)
		db.session.commit()
		tagid1=tg.tag_id
	else:
		tagid1=tg.tag_id

	if tag2!=None or tag2!="":
		tg = tag.query.filter_by(tag_name=tag2).first()
		if tg==None: 
			tg = tag(tag_name=tag2)
			db.session.add(tg)
			db.session.commit()
			tagid2=tg.tag_id
		else:
			tagid2=tg.tag_id

	if tag3!=None or tag3!="":
		tg = tag.query.filter_by(tag_name=tag3).first()
		if tg==None :
			tg = tag(tag_name=tag3)
			if tg.tag_name!="":
				db.session.add(tg)
				db.session.commit()
				tagid3=tg.tag_id
		else:
			tagid3=tg.tag_id

	if tag4!=None or tag4!="":
		tg = tag.query.filter_by(tag_name=tag4).first()
		if tg==None:
			tg = tag(tag_name=tag4)
			if tg.tag_name!="":
				db.session.add(tg)
				db.session.commit()
				tagid4=tg.tag_id
		else:
			tagid4=tg.tag_id

	if tag5!=None or tag5!="":
		tg = tag.query.filter_by(tag_name=tag5).first()
		if tg==None:
			tg = tag(tag_name=tag5)
			if tg.tag_name!="":
				db.session.add(tg)
				db.session.commit()
				tagid5=tg.tag_id
		else:
			tagid5=tg.tag_id


	que=questions(user_id=1,question_content=sn,title=title,votes=0,delete_votes=0,views=0,que_date=date_of_question)
	db.session.add(que)
	db.session.commit()
	qid = que.question_id 

	if tagid1!=None and tagid1!="":
		qt = que_tag(tag_id=tagid1,question_id=qid)
		db.session.add(qt)
		db.session.commit()

	if tagid2!=None  and tagid2!="":
		qt = que_tag(tag_id=tagid2,question_id=qid)
		db.session.add(qt)
		db.session.commit()

	if tagid3!=None and tagid3!="":
		qt = que_tag(tag_id=tagid3,question_id=qid)
		db.session.add(qt)
		db.session.commit()

	if tagid4!=None and tagid4!="":
		qt = que_tag(tag_id=tagid4,question_id=qid)
		db.session.add(qt)
		db.session.commit()

	if tagid5!=None and tagid5!="":
		qt = que_tag(tag_id=tagid5,question_id=qid)
		db.session.add(qt)
		db.session.commit()

	return render_template('index.html')


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