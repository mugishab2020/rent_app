from flask import Blueprint, jsonify, request,render_template
from flask_bcrypt import Bcrypt
from datetime import date
from models import db
from models import Car, User
bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return 'This is the home page of the app'


@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')

    # Validate user input (e.g., check for required fields, validate email format)

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user object
    new_user = User(username=username, email=email, password=hashed_password, gender=gender)

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

@bp.route('/cars', methods=['POST','GET'])
def get_cars():
    cars = Car.query.all()
    result = [{'carID': car.carID, 'maker': car.maker, 'released_year': car.released_year} for car in cars]
    return jsonify(result)

@bp.route('/clients', methods=['POST','GET'])
def get_clients():
    clients = User.query.all()
    result = [{'clientID': User.clientID, 'firstname': User.firstname, 'lastname': User.lastname,
               'remain': User.remain, 'age': User.age, 'address': User.address} for client in clients]
    return jsonify(result)

@bp.route('/rented_cars', methods=['POST','GET'])
def get_rented_cars():
    rented_cars = Car.query.all()
    if Car.rent_status==True:
        result = [{'id': car.id, 'carID': car.carID, 'clientID': car.clientID, 'rent_status' : Car.rent_status, 'date_taken': car.date_taken,
            'returning_date': car.returning_date, 'cost_per_day': car.cost_per_day} for car in rented_cars]
    return jsonify(result)

@bp.route('/rent_car', methods=['POST','POST'])
def rent_car():
    data = request.json
    if Car.rent_status == False:
        new_rental = Car(carID=data['carID'], clientID=data['clientID'], date_taken=date.today(),
                            returning_date=data['returning_date'], cost_per_day=data['cost_per_day'])
        db.session.add(new_rental)
        db.session.commit()
        return jsonify({'message': 'Car rented successfully'}), 201
