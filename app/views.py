import datetime
from flask import render_template, jsonify, flash, redirect, url_for, session, request
from app import app, db
from .forms import LoginForm
from .models import User, Todo

general_uname = None

@app.route('/')
@app.route('/index')
def index():
	users = User.query.all()
	return render_template('index.html', title='Home', users = users)

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		req_username = request.form['username']
		req_password = request.form['password']
		user = User.query.filter_by(username=req_username).first()
		if user is None:
			error = "Wrong username"
		else:
			if user.password != req_password:
				error = "Wrong password"
			else:
				session['logged_in'] = True
				session['uname'] = req_username
				session['update'] = 0
				flash('You were logged in')
				return redirect(url_for('show_todos'))

	return render_template('login.html', error=error)

@app.route('/show_todos')
def show_todos():
	sesh_user = session['uname']
	uname = User.query.filter_by(username=sesh_user).first()
	return render_template('show_todos.html', uname=uname)

@app.route('/logout')
def logout():
	session.pop('uname', None)
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add_todo():
	if not session.get('logged_in'):
		abort(401)
	sesh_user = session['uname']
	new_todo = request.form['todo']
	user = User.query.filter_by(username=sesh_user).first()
	post = Todo(body=new_todo, is_done=0, timestamp=datetime.datetime.utcnow(), author=user)
	db.session.commit()
	return redirect(url_for('show_todos'))

@app.route('/_cross_todo')
def cross_todo():
	if not session.get('logged_in'):
		abort(401)
	a = request.args.get('a', 0, type=int)
	post = Todo.query.get(a)
	if post.is_done == 1:
		post.is_done=0
	else:
		post.is_done=1
	db.session.commit()
	a=0
	return jsonify(result=a)

@app.route('/clear_todos')
def clear_todos():
	if not session.get('logged_in'):
		abort(401)
	sesh_user = session['uname']
	uname = User.query.filter_by(username=sesh_user).first()
	uname.todos.filter_by(is_done=1).delete()
	db.session.commit()
	return redirect(url_for('show_todos'))