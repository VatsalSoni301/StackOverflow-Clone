#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request, redirect, url_for, session, \
    flash, jsonify

from model import *
from datetime import datetime
import os
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def index():
    try:
        set_questions_obj = questions.query.all()
        if 'uid' not in session:
            set_questions = getQuestionDict(set_questions_obj, True)
            return render_template('index.html', name='#',
                                   questionList=set_questions, uuid=0)
        else:
            cur_id = session['uid']
            set_questions = getQuestionDict(set_questions_obj, False)
            return render_template('index.html', name=session['fname'],
                                   questionList=set_questions,
                                   uuid=cur_id)
    except :
        return render_template('error.html')


@app.route('/add_answer_later_1', methods=['POST'])
def add_answer_later_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        ans_l = answer_later(user_id=usr, question_id=que)
        db.session.add(ans_l)
        db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/rm_answer_later_1', methods=['POST'])
def rm_answer_later_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        answer_later.query.filter_by(question_id=que,
                user_id=usr).delete()
        db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/add_bookmark_1', methods=['POST'])
def add_bookmark_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        bk = bookmark(user_id=usr, question_id=que)
        db.session.add(bk)
        db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/rm_bookmark_1', methods=['POST'])
def rm_bookmark_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        bookmark.query.filter_by(question_id=que, user_id=usr).delete()
        db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/user_sign_in_1', methods=['POST'])
def user_sign_in_1():
    try:
        email = request.form['email']
        password = request.form['password']
        usr = user.query.filter_by(email_id=email,
                                   password=password).first()
        if usr is None:
            return 'wrong'
        else:
            session['uid'] = usr.user_id
            session['fname'] = usr.first_name
            return 'success'
    except :
        return render_template('error.html')


@app.route('/upvote_que_1', methods=['POST'])
def upvote_que_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        queobj = user_que_vote.query.filter_by(user_id=usr,
                question_id=que).first()
        if queobj is not None:
            queobj.upvote = 1
            queobj.downvote = 0
            db.session.commit()
        else:
            queobj = user_que_vote(user_id=usr, question_id=que,
                                   upvote=1, downvote=0)
            db.session.add(queobj)
            db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/neutral_que_1', methods=['POST'])
def neutral_que_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        queobj = user_que_vote.query.filter_by(user_id=usr,
                question_id=que).first()
        if queobj is not None:
            queobj.upvote = 0
            queobj.downvote = 0
            db.session.commit()
        else:
            queobj = user_que_vote(user_id=usr, question_id=que,
                                   upvote=0, downvote=0)
            db.session.add(queobj)
            db.session.commit()
        db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/downvote_que_1', methods=['POST'])
def downvote_que_1():
    try:
        usr = request.form['usr']
        que = request.form['que']
        queobj = user_que_vote.query.filter_by(user_id=usr,
                question_id=que).first()
        if queobj is not None:
            queobj.upvote = 0
            queobj.downvote = -1
            db.session.commit()
        else:
            queobj = user_que_vote(user_id=usr, question_id=que,
                                   upvote=0, downvote=-1)
            db.session.add(queobj)
            db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/upvote_ans_1', methods=['POST'])
def upvote_ans_1():
    try:
        usr = request.form['usr']
        ans = request.form['ans']
        ansobj = user_ans_vote.query.filter_by(user_id=usr,
                ans_id=ans).first()
        if ansobj is not None:
            ansobj.upvote = 1
            ansobj.downvote = 0
            db.session.commit()
        else:
            ansobj = user_ans_vote(user_id=usr, ans_id=ans, upvote=1,
                                   downvote=0)
            db.session.add(ansobj)
            db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/neutral_ans_1', methods=['POST'])
def neutral_ans_1():
    try:
        usr = request.form['usr']
        ans = request.form['ans']
        ansobj = user_ans_vote.query.filter_by(user_id=usr,
                ans_id=ans).first()
        if ansobj is not None:
            ansobj.upvote = 0
            ansobj.downvote = 0
            db.session.commit()
        else:
            ansobj = user_ans_vote(user_id=usr, ans_id=ans, upvote=0,
                                   downvote=0)
            db.session.add(ansobj)
            db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/downvote_ans_1', methods=['POST'])
