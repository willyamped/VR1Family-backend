from application import db

class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(80), nullable = False)
	status = db.Column(db.String(80), nullable = False)

class Kit(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(80), nullable = False)
	items = db.Column(db.JSON, nullable = False)

"""
e.g
"name": "warm clothing kit",
"items": [{"socks": 2}, {"shirts": 2}, {"blanket": 1}]
})
"""