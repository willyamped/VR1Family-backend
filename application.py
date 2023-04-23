from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Recipient(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable = False)
  age = db.Column(db.Integer)
  address = db.Column(db.String(80))
  num_of_family_members = db.Column(db.Integer)

with app.app_context():
  db.create_all()

@app.route('/recipients/<id>')
def get_recipient(id):
  recipient = Recipient.query.get_or_404(id)
  return {"name": recipient.name}

@app.route('/recipients', methods=['GET', 'POST'])
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
      num_of_family_members = request.json['num_of_family_members']
    )
    db.session.add(recipient)
    db.session.commit()
    return f"Recipient {recipient.id} has been added"

@app.route('/recipient/<id>', methods=['DELETE'])
def delete_recipient(id):
  recipient = Recipient.query.get(id)
  if recipient is None:
    return "Recipient does not exist"
  db.session.delete(recipient)
  db.session.commit()
  return f"Recipient {id} has been deleted"