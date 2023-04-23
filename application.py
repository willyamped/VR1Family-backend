from flask import Flask, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from recipient import Recipient, db

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

from recipient_routes import recipient_bp
app.register_blueprint(recipient_bp)

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run()

