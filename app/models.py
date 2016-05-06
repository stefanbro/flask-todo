from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(64), index=True)
	todos = db.relationship('Todo', backref='author', lazy='dynamic')
	
	def __repr__(self):
		return '<User %r>' % (self.username)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(100))
	is_done = db.Column(db.Integer, default=0)
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '%r' % (self.body)
