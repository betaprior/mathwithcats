from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from flask import request
from flask import __version__
from flask import jsonify
from flask import render_template
from flask import make_response
import re
import os
import json
app = Flask(__name__, static_url_path='')
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db = SQLAlchemy(app)

tags = db.Table('tags',
				db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
				db.Column('question_id', db.Integer, db.ForeignKey('question.id'))
			)

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String)

	def __init__(self, body):
		self.body = body


class Question(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	body = db.Column(db.String)
	options = db.relationship('MChoiceOption', backref=db.backref('question'),
							  lazy=False)
	rating = db.Column(db.Integer)
	taglist = db.relationship('Tag', secondary=lambda: tags,
						   backref=db.backref('questions', lazy='dynamic'))
	tags = association_proxy('taglist', 'body')
	explanations = db.relationship('Explanation', backref=db.backref('question'),
								   lazy='dynamic')
	comments = db.relationship('Comment', backref=db.backref('question'),
								   lazy='dynamic')

	def __init__(self, title, body):
		self.body = body
		self.title = title

	def __repr__(self):
		return '<Question: %r>' % self.body

	@hybrid_property
	def answer(self):
		return [x[1].body for x in enumerate(self.options) if x[1].correct]

	@hybrid_property
	def answer_idx(self):
		return [x[0] for x in enumerate(self.options) if x[1].correct]

	@classmethod
	def from_data(cls, d):
		"Data should be a dict"
		q = cls(d["title"], d["body"])
		answer_idx = d.get("answer_idx", [])
		opt = []
		for i, a in enumerate(d.get("options", [])):
			opt.append(MChoiceOption(a, correct=i in answer_idx))
		q.options = opt
		q.rating = d.get("rating", -1)
		q.tags = d.get("tags", [])
		for e in d.get("explanations", []):
			q.explanations.append(Explanation(e))
		for c in d.get("comments", []):
			q.comments.append(Comment(c))
		return q

	def match_tags(self, key):
		if key == "*": return True
		if not key: return False
		return any(x.startswith(key) for x in self.tags)

	def json_view(self):
		return {
			"id": self.id,
			"title": self.title,
			"body": self.body,
			"tags": list(self.tags),
			"options": [x.body for x in self.options],
			"answer": self.answer,
			"answer_idx": self.answer_idx,
			"rating": self.rating,
			"explanations": [x.body for x in self.explanations],
			"comments": [x.body for x in self.comments]
		}

class MChoiceOption(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String)
	correct = db.Column(db.Boolean)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

	def __init__(self, body, correct=False):
		self.body = body
		self.correct = correct

	def __repr__(self):
		return '<MChoiceOption: %r>' % self.body


class Explanation(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String)
	rating = db.Column(db.Integer)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

	def __init__(self, body):
		self.body = body

	def __repr__(self):
		return '<Explanation: %r>' % self.body

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String)
	rating = db.Column(db.Integer)
	question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

	def __init__(self, body):
		self.body = body

	def __repr__(self):
		return '<Comment: %r>' % self.body



@app.route("/")
def root():
	return app.send_static_file('index.html')
	# return render_template('index.html')

@app.route('/questions')
def get_questions():
	questions = Question.query.all()
	key = request.args.get('key')
	matches = [q for q in questions if q.match_tags(key)]
	return jsonify(collection=[i.json_view() for i in matches])

@app.route("/version")
def version():
	return "Flask version: %s" % __version__

@app.route("/test<string:num>")
def numbered_test(num):
	return render_template('test' + num + '.html')


@app.route('/files/<path:path>')
def static_proxy(path):
	# send_static_file will guess the correct MIME type
	return app.send_static_file(os.path.join('files', path))


class InvalidSearch(Exception):
	status_code = 400
	def __init__(self, message, status_code=None, payload=None):
		Exception.__init__(self)
		self.message = message
		if status_code is not None:
			self.status_code = status_code
		self.payload = payload
	def to_dict(self):
		rv = dict(self.payload or ())
		rv['message'] = self.message
		return rv

@app.errorhandler(InvalidSearch)
def handle_invalid_search(error):
	response = jsonify(error.to_dict())
	response.status_code = error.status_code
	return response



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5002, debug = True) # in Flask
	# app.run(host='0.0.0.0', port=5002, debug = False) # in Flask