def downvote_ans_1():
    try:
        usr = request.form['usr']
        ans = request.form['ans']
        ansobj = user_ans_vote.query.filter_by(user_id=usr,
                ans_id=ans).first()
        if ansobj is not None:
            ansobj.upvote = 0
            ansobj.downvote = -1
            db.session.commit()
        else:
            ansobj = user_ans_vote(user_id=usr, ans_id=ans, upvote=0,
                                   downvote=-1)
            db.session.add(ansobj)
            db.session.commit()
        return 'success'
    except :
        return render_template('error.html')


@app.route('/user_sign_in', methods=['POST'])
def user_sign_in():
    try:
        return redirect(url_for('.index'))
    except :
        return render_template('error.html')


@app.route('/user_sign_up')
def user_sign_up():
    try:
        cn = country.query.all()
        con = []
        for i in cn:
            con.append({'id': i.country_id, 'name': i.country_name})
        return render_template('user_sign_up.html', name='#',
                               country=con)
    except :
        return render_template('error.html')


@app.route('/signout_user')
def signout_user():
    try:
        session.pop('uid', None)
        session.pop('fname', None)
        return redirect(url_for('.index'))
    except :
        return render_template('error.html')


@app.route('/view_profile')
def view_profile():
    try:
        uid = request.args.get('uid', default='', type=str)
        usr = user.query.filter_by(user_id=uid).first()
        con = country.query.filter_by(country_id=usr.country_id).first()
        user_dict = {
            'fname': usr.first_name,
            'lname': usr.last_name,
            'email': usr.email_id,
            'country': con.country_name,
            'current': usr.current_position,
            'college': usr.college,
            'date': str(usr.date_of_birth)[:10],
            'pic': usr.profile_pic,
            'gn': usr.gender,
            }

        ques_obj = questions.query.filter_by(user_id=uid)
        ques_set = []
        for item in ques_obj:
            ques_set.append({'id': item.question_id,
                            'title': item.title})

        ans_obj = answer.query.filter_by(user_id=uid)
        ques_ans_set = []
        for item in ans_obj:
            que_detail = \
                questions.query.filter_by(question_id=item.question_id).first()
            ques_ans_set.append({'title': que_detail.title,
                                'id': que_detail.question_id})
        if 'uid' not in session:
            return render_template('view_profile.html', name="#", usr_dict=user_dict, qset=ques_set,
                               ansset=ques_ans_set)
        else :
            return render_template('view_profile.html', name=session['fname'
                               ], usr_dict=user_dict, qset=ques_set,
                               ansset=ques_ans_set)
    except :
        return render_template('error.html')


@app.route('/user_sign_up_1', methods=['POST'])
def user_sign_up_1():
    try:
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
        dd = datetime.now()
        destination = 'Default.jpg'
        for f in request.files.getlist('file'):
            if f.filename == '':
                break
            else:

                cwd = os.getcwd()
                target = os.path.join(cwd, 'static/Img/')
                filename = f.filename
                ext = filename.split('.')
                destination = '/'.join([target, filename])
                f.save(destination)
                destination = filename

        usr = user(
            first_name=first,
            middle_name=middle,
            last_name=last,
            email_id=email,
            password=password,
            gender=gender,
            mobile_no=mobile,
            country_id=country,
            current_position=current_pos,
            college=college,
            date_of_birth=dob,
            date_of_reg=dd,
            profile_pic=destination,
            )
        db.session.add(usr)
        db.session.commit()
        return redirect(url_for('.index'))
    except :
        return render_template('error.html')


@app.route('/validate_email_user', methods=['POST'])
def validate_email_user():
    try:
        x = 0
        email = request.form['email']
        usr = user.query.all()
        for data in usr:
            if data.email_id == email:
                x = 1

        if x == 1:
            return 'wrong'
        else:
            return 'success'
    except :
        return render_template('error.html')


@app.route('/admin_login')
def admin_login():
    try:
        return render_template('admin_login.html')
    except :
        return render_template('error.html')


@app.route('/Bookmark')
def Bookmark():
    try:
        set_questions = []
        if 'uid' not in session:
            return render_template('bookmark.html', name='#',
                                   questionList=set_questions, uuid='')
        else:
            bookmark_objs = \
                bookmark.query.filter_by(user_id=session['uid'])
            que_set = []
            for bookmark_obj in bookmark_objs:
                b_que_id = bookmark_obj.question_id
                ques = \
                    questions.query.filter_by(question_id=b_que_id).first()
                que_set.append(ques)
            cur_id = session['uid']
            set_questions = getQuestionDict(que_set, False)
            return render_template('bookmark.html', name=session['fname'
                                   ], questionList=set_questions,
                                   uuid=cur_id)
    except :
        return render_template('error.html')


@app.route('/admin', methods=['POST'])
def admin():
    try:
        cu_obj = contact_us.query.filter_by(cu_resolve=0)
        cu_dict = []
        for i in cu_obj:
            cu_dict.append({
                'name': i.cu_name,
                'email': i.cu_email_id,
                'mobile': i.cu_mobile_no,
                'message': i.cu_msg,
                })
        return render_template('admin.html', contact_us_dict=cu_dict)
    except :
        return render_template('error.html')


@app.route('/que_page')
def que_page():
    try:
        if 'uid' not in session:
            cur_id = 0
        else:
            cur_id = session['uid']
        qid = request.args.get('qid', default='', type=str)
        qobj = questions.query.filter_by(question_id=qid).first()
        usr = user.query.filter_by(user_id=qobj.user_id).first()
        tags = que_tag.query.filter_by(question_id=qid)
        tglist = []
        for tg in tags:
            tname = tag.query.filter_by(tag_id=tg.tag_id).first()
            tglist.append({'id': tg.tag_id, 'name': tname.tag_name})

        book = bookmark.query.filter_by(user_id=cur_id,
                question_id=qid).first()
        if book is None:
            bool_bid = 0
        else:
            bool_bid = 1
        ans_lat = answer_later.query.filter_by(question_id=qid,
                user_id=cur_id).first()
        if ans_lat is None:
            bool_ans_lat = 0
        else:
            bool_ans_lat = 1
        ans = answer.query.filter_by(question_id=qid,
                user_id=cur_id).first()
        if ans is None:
            bool_ans = 0
        else:
            bool_ans = 1
        vw = user_views.query.filter_by(question_id=qid)
        viewcount = 0
        for vwitem in vw:
            viewcount = viewcount + 1
        votecount = 0
        vtobj = user_que_vote.query.filter_by(question_id=qid)
        for voteitem in vtobj:
            votecount = votecount + voteitem.upvote + voteitem.downvote
        up = 0
        down = 0
        if cur_id != 0:
            vtobj = user_que_vote.query.filter_by(question_id=qid,
                    user_id=cur_id).first()
            if vtobj is not None:
                up = vtobj.upvote
                down = vtobj.downvote
            uvobj = user_views.query.filter_by(user_id=cur_id,
                    question_id=qid).first()
            if uvobj is None:
                viewcount = viewcount + 1
                uvobj = user_views(user_id=cur_id, question_id=qid,
                                   views=1)
                db.session.add(uvobj)
                db.session.commit()
        quedict = {
            'id': qid,
            'title': qobj.title,
            'question_content': qobj.question_content,
            'votes': votecount,
            'date': str(qobj.que_date)[:16],
            'views': viewcount,
            'uid': usr.user_id,
            'ufname': usr.first_name,
            'ulname': usr.last_name,
            'tag': tglist,
            'BID': bool_bid,
            'ans_later': bool_ans_lat,
            'answered': bool_ans,
            'upvote': up,
            'downvote': down,
            }

        chk = 0
        ansobj = answer.query.filter_by(question_id=qid)
        anslist = []
        for item in ansobj:
            if item.user_id == cur_id:
                chk = 1
            usr = user.query.filter_by(user_id=item.user_id).first()
            commentlist = []
            cmnt = comment.query.filter_by(ans_id=item.ans_id)
            for cmntitem in cmnt:
                usr_1 = \
                    user.query.filter_by(user_id=cmntitem.user_id).first()
                commentlist.append({
                    'id': cmntitem.comment_id,
                    'content': cmntitem.comment_content,
                    'uid': usr_1.user_id,
                    'ufname': usr_1.first_name,
                    'ulname': usr_1.last_name,
                    'date': str(cmntitem.comment_date)[:16],
                    })
            vtobj = user_ans_vote.query.filter_by(ans_id=item.ans_id)
            votecount = 0
            for voteitem in vtobj:
                votecount = votecount + voteitem.upvote \
                    + voteitem.downvote
            up = 0
            down = 0
            ansvoteobj = user_ans_vote.query.filter_by(user_id=cur_id,
                    ans_id=item.ans_id).first()
            if ansvoteobj is not None:
                up = ansvoteobj.upvote
                down = ansvoteobj.downvote
            anslist.append({
                'a_id': item.ans_id,
                'content': item.ans_content,
                'date': str(item.ans_date)[:16],
                'votes': votecount,
                'uid': item.user_id,
                'ufname': usr.first_name,
                'ulname': usr.last_name,
                'comments': commentlist,
                'upvote': up,
                'downvote': down,
                })
        from operator import itemgetter
        anslist = sorted(anslist, key=itemgetter('votes'), reverse=True)

        if 'uid' not in session:
            return render_template(
                'que_page.html',
                name='#',
                uid=cur_id,
                qid=qid,
                quedict=quedict,
                anslist=anslist,
                )
        else:
            return render_template(
                'que_page.html',
                name=session['fname'],
                uid=cur_id,
                qid=qid,
                quedict=quedict,
                anslist=anslist,
                chkbtn=chk,
                )
    except :
        return render_template('error.html')


