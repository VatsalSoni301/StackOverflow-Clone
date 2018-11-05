from flask import Flask
from flask import render_template,request,redirect,url_for,session,flash,jsonify

from model import *
from datetime import datetime
import os
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def index():
	if 'uid' not in session:
		set_questions_obj = questions.query.all()
		set_questions = [{}]
		del set_questions[:]
		for item in set_questions_obj:
			tg_id = que_tag.query.filter_by(question_id=item.question_id)
			tagName = [{}]
			del tagName[:]
			for it in tg_id:
				tgNameObj=tag.query.filter_by(tag_id=it.tag_id).first()
				tagName.append({'id':tgNameObj.tag_id,'name':tgNameObj.tag_name})
			usr = user.query.filter_by(user_id = item.user_id).first()
			# book = bookmark.query.filter_by(user_id = cur_id,question_id=item.question_id).first()
			# if book == "None":
			# 	bool_bid=0
			# else:
			# 	bool_bid=1
			ans = answer.query.filter_by(question_id=item.question_id)
			ans_count=0
			for answer_que in ans:
				ans_count=ans_count+1
			# ans_lat = answer_later.query.filter_by(question_id=item.question_id,user_id=cur_id)
			# if ans_lat == "None":
			# 	bool_ans_lat=0
			# else:
			# 	bool_ans_lat=1
			# ans = answer.query.filter_by(question_id=item.question_id,user_id=cur_id)
			# if ans == "None":
			# 	bool_ans=0
			# else:
			# 	bool_ans=1
			set_questions.append({'id':item.question_id,'title':item.title,'votes':item.votes,\
			'views':item.views,'date':item.que_date,'fname':usr.first_name,'lname':usr.last_name,\
			'tags':tagName,'uid':0,'ans':ans_count,'BID':0,'ans_later':0,'answered':0})
		return render_template('index.html',name="#",questionList=set_questions,uuid=0)
	else:
		cur_id = session['uid']
		set_questions_obj = questions.query.all()
		set_questions = [{}]
		del set_questions[:]
		for item in set_questions_obj:
			tg_id = que_tag.query.filter_by(question_id=item.question_id)
			tagName = [{}]
			for it in tg_id:
				tgNameObj=tag.query.filter_by(tag_id=it.tag_id).first()
				tagName.append({'id':tgNameObj.tag_id,'name':tgNameObj.tag_name})
			usr = user.query.filter_by(user_id = item.user_id).first()
			book = bookmark.query.filter_by(user_id = cur_id,question_id=item.question_id).first()
			if book is None:
				bool_bid=0
			else:
				bool_bid=1
			ans = answer.query.filter_by(question_id=item.question_id)
			ans_count=0	# need to  check
			for answer_que in ans:
				ans_count=ans_count+1
			ans_lat = answer_later.query.filter_by(question_id=item.question_id,user_id=cur_id).first()
			if ans_lat is None:
				bool_ans_lat=0
			else:
				bool_ans_lat=1
			ans = answer.query.filter_by(question_id=item.question_id,user_id=cur_id).first()
			if ans is None:
				bool_ans=0
			else:
				bool_ans=1
			set_questions.append({'id':item.question_id,'title':item.title,'votes':item.votes,\
			'views':item.views,'date':item.que_date,'fname':usr.first_name,'lname':usr.last_name,\
			'tags':tagName,'uid':item.user_id,'ans':ans_count,'BID':bool_bid,'ans_later':bool_ans_lat,'answered':bool_ans})
		return render_template('index.html',name=session['fname'],questionList=set_questions,uuid=cur_id)


@app.route("/add_answer_later_1",methods=['POST'])
def add_answer_later_1():
	usr = request.form['usr']
	que = request.form['que']
	ans_l = answer_later(user_id=usr,question_id=que)
	#answer_later.query.filter(User.id == 123).delete()
	db.session.add(ans_l)
	db.session.commit()
	return "success"

@app.route("/rm_answer_later_1",methods=['POST'])
def rm_answer_later_1():
	usr = request.form['usr']
	que = request.form['que']
	# ans_l = answer_later(user_id=usr,question_id=que)
	# db.session.delete(ans_l)
	answer_later.query.filter_by(question_id=que,user_id=usr).delete()
	db.session.commit()
	return "success"

@app.route("/add_bookmark_1",methods=['POST'])
def add_bookmark_1():
	usr = request.form['usr']
	que = request.form['que']
	bk = bookmark(user_id=usr,question_id=que)
	db.session.add(bk)
	db.session.commit()
	return "success"

@app.route("/rm_bookmark_1",methods=['POST'])
def rm_bookmark_1():
	usr = request.form['usr']
	que = request.form['que']
	# bk = bookmark(user_id=usr,question_id=que)
	# db.session.delete(bk)
	bookmark.query.filter_by(question_id=que,user_id=usr).delete()
	db.session.commit()
	return "success"

