import json
from app import db
db.create_all()
from app import Question, Comment, Tag, Explanation
with open("./questions.json") as f:
	try:
		questions = json.load(f)
		for qdict in questions:
			q = Question.from_data(qdict)
			db.session.add(q)
	except Exception as e:
		print "Invalid JSON: %s" % e

db.session.commit()