@app.route('/ask_question')
def ask_question():
    try:
        if 'uid' not in session:
            return render_template('ask_question.html', name='#')
        else:
            return render_template('ask_question.html',
                                   name=session['fname'])
    except :
        return render_template('error.html')


@app.route('/ask_question_1', methods=['POST'])
def ask_question_1():
    try:
        cur_id = session['uid']
        title = request.form['title']
        sn = request.form['editordata']
        tag1 = request.form['tag_1']
        tag2 = request.form['tag_2']
        tag3 = request.form['tag_3']
        tag4 = request.form['tag_4']
        tag5 = request.form['tag_5']

        tag1 = tag1.lower()
        tag2 = tag2.lower()
        tag3 = tag3.lower()
        tag4 = tag4.lower()
        tag5 = tag5.lower()

        date_of_question = datetime.now()
        tagid1 = None
        tagid2 = None
        tagid3 = None
        tagid4 = None
        tagid5 = None

        tg = tag.query.filter_by(tag_name=tag1).first()
        if tg == None:
            tg = tag(tag_name=tag1)
            db.session.add(tg)
            db.session.commit()
            tagid1 = tg.tag_id
        else:
            tagid1 = tg.tag_id

        if tag2 != None or tag2 != '':
            tg = tag.query.filter_by(tag_name=tag2).first()
            if tg == None:
                tg = tag(tag_name=tag2)
                if tg.tag_name != '':
                    db.session.add(tg)
                    db.session.commit()
                    tagid2 = tg.tag_id
            else:
                tagid2 = tg.tag_id

        if tag3 != None or tag3 != '':
            tg = tag.query.filter_by(tag_name=tag3).first()
            if tg == None:
                tg = tag(tag_name=tag3)
                if tg.tag_name != '':
                    db.session.add(tg)
                    db.session.commit()
                    tagid3 = tg.tag_id
            else:
                tagid3 = tg.tag_id

        if tag4 != None or tag4 != '':
            tg = tag.query.filter_by(tag_name=tag4).first()
            if tg == None:
                tg = tag(tag_name=tag4)
                if tg.tag_name != '':
                    db.session.add(tg)
                    db.session.commit()
                    tagid4 = tg.tag_id
            else:
                tagid4 = tg.tag_id

        if tag5 != None or tag5 != '':
            tg = tag.query.filter_by(tag_name=tag5).first()
            if tg == None:
                tg = tag(tag_name=tag5)
                if tg.tag_name != '':
                    db.session.add(tg)
                    db.session.commit()
                    tagid5 = tg.tag_id
            else:
                tagid5 = tg.tag_id

        que = questions(user_id=cur_id, question_content=sn,
                        title=title, delete_votes=0,
                        que_date=date_of_question)
        db.session.add(que)
        db.session.commit()
        qid = que.question_id

        quevote = user_que_vote(user_id=cur_id, question_id=qid,
                                upvote=0, downvote=0)
        db.session.add(quevote)
        db.session.commit()

        if tagid1 != None and tagid1 != '':
            qt = que_tag(tag_id=tagid1, question_id=qid)
            db.session.add(qt)
            db.session.commit()

        if tagid2 != None and tagid2 != '':
            qt = que_tag(tag_id=tagid2, question_id=qid)
            db.session.add(qt)
            db.session.commit()

        if tagid3 != None and tagid3 != '':
            qt = que_tag(tag_id=tagid3, question_id=qid)
            db.session.add(qt)
            db.session.commit()

        if tagid4 != None and tagid4 != '':
            qt = que_tag(tag_id=tagid4, question_id=qid)
            db.session.add(qt)
            db.session.commit()

        if tagid5 != None and tagid5 != '':
            qt = que_tag(tag_id=tagid5, question_id=qid)
            db.session.add(qt)
            db.session.commit()

        return redirect(url_for('.index'))
    except :
        return render_template('error.html')


@app.route('/todo')
def todo():
    try:
        set_questions = []
        if 'uid' not in session:
            return render_template('todo.html', name='#',
                                   questionList=set_questions)
        else:
            cur_id = session['uid']
            later_ques = answer_later.query.filter_by(user_id=cur_id)
            set_questions_obj = []
            for q in later_ques:
                ques = \
                    questions.query.filter_by(question_id=q.question_id).first()
                set_questions_obj.append(ques)
            set_questions = getQuestionDict(set_questions_obj, False)
            return render_template('todo.html', name=session['fname'],
                                   questionList=set_questions,
                                   uuid=cur_id)
    except :
        return render_template('error.html')


@app.route('/about_us')
def about_us():
    try:
        if 'uid' not in session:
            return render_template('about_us.html', name='#')
        else:
            return render_template('about_us.html', name=session['fname'
                                   ])
    except :
        return render_template('error.html')


@app.route('/contact_us')
def contact():
    try:
        if 'uid' not in session:
            return render_template('contact_us.html', name='#')
        else:
            return render_template('contact_us.html',
                                   name=session['fname'])
    except :
        return render_template('error.html')


@app.route('/search_question', methods=['POST'])
def search_question():
    try:
        search_question_text = request.form['search_question_input']
        newstr = '%' + search_question_text + '%'
        questionlist = \
            questions.query.filter(questions.title.like(newstr)).all()
        if 'uid' not in session:
            set_questions = getQuestionDict(questionlist, True)
            return render_template('search_result.html', name='#',
                                   questionList=set_questions, uuid=0)
        else:
            set_questions = getQuestionDict(questionlist, False)
            return render_template('search_result.html',
                                   name=session['fname'],
                                   questionList=set_questions,
                                   uuid=session['uid'])
    except :
        return render_template('error.html')


@app.route('/search_tag', methods=['POST'])
def search_tag():
    try:
        search_tag_text = request.form['search_tag_input']
        newstr = '%' + search_tag_text + '%'
        tagidlist = tag.query.filter(tag.tag_name.like(newstr)).all()
        queidlist = []
        for tagid in tagidlist:
            tmp = que_tag.query.filter_by(tag_id=tagid.tag_id).all()
            queidlist += tmp
        questionlist = []
        for queid in queidlist:
            question_obj = \
                questions.query.filter_by(question_id=queid.question_id).first()
            questionlist.append(question_obj)
        if 'uid' not in session:
            set_questions = getQuestionDict(questionlist, True)
            return render_template('search_result.html', name='#',
                                   questionList=set_questions, uuid=0)
        else:
            set_questions = getQuestionDict(questionlist, False)
            return render_template('search_result.html',
                                   name=session['fname'],
                                   questionList=set_questions,
                                   uuid=session['uid'])
    except :
        return render_template('error.html')


@app.route('/search_perticular_tag')
def search_perticular_tag():
    try:
        search_tagid = request.args.get('search_tid', default='',
                type=str)
        queidlist = que_tag.query.filter_by(tag_id=search_tagid).all()
        questionlist = []
        for queid in queidlist:
            question_obj = \
                questions.query.filter_by(question_id=queid.question_id).first()
            questionlist.append(question_obj)
        if 'uid' not in session:
            set_questions = getQuestionDict(questionlist, True)
            return render_template('search_result.html', name='#',
                                   questionList=set_questions, uuid=0)
        else:
            set_questions = getQuestionDict(questionlist, False)
            return render_template('search_result.html',
                                   name=session['fname'],
                                   questionList=set_questions,
                                   uuid=session['uid'])
    except :
        return render_template('error.html')