@app.route("/user_sign_in_1",methods=['POST'])
def user_sign_in_1():
	email = request.form['email']
	password = request.form['password']
	usr = user.query.filter_by(email_id=email,password=password).first()
	if usr is None:
		return "wrong"
	else:
		session['uid'] = usr.user_id
		session['fname'] = usr.first_name
		return "success"

@app.route("/user_sign_in",methods=['POST'])
def user_sign_in():
	return redirect(url_for('.index'))

@app.route("/user_sign_up")
def user_sign_up():
	cn = country.query.all()
	con = [{}]
	del con[:]
	for i in cn:
		con.append({'id':i.country_id,'name':i.country_name})
	return render_template('user_sign_up.html',name="#",country=con)

@app.route('/signout_user')
def signout_user():
		session.pop('uid', None)
		session.pop('fname', None)
		return redirect(url_for('.index'))

@app.route("/view_profile")
def view_profile():
	uid= request.args.get('uid', default='', type=str)
	usr = user.query.filter_by(user_id=uid).first()
	con = country.query.filter_by(country_id=usr.country_id).first()
	user_dict={'fname':usr.first_name,'lname':usr.last_name,'email':usr.email_id,\
	'country':con.country_name,'current':usr.current_position,'college':usr.college,\
	'date':usr.date_of_birth,'pic':usr.profile_pic,'gn':usr.gender}

	ques_obj = questions.query.filter_by(user_id=uid)
	ques_set = [{}]
	del ques_set[:]
	for item in ques_obj:
		ques_set.append({'id':item.question_id,'title':item.title})

	ans_obj = answer.query.filter_by(user_id=uid)
	ques_ans_set = [{}]
	del ques_ans_set[:]
	for item in ans_obj:
		que_detail = questions.query.filter_by(question_id=item.question_id).first()
		ques_ans_set.append({'title':que_detail.title,'id':que_detail.question_id})
	
	return render_template('view_profile.html',name=session['fname'],usr_dict=user_dict,qset=ques_set,ansset=ques_ans_set)

@app.route("/user_sign_up_1",methods=['POST'])
def user_sign_up_1():

	email = request.form['email']
	password = request.form['password']
	first = request.form['fname']
	middle = request.form['mname']
	last = request.form['lname']
	gender = request.form['gn']
	mobile = request.form['mobile']
	country = int(request.form['country'])
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
	
	usr = user(first_name=first,middle_name=middle,last_name=last,email_id=email,password=password,gender=gender,mobile_no=mobile,country_id=country,current_position=current_pos,college=college,date_of_birth=dob,date_of_reg=dd,profile_pic=destination)
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
def admin_login():
	return render_template('admin_login.html')

@app.route("/Bookmark")
def Bookmark():
	if 'uid' not in session:
		pass
	else:
		bookmark_objs = bookmark.query.filter_by(user_id = session['uid'])
		que_set = []
		set_questions=[]
		for bookmark_obj in bookmark_objs:
			b_que_id = bookmark_obj.question_id
			ques = questions.query.filter_by(question_id = b_que_id ).first()
			que_set.append(ques)
		cur_id = session['uid']
		
		print que_set

		for item in que_set:
			print type(item)
			tg_id = que_tag.query.filter_by(question_id=item.question_id)
			tagName = [{}]
			for it in tg_id:
				tgNameObj=tag.query.filter_by(tag_id=it.tag_id).first()
				tagName.append({'id':tgNameObj.tag_id,'name':tgNameObj.tag_name})
			usr = user.query.filter_by(user_id = item.user_id).first()
			book = bookmark.query.filter_by(user_id = cur_id,question_id=item.question_id).first()
			if book is None:
				bool_bid=0
			else:
				bool_bid=1
			ans = answer.query.filter_by(question_id=item.question_id)
			ans_count=0	# need to  check
			for answer_que in ans:
				ans_count=ans_count+1
			ans_lat = answer_later.query.filter_by(question_id=item.question_id,user_id=cur_id).first()
			if ans_lat is None:
				bool_ans_lat=0
			else:
				bool_ans_lat=1
			ans = answer.query.filter_by(question_id=item.question_id,user_id=cur_id).first()
			if ans is None:
				bool_ans=0
			else:
				bool_ans=1
			set_questions.append({'id':item.question_id,'title':item.title,'votes':item.votes,\
			'views':item.views,'date':item.que_date,'fname':usr.first_name,'lname':usr.last_name,\
			'tags':tagName,'uid':item.user_id,'ans':ans_count,'BID':bool_bid,'ans_later':bool_ans_lat,'answered':bool_ans})
		return render_template('bookmark.html',name=session['fname'],questionList=set_questions,uuid=session['uid'])	

