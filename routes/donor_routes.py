from flask import Blueprint, request
from models.donor import Donor
from application import db

donor_bp = Blueprint('donor', __name__, url_prefix='/donors')
@donor_bp.route('/', methods=['GET'])
def get_all_donors():
  donors = Donor.query.order_by(Donor.id).all()
  output = []
  for donor in donors:
    donor_data = {
      'id': donor.id,
      'name': donor.name, 
      'age': donor.age, 
      'address': donor.address,
      'phone_number': donor.phone_number,
      'email_address': donor.email_address,
      'contact_person': donor.contact_person,
      }
    output.append(donor_data)
  return output

@donor_bp.route('/', methods=['POST'])
def add_new_donor():
  try:
    donor = Donor(
      name = request.json['name'],
      age = request.json['age'],
      address = request.json['address'],
      phone_number = request.json['phone_number'],
      email_address = request.json['email_address'],
      contact_person = request.json['contact_person'] if 'contact_person' in request.json else None,
      nationality = request.json['nationality'],
      identification_numbers = request.json['identification_numbers'],
      registration_details = request.json['registration_details'] if 'registration_details' in request.json else None
    )
    db.session.add(donor)
    db.session.commit()
    return f"Donor {donor.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"name, age, address, phone_number, email_address, nationality, identification_numbers\""