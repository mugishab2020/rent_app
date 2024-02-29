from flask import Flask
from models import db
from routes import bp as routes_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database:mugishab2020@localhost/mydatabase' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Register blueprint containing routes
    app.register_blueprint(routes_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
