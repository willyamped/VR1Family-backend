from application import db

class Receive(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    donor_name = db.Column(db.String(80), nullable = False)
    item = db.Column(db.JSON, nullable = False)
    

