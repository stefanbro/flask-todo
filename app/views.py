import datetime
from flask import render_template, flash, redirect, url_for, session, request
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

@app.route('/update', methods=['POST'])
def update_todo(sesh_id):
	if not session.get('logged_in'):
		abort(401)
	sesh_update_id = sesh_id
	post = Todo.query.get(sesh_update_id)
	if post.is_done == 0:
		post.is_done = 1
	else:
		post.is_done = 0
	
	session['update'] = 0