@app.route('/contact_us_1', methods=['POST'])
def contact_us_1():
    try:
        name = request.form['name']
        email = request.form['email_ct']
        mobile = request.form['mobile']
        message = request.form['message']

        cu = contact_us(cu_name=name, cu_email_id=email,
                        cu_mobile_no=mobile, cu_msg=message)
        db.session.add(cu)
        db.session.commit()
        return redirect(url_for('.index'))
    except :
        return render_template('error.html')


@app.route('/post_answer', methods=['POST'])
def post_answer():
    try:
        cur_id = session['uid']
        ans_content = request.form['editordata']
        qid = request.form['qid']
        ans_date = datetime.now()
        ans = answer(ans_content=ans_content, user_id=cur_id,
                     question_id=qid, ans_date=ans_date)
        db.session.add(ans)
        db.session.commit()
        aid = ans.ans_id
        ansvote = user_ans_vote(user_id=cur_id, ans_id=aid, upvote=0,
                                downvote=0)
        db.session.add(ansvote)
        db.session.commit()
        ans_l = answer_later.query.filter_by(user_id=cur_id,
                question_id=qid).first()
        if ans_l is not None:
            db.session.delete(ans_l)
            db.session.commit()
        return redirect(url_for('.que_page', qid=qid))
    except :
        return render_template('error.html')


@app.route('/post_comment_1', methods=['POST'])
def post_comment_1():
    try:
        uid = session['uid']
        aid = request.form['ans__id']
        qid = request.form['que__id']
        comment_content = request.form['commentbox']
        cmnt_date = datetime.now()
        cmnt = comment(user_id=uid, ans_id=aid,
                       comment_content=comment_content,
                       comment_date=cmnt_date)
        db.session.add(cmnt)
        db.session.commit()
        return redirect(url_for('.que_page', qid=qid))
    except :
        return render_template('error.html')


@app.route('/user_change_pass')
def user_change_pass():
    try:
        try:
            uid = session['uid']
            uname = session['fname']
            return render_template('user_change_pass.html', name=uname)
        except:
            return 'not logged in'
    except :
        return render_template('error.html')


@app.route('/check_cur_psd', methods=['POST'])
def check__cur_psd():
    try:
        old_pass = request.form['cur_psd']
        uid = session['uid']
        usr = user.query.filter_by(user_id=uid).first()
        if old_pass != usr.password:
            return 'wrong'
        else:
            return 'ok'
    except :
        return render_template('error.html')


@app.route('/user_change_pass_1', methods=['POST'])
def user_change_pass_1():
    try:
        old_pass = request.form['cur_psd']
        uid = session['uid']
        usr = user.query.filter_by(user_id=uid).first()
        new_pass = request.form['new_psd']
        usr.password = new_pass
        db.session.add(usr)
        db.session.commit()
        session.pop('uid', None)
        session.pop('fname', None)
        return redirect(url_for('.index'))
    except :
        return render_template('error.html')


@app.route('/edit_profile_1', methods=['POST'])
def edit_profile_1():
    try:
        first = request.form['fname']
        middle = request.form['mname']
        last = request.form['lname']
        gender = request.form['gn']
        mobile = request.form['mobile']
        country = int(request.form['country'])
        current_pos = request.form['cur_pos']
        college = request.form['collegename']
        dob = request.form['date']
        destination = 'Default.jpg'
        for f in request.files.getlist('file'):
            if f.filename == '':
                break
            else:
                cwd = os.getcwd()
                target = os.path.join(cwd, 'static/Img/')
                filename = f.filename
                ext = filename.split('.')
                destination = '/'.join([target, filename])
                f.save(destination)
                destination = filename

        usr = user.query.filter_by(user_id=session['uid']).first()
        usr.first_name = first
        usr.middle_name = middle
        usr.last_name = last
        usr.gender = gender
        usr.mobile_no = mobile
        usr.country_id = country
        usr.current_position = current_pos
        usr.college = college
        usr.date_of_birth = dob
        if destination != 'Default.jpg':
            usr.profile_pic = destination
        db.session.commit()
        return redirect(url_for('edit_profile'))
    except :
        return render_template('error.html')


