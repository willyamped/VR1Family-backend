from flask import Blueprint, request
from models.receive import Receive
from application import db

receive_bp = Blueprint('receive', __name__, url_prefix='/receives')
@receive_bp.route('/', methods=['GET'])
def get_all_receives():
  receives = Receive.query.order_by(Receive.id).all()
  output = []
  for receive in receives:
    receive_data = {
      'id': receive.id,
      'donor_name': receive.donor_name, 
      'item': receive.item,
      }
    output.append(receive_data)
  return output

@receive_bp.route('/', methods=['POST'])
def add_new_receive():
  try:
    receive_data = Receive(
      donor_name = request.json['donor_name'],
      item = request.json['item'],
    )
    db.session.add(receive_data)
    db.session.commit()
    return f"Receive {receive_data.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"donor_name, item\""