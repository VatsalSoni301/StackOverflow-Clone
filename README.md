# Stackoverflow
This repository contains code for clone of Stackoverflow site made using 
* Python Flask 
* MySQL as database
* SQLAlchemy for ORM
* HTML, CSS and Bootstrap for frontend

## Prerequisites

```
sudo apt install python2.7 python-pip
pip install Flask
pip install flask-mysql
pip install flask-sqlalchemy
pip install PyMySQL
```
## Database setup
* install and setup mysql ([click here](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-18-04))
* mysql username and password should be set to 'root'
* use data.sql to import the schema, tables and data

## Steps to run
* python home.py (from the directory of this project)
* open localhost in browser to see the website

## Features supported
* Ask question (with summernote editor)
* Answers (with summernote editor), comments to questions
* Upvote, downvote to questions and answers
* Save questions to Answer Later
* Bookmark answer
* Search questions by tag, title
* List of questions of a particular tag when clicked on it
* View and edit profile
