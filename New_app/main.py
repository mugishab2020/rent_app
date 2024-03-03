from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db
from routes import bp as routes_bp
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mugishab2020:edsonb2023@localhost/mydatabase' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

    # Register blueprint containing routes
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
