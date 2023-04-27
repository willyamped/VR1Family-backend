from application import db

class Recipient(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  age = db.Column(db.Integer)
  address = db.Column(db.String(80))
  num_of_family_members = db.Column(db.Integer)
  
  nationality = db.Column(db.String(80))
  identification_numbers = db.Column(db.JSON)