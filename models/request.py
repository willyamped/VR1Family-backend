from application import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    recipient_name = db.Column(db.String(80), nullable = False)
    kit = db.Column(db.String(80), nullable = True)
    item = db.Column(db.JSON, nullable = True)
    quantity = db.Column(db.Integer, nullable = False)
    note = db.Column(db.String(80), nullable = False)

