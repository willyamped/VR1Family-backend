from flask import Blueprint, request
from models.category import Category, Kit
from application import db

category_bp = Blueprint('category', __name__, url_prefix='/categories')
@category_bp.route('/category', methods=['GET'])
def get_all_categories():
  categories = Category.query.order_by(Category.id).all()
  output = []
  for category in categories:
    category_data = {
      'id': category.id,
      'name': category.name, 
      'status': category.status, 
      }
    output.append(category_data)
  return output

@category_bp.route('/category', methods=['POST'])
def add_new_category():
  try:
    category = Category(
      name = request.json['name'],
      status = request.json['status'],
    )
    db.session.add(category)
    db.session.commit()
    return f"Category {category.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"name, status\""

@category_bp.route('/kit', methods=['GET'])
def get_all_kits():
  kits = Kit.query.order_by(Kit.id).all()
  output = []
  for kit in kits:
    kit_data = {
      'id': kit.id,
      'name': kit.name, 
      'items': kit.items
      }
    output.append(kit_data)
  return output

@category_bp.route('/kit', methods=['POST'])
def add_new_kit():
  try:
    kit = Kit(
      name = request.json['name'],
      items = request.json['items']
    )
    db.session.add(kit)
    db.session.commit()
    return f"Kit {kit.id} has been added"
  except:
    return "One of the attributes is missing. Ensure you have \"name, items\""