from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/stackoverflow'

db = SQLAlchemy(app)

class tag(db.Model):
	__tablename__ = 'tag'
	tag_id = db.Column('tag_id',db.Integer,primary_key=True)
	tag_name = db.Column('tag_name',db.String)

class user(db.Model):
	__tablename__ = 'user'
	user_id = db.Column('user_id',db.Integer,primary_key=True)
	email_id = db.Column('email_id',db.String)
	password = db.Column('password',db.String)
	first_name = db.Column('first_name',db.String)
	middle_name = db.Column('middle_name',db.String)
	last_name = db.Column('last_name',db.String)
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
	date_of_reg = db.Column('date_of_reg',db.DateTime)
	profile_pic = db.Column('profile_pic',db.String)

class que_tag(db.Model):
	__tablename__ = 'que_tag'
	tag_id = db.Column('tag_id',db.Integer,primary_key=True)
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class questions(db.Model):
	__tablename__ = 'questions'
	question_id = db.Column('question_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_content = db.Column('question_content',db.String)
	title = db.Column('title',db.String)
	votes = db.Column('votes',db.Integer)
	delete_votes = db.Column('delete_votes',db.Integer)
	que_date = db.Column('que_date',db.DateTime)
	views = db.Column('views',db.Integer)

class answer(db.Model):
	__tablename__ = 'answer'
	ans_id = db.Column('ans_id',db.Integer,primary_key=True)
	ans_content = db.Column('ans_content',db.String)
	votes = db.Column('votes',db.Integer)
	ans_date = db.Column('ans_date',db.DateTime)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class bookmark(db.Model):
	__tablename__ = 'bookmark'
	bookmark_id = db.Column('bookmark_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	question_id = db.Column(db.ForeignKey('questions.question_id'))

class comment(db.Model):
	__tablename__ = 'comment'
	comment_id = db.Column('comment_id',db.Integer,primary_key=True)
	user_id = db.Column(db.ForeignKey('user.user_id'))
	ans_id = db.Column(db.ForeignKey('answer.ans_id'))
	comment_content = db.Column('comment_content',db.String)
	comment_date = db.Column('comment_date',db.DateTime)

# class admin(db.Model):
# 	__tablename__ = 'bookmark'
# 	bookmark_id = db.Column('bookmark_id',db.Integer,primary_key=True)
# 	user_id = db.Column(ForeignKey('user.user_id'),db.Integer)
# 	question_id = db.Column(ForeignKey('questions.question_id'),db.Integer)
