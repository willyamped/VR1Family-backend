from flask import Blueprint, request
from models.request import Request
from application import db

request_bp = Blueprint('request', __name__, url_prefix='/requests')
@request_bp.route('/', methods=['GET'])
def get_all_requests():
  requests = Request.query.order_by(Request.id).all()
  output = []
  for request in requests:
    request_data = {
      'id': request.id,
      'recipient_name': request.recipient_name, 
      'kit': request.kit, 
      'item': request.item,
      'quantity': request.quantity,
      'note': request.note,
      }
    output.append(request_data)
  return output

@request_bp.route('/', methods=['POST'])
def add_new_request():
  try:
    request_data = Request(
      recipient_name = request.json['recipient_name'],
      kit = request.json['kit'] if 'kit' in request.json else None,
      item = request.json['item'] if 'item' in request.json else None,
      quantity = request.json['quantity'],
      note = request.json['note'],
    )
    db.session.add(request_data)
    db.session.commit()
    return f"Request {request_data.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"recipient_name, quantity, note\""