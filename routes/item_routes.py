from flask import Blueprint, request
from models.item import Item
from application import db

item_bp = Blueprint('item', __name__, url_prefix='/items')
@item_bp.route('/', methods=['GET'])
def get_all_items():
  items = Item.query.order_by(Item.id).all()
  output = []
  for item in items:
    item_data = {
      'id': item.id,
      'name': item.name, 
      'category': item.category, 
      'quantity': item.quantity,
      'brand': item.brand,
      'expiry_date': item.expiry_date,
      'ingredients': item.ingredients,
      'allergens': item.allergens,
      'size': item.size,
      'kit': item.kit
      }
    output.append(item_data)
  return output

@item_bp.route('/', methods=['POST'])
def add_new_item():
  try:
    item = Item(
      name = request.json['name'],
      category = request.json['category'],
      quantity = request.json['quantity'],
      brand = request.json['brand'],
      expiry_date = request.json['expiry_date'],
      ingredients = request.json['ingredients'],
      allergens = request.json['allergens'],
      size = request.json['size'] if 'size' in request.json else None,
      kit = request.json['kit'] if 'kit' in request.json else None
    )
    db.session.add(item)
    db.session.commit()
    return f"Item {item.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"name, age, address, phone_number, email_address, nationality, identification_numbers\""