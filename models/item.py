from application import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    category = db.Column(db.String(80), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    brand = db.Column(db.String(80), nullable = False)
    expiry_date = db.Column(db.String(80), nullable = False)
    ingredients = db.Column(db.JSON, nullable = False)
    allergens = db.Column(db.JSON, nullable = False)
    size = db.Column(db.String(80), nullable = True)
    kit = db.Column(db.JSON, nullable = True)

