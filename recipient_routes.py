from flask import Blueprint, request, jsonify
from recipient import Recipient, db

recipient_bp = Blueprint('recipient', __name__, url_prefix='/recipients')

@recipient_bp.route('/<id>')
def get_recipient(id):
  recipient = Recipient.query.get_or_404(id)
  return {"name": recipient.name}

@recipient_bp.route('/', methods=['GET', 'POST'])
def recipient():
  if request.method == 'GET':
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
  elif request.method == 'POST':
    recipient = Recipient(
      name = request.json['name'],
      age = request.json['age'],
      address = request.json['address'],
      num_of_family_members = request.json['num_of_family_members'],
      nationality = request.json['nationality'],
      identification_number = request.json['identification_number']
    )
    db.session.add(recipient)
    db.session.commit()
    return f"Recipient {recipient.id} has been added"

@recipient_bp.route('/<id>', methods=['DELETE'])
def delete_recipient(id):
  recipient = Recipient.query.get(id)
  if recipient is None:
    return "Recipient does not exist"
  db.session.delete(recipient)
  db.session.commit()
  return f"Recipient {id} has been deleted"