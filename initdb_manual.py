from app import db
db.create_all()
from app import Question, Comment, Tag, Explanation
from app import MChoiceOption as MC
q = Question("H2G2 Q1", "What do you get when you multipyly 6 x 9?")
q.tags = ['h2g2']
q.options = [MC('0'), MC('1'), MC('42', True), MC('over 9000')]
q.rating = -1
q.explanations.append(Explanation("It's the answer to life, universe, and everything."))
q.comments.append(Comment("Douglas Adams is awesome."))
db.session.add(q)


q = Question("H2G2 Q2", "What is Zaphod Beeblebrox's favorite drink?")
q.tags = ['h2g2']
q.options = [MC('Liquid that is almost, but not quite, entirely unlike tea'),
			 MC('Pan-galactic gargle blaster', True),
			 MC('White Russian'),
			 MC('Diet Coke')]
q.rating = -1
q.explanations.append(Explanation("The effect of drinking a Pan Galactic Gargle Blaster is like having your brains smashed out by a slice of lemon wrapped around a large gold brick."))
db.session.add(q)

db.session.commit()
