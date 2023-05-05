from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

from routes.recipient_routes import recipient_bp
app.register_blueprint(recipient_bp)

from routes.donor_routes import donor_bp
app.register_blueprint(donor_bp)

from routes.category_routes import category_bp
app.register_blueprint(category_bp)

from routes.item_routes import item_bp
app.register_blueprint(item_bp)

from routes.request_routes import request_bp
app.register_blueprint(request_bp)

from routes.receive_routes import receive_bp
app.register_blueprint(receive_bp)

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(host = 'localhost', port = 5001)

