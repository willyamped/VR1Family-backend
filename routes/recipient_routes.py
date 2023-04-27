from flask import Blueprint, request
from models.recipient import Recipient
from application import db

recipient_bp = Blueprint('recipient', __name__, url_prefix='/recipients')
@recipient_bp.route('/', methods=['GET'])
def get_all_recipients():
  recipients = Recipient.query.order_by(Recipient.id).all()
  output = []
  for recipient in recipients:
    recipient_data = {
      'id': recipient.id,
      'name': recipient.name, 
      'age': recipient.age, 
      'address': recipient.address,
      'num_of_family_members': recipient.num_of_family_members
      }
    output.append(recipient_data)
  return output

@recipient_bp.route('/', methods=['POST'])
def add_new_recipient():
  try:
    recipient = Recipient(
      name = request.json['name'],
      age = request.json['age'],
      address = request.json['address'],
      num_of_family_members = request.json['num_of_family_members'],
      nationality = request.json['nationality'],
      identification_numbers = request.json['identification_numbers']
    )
    db.session.add(recipient)
    db.session.commit()
    return f"Recipient {recipient.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"name, age, address, num_of_family_members, nationality, identification_numbers\""
    
@recipient_bp.route('/<id>', methods=['GET'])
def get_recipient_by_id(id):
  try:
    recipient = Recipient.query.get(id)
    return {"name": recipient.name, "identification": recipient.identification_numbers}
  except:
    return f"id: {id} does not exist"

@recipient_bp.route('/<id>', methods=['DELETE'])
def delete_recipient_by_id(id):
  recipient = Recipient.query.get(id)
  if recipient:
    db.session.delete(recipient)
    db.session.commit()
    return f"Recipient {id} has been deleted"
  else:
    return f"id: {id} does not exist"

@recipient_bp.route('/<id>', methods=['PUT'])
def update_recipient_by_id(id):
  print(id)
  recipient = Recipient.query.get(id)
  if recipient:
    name = request.json.get('name', recipient.name)
    age = request.json.get('age', recipient.age)
    address = request.json.get('address', recipient.address)
    num_of_family_members = request.json.get('num_of_family_members', recipient.num_of_family_members)
    nationality = request.json.get('nationality', recipient.nationality)
    identification_number = request.json.get('identification_number', recipient.identification_number)
    
    recipient.name = name
    recipient.age = age
    recipient.address = address
    recipient.num_of_family_members = num_of_family_members
    recipient.nationality = nationality
    recipient.identification_number = identification_number
    
    db.session.commit()
    
    return f"Recipient {recipient.id} has been updated"
  else:
    return f"id: {id} does not exist"