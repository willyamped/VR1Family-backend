from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

from routes.recipient_routes import recipient_bp
app.register_blueprint(recipient_bp)

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run()

