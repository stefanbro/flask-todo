import datetime
from flask import render_template, jsonify, flash, redirect, url_for, session, request
from app import app, db
from .forms import LoginForm, RegisterForm
from .models import User, Todo

general_uname = None

@app.route('/')
@app.route('/index')
def index():
	error = None
	form = RegisterForm()
	return render_template('index.html', error = error, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	error = None
	if request.method == 'POST':
		req_username = form.username.data
		req_password = form.password.data
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

	return render_template('login.html', error=error, form=form)

@app.route('/register', methods=['POST'])
def user_register():
	error = None
	form = RegisterForm()
	req_username = form.username.data
	req_email = form.email.data
	req_password = form.password.data
	req_password_again = form.password_again.data
	
	user = User.query.filter_by(username=req_username).first()
	if user is not None:
		error = "Username already exists"
		return render_template('index.html', error=error, form=form)
	elif req_password != req_password_again:
		return render_template('index.html', error=error, form=form)
	else:
		if form.validate():
			new_user = User(username=req_username, email=req_email, password=req_password_again)
			db.session.add(new_user)
			db.session.commit()
			return redirect(url_for('login'))
		else:
			error = 'Try again'
			return render_template('index.html', error=error, form=form)

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