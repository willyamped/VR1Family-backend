from application import db

class Donor(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  age = db.Column(db.Integer)
  address = db.Column(db.String(80))
  phone_number = db.Column(db.String(80), nullable = False)
  email_address = db.Column(db.String(80), nullable = False)
  contact_person = db.Column(db.String(80), nullable = True)
  
  nationality = db.Column(db.String(80))
  identification_numbers = db.Column(db.JSON)
  registration_details = db.Column(db.String(80), nullable = True)