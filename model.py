from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/stackoverflow'

db = SQLAlchemy(app)

class tag(db.Model):
	__tablename__ = 'tag'
	tag_id = db.Column('tag_id',db.Integer,primary_key=True)
	tag_name = db.Column('tag_name',db.String(30),nullable=False)

class user(db.Model):
	__tablename__ = 'user'
	user_id = db.Column('user_id',db.Integer,primary_key=True)
	email_id = db.Column('email_id',db.String,nullable=False,unique=True)
	password = db.Column('password',db.String,nullable=False)
	first_name = db.Column('first_name',db.String,nullable=False)
	middle_name = db.Column('middle_name',db.String)
	last_name = db.Column('last_name',db.String,nullable=False)
	gender = db.Column('gender',db.String)
	mobile_no = db.Column('mobile_no',db.String)
	country = db.Column('country',db.String)
	state = db.Column('state',db.String)
	city = db.Column('city',db.String)
	current_position = db.Column('current_position',db.String)
	college = db.Column('college',db.String)
	date_of_birth = db.Column('date_of_birth',db.DateTime)
	up_votes = db.Column('up_votes',db.Integer)
	down_votes = db.Column('down_votes',db.Integer)
	date_of_reg = db.Column('date_of_reg',db.DateTime,nullable=False)
	profile_pic = db.Column('profile_pic',db.String)

class que_tag(db.Model):
	__tablename__ = 'que_tag'
	que_tag_id = db.Column('que_tag_id',db.Integer,primary_key=True)
	tag_id = db.Column(db.ForeignKey('tag.tag_id'))
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class questions(db.Model):
	__tablename__ = 'questions'
	question_id = db.Column('question_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_content = db.Column('question_content',db.String,nullable=False)
	title = db.Column('title',db.String,nullable=False)
	votes = db.Column('votes',db.Integer)
	delete_votes = db.Column('delete_votes',db.Integer)
	que_date = db.Column('que_date',db.DateTime,nullable=False)
	views = db.Column('views',db.Integer)

class answer(db.Model):
	__tablename__ = 'answer'
	ans_id = db.Column('ans_id',db.Integer,primary_key=True)
	ans_content = db.Column('ans_content',db.String,nullable=False)
	votes = db.Column('votes',db.Integer)
	ans_date = db.Column('ans_date',db.DateTime,nullable=False)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class bookmark(db.Model):
	__tablename__ = 'bookmark'
	bookmark_id = db.Column('bookmark_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class answer_later(db.Model):
	__tablename__ = 'answer_later'
	later_id = db.Column('later_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class comment(db.Model):
	__tablename__ = 'comment'
	comment_id = db.Column('comment_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	ans_id = db.Column(db.ForeignKey('answer.ans_id'))
	comment_content = db.Column('comment_content',db.String,nullable=False)
	comment_date = db.Column('comment_date',db.DateTime,nullable=False)

class admin(db.Model):
	__tablename__ = 'admin'
	admin_id = db.Column('admin_id',db.Integer,primary_key=True)
	first_name = db.Column('first_name',db.String,nullable=False)
	middle_name = db.Column('middle_name',db.String)
	last_name = db.Column('last_name',db.String,nullable=False)
	email_id = db.Column('email_id',db.String,nullable=False,unique=True)
	password = db.Column('password',db.String,nullable=False)
	country = db.Column('country',db.String)
	state = db.Column('state',db.String)
	city = db.Column('city',db.String)
	mobile_no = db.Column('mobile_no',db.String)
	gender = db.Column('gender',db.String)
	date_of_birth = db.Column('date_of_birth',db.DateTime)
	date_of_reg = db.Column('date_of_reg',db.DateTime,nullable=False)
	profile_pic = db.Column('profile_pic',db.String)



# tg = tag.query.all() # Retrieve all data
# 	ll = [{'id':1,'name':"sad"}]
# 	del ll[:]
# 	for i in tg:
# 		ll.append({'id':i.tag_id,'name':i.tag_name})
	
# 	For select particular record
# 	tg = tag.query.filter_by(tag_id=1).first()
# 	For insertion
# 	tg = tag(tag_name="DEF")
# 	db.session.add(tg)
# 	db.session.commit()
# 	For deletion
# 	db.session.delete(tg)
# 	db.session.commit()