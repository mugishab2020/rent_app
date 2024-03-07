from flask import Flask
from models import db
from routes import bp 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mugishab2020:edsonb2023@localhost/mydatabase' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

    # Register blueprint containing routes
app.register_blueprint(bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