@app.route("/admin")
def admin():
	cu_obj = contact_us.query.filter_by(cu_resolve=0)
	cu_dict=[{}]
	del cu_dict[:]
	for i in cu_obj:
		cu_dict.append({ 
			'name':i.cu_name,
			'email':i.cu_email_id,
			'mobile':i.cu_mobile_no,
			'message':i.cu_msg
			} ) 

	return render_template('admin.html', contact_us_dict = cu_dict)

@app.route("/que_page")
def que_page():
	if 'uid' not in session:
		cur_id=0
	else:
		cur_id = session['uid']
	qid = request.args.get('qid', default='', type=str)
	qobj = questions.query.filter_by(question_id=qid).first()
	usr = user.query.filter_by(user_id=qobj.user_id).first()
	tags = que_tag.query.filter_by(question_id=qid)
	tglist = [{}]
	del tglist[:]
	for tg in tags:
		tname = tag.query.filter_by(tag_id=tg.tag_id).first()
		tglist.append({'id':tg.tag_id,'name':tname.tag_name})
	quedict = {'id':qid,'title':qobj.title,'question_content':qobj.question_content,'votes':\
	qobj.votes,'date':qobj.que_date,'views':qobj.views,'uid':usr.user_id,'ufname':usr.first_name,\
	'ulname':usr.last_name,'tag':tglist}
	
	chk=0
	ansobj = answer.query.filter_by(question_id=qid)
	anslist=[{}]
	del anslist[:]
	for item in ansobj:
		if item.user_id == cur_id:
			chk=1
		usr = user.query.filter_by(user_id=item.user_id).first()
		commentlist = [{}]
		del commentlist[:]
		cmnt = comment.query.filter_by(ans_id=item.ans_id)
		for cmntitem in cmnt:
			usr_1 = user.query.filter_by(user_id=cmntitem.user_id).first()
			commentlist.append({'id':cmntitem.comment_id,'content':cmntitem.comment_content,\
			'uid':usr_1.user_id,'ufname':usr_1.first_name,'ulname':usr_1.last_name,'date':\
			cmntitem.comment_date})
		anslist.append({'a_id':item.ans_id,'content':item.ans_content,'date':item.ans_date,\
		'votes':item.votes,'uid':item.user_id,'ufname':usr.first_name,'ulname':usr.last_name\
		,'comments':commentlist})

	if 'uid' not in session:
		return render_template('que_page.html',name="#",uid=cur_id,qid=qid,quedict=quedict,anslist=anslist)
	else:
		return render_template('que_page.html',name=session['fname'],uid=cur_id,qid=qid,quedict=quedict,anslist=anslist,chkbtn=chk)

@app.route("/ask_question")
def ask_question():
	if 'uid' not in session:
		return render_template('ask_question.html',name="#")
	else:
		return render_template('ask_question.html',name=session['fname'])

@app.route("/ask_question_1",methods=['POST'])
def ask_question_1():
	cur_id = session['uid']
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
			if tg.tag_name!="":
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


	que=questions(user_id=cur_id,question_content=sn,title=title,votes=0,delete_votes=0,views=0,que_date=date_of_question)
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

	return redirect(url_for('.index'))

@app.route("/todo")
def todo():
	if 'uid' not in session:
		pass
	else:
		return render_template('todo.html',name=session['fname'])

@app.route("/about_us")
def about_us():
	if 'uid' not in session:
		return render_template('about_us.html',name="#")
	else:
		return render_template('about_us.html',name=session['fname'])

@app.route("/contact_us")
def contact():
	if 'uid' not in session:
		return render_template('contact_us.html',name="#")	
	else:
		return render_template('contact_us.html',name=session['fname'])

@app.route("/contact_us_1",methods=['POST'])
def contact_us_1():
	name = request.form['name']
	email = request.form['email_ct']
	mobile = request.form['mobile']
	message = request.form['message']

	cu=contact_us(cu_name=name,cu_email_id=email,cu_mobile_no=mobile,cu_msg=message)
	db.session.add(cu)
	db.session.commit()
	return redirect(url_for('.index'))

@app.route("/post_answer",methods=['POST'])
def post_answer():
	cur_id = session['uid']
	ans_content = request.form['editordata']
	qid = request.form['qid']
	ans_date = datetime.utcnow()
	ans = answer(ans_content=ans_content,votes=0,user_id=cur_id,question_id=qid,ans_date=ans_date) 
	db.session.add(ans)
	db.session.commit()
	return redirect(url_for('.que_page',qid=qid))

@app.route("/post_comment_1",methods=['POST'])
def post_comment_1():
	uid=session['uid']
	aid = request.form['ans__id']
	qid = request.form['que__id']
	comment_content = request.form['commentbox']
	cmnt_date = datetime.utcnow()
	cmnt = comment(user_id=uid,ans_id=aid,comment_content=comment_content,comment_date=cmnt_date)
	db.session.add(cmnt)
	db.session.commit()
	return redirect(url_for('.que_page',qid=qid))

if __name__=='__main__':
	app.run(port=5000,debug=True,threaded=True,host="127.0.0.1")