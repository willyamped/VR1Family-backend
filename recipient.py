from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipient(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  age = db.Column(db.Integer)
  address = db.Column(db.String(80))
  num_of_family_members = db.Column(db.Integer)
  
  nationality = db.Column(db.String(80))
  identification_number = db.Column(db.String(80))