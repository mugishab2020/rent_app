from flask import Flask
from models import db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from routes import bp 
from flask_migrate import Migrate

from models import Car, User
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mugishab2020:edsonb2023@localhost/mydatabase' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mugishab2020'

migrate = Migrate(app, db)

admin = Admin(app, name='Admin', template_mode='bootstrap3')

# Add views for models to the admin interface
#admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Car, db.session))


db.init_app(app)

    # Register blueprint containing routes
app.register_blueprint(bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