@app.route('/edit_profile')
def edit_profile():
    try:
        cn = country.query.all()
        con = []
        for i in cn:
            con.append({'id': i.country_id, 'name': i.country_name})
        uname = session['fname']
        uid = session['uid']
        usr = user.query.filter_by(user_id=uid).first()
        return render_template('user_edit_profile.html', name=uname,
                               u=usr, country=con)
    except :
        return render_template('error.html')


def getQuestionDict(questionlist, isguest):
    try:
        set_questions = []
        if isguest:
            for item in questionlist:
                tg_id = \
                    que_tag.query.filter_by(question_id=item.question_id)
                tagName = []
                for it in tg_id:
                    tgNameObj = \
                        tag.query.filter_by(tag_id=it.tag_id).first()
                    tagName.append({'id': tgNameObj.tag_id,
                                   'name': tgNameObj.tag_name})
                usr = user.query.filter_by(user_id=item.user_id).first()
                ans = \
                    answer.query.filter_by(question_id=item.question_id)
                ans_count = 0
                for answer_que in ans:
                    ans_count = ans_count + 1
                vw = \
                    user_views.query.filter_by(question_id=item.question_id)
                viewcount = 0
                for vwitem in vw:
                    viewcount = viewcount + 1
                votecount = 0
                vtobj = \
                    user_que_vote.query.filter_by(question_id=item.question_id)
                for voteitem in vtobj:
                    votecount = votecount + voteitem.upvote \
                        + voteitem.downvote
                set_questions.append({
                    'id': item.question_id,
                    'title': item.title,
                    'votes': votecount,
                    'views': viewcount,
                    'date': str(item.que_date)[:16],
                    'fname': usr.first_name,
                    'lname': usr.last_name,
                    'tags': tagName,
                    'uid': usr.user_id,
                    'ans': ans_count,
                    'BID': 0,
                    'ans_later': 0,
                    'answered': 0,
                    })
            return set_questions
        else:
            cur_id = session['uid']
            for item in questionlist:
                tg_id = \
                    que_tag.query.filter_by(question_id=item.question_id)
                tagName = [{}]
                for it in tg_id:
                    tgNameObj = \
                        tag.query.filter_by(tag_id=it.tag_id).first()
                    tagName.append({'id': tgNameObj.tag_id,
                                   'name': tgNameObj.tag_name})
                usr = user.query.filter_by(user_id=item.user_id).first()
                book = bookmark.query.filter_by(user_id=cur_id,
                        question_id=item.question_id).first()
                if book is None:
                    bool_bid = 0
                else:
                    bool_bid = 1
                ans = \
                    answer.query.filter_by(question_id=item.question_id)
                ans_count = 0
                for answer_que in ans:
                    ans_count = ans_count + 1
                ans_lat = \
                    answer_later.query.filter_by(question_id=item.question_id,
                        user_id=cur_id).first()
                if ans_lat is None:
                    bool_ans_lat = 0
                else:
                    bool_ans_lat = 1
                ans = \
                    answer.query.filter_by(question_id=item.question_id,
                        user_id=cur_id).first()
                if ans is None:
                    bool_ans = 0
                else:
                    bool_ans = 1
                vw = \
                    user_views.query.filter_by(question_id=item.question_id)
                viewcount = 0
                for vwitem in vw:
                    viewcount = viewcount + 1
                votecount = 0
                vtobj = \
                    user_que_vote.query.filter_by(question_id=item.question_id)
                for voteitem in vtobj:
                    votecount = votecount + voteitem.upvote \
                        + voteitem.downvote
                set_questions.append({
                    'id': item.question_id,
                    'title': item.title,
                    'votes': votecount,
                    'views': viewcount,
                    'date': str(item.que_date)[:16],
                    'fname': usr.first_name,
                    'lname': usr.last_name,
                    'tags': tagName,
                    'uid': item.user_id,
                    'ans': ans_count,
                    'BID': bool_bid,
                    'ans_later': bool_ans_lat,
                    'answered': bool_ans,
                    })
            return set_questions
    except :
        return render_template('error.html')


@app.errorhandler(404)
def http_404_handler(error):
	return render_template('error.html')

@app.errorhandler(405)
def http_405_handler(error):
	return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True, threaded=True, host='127.0.0.1')
