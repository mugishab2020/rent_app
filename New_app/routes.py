from flask import Blueprint, jsonify, request,render_template, redirect, url_for, session
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash
from datetime import date
#from flask_cors import CORS
from models import db
from flask import abort
from models import Car, User
from werkzeug.security import check_password_hash

bp = Blueprint('routes', __name__)



@bp.route('/login', methods=['POST'])
def login():
    user_name = request.json.get('username')
    password = request.json.get('password')
    
    user = User.query.filter_by(username=user_name).first()
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'wrong credintials'}), 401
        #abort(401) may be for security reasons

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user_name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender')

    if not(user_name and email and password):
        return jsonify({'message': 'Please fill all fields'}), 400
    existing_user = User.query.filter_by(username=user_name).first()
    if existing_user:
        return jsonify({'Error': 'Usermane already exists'}), 409
    
    hash_password = generate_password_hash(password)

    new_user = User(username=user_name, email=email, password=hash_password, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 200

@bp.route('/cars', methods=['GET'])
def get_cars():
    if request.method == 'GET':
        cars = Car.query.all()
        car_list = []
        for car in cars:
            car_info = {
                'id': car.id,
                'model': car.model,
                'car_name': car.carName,
                'automatic': car.automatic,
                'speed': car.speed,
                'price': car.rental_price,
                'rent_status': car.rent_status,
                
            }
            car_list.append(car_info)
    return jsonify(car_list)

@bp.route('/clients', methods=['POST','GET'])
def get_clients():
    clients = User.query.all()
    result = [{'clientID': User.clientID, 'firstname': User.firstname, 'lastname': User.lastname,
               'remain': User.remain, 'age': User.age, 'address': User.address} for client in clients]
    return jsonify(result),200

@bp.route('/rented_cars', methods=['POST','GET'])
def get_rented_cars():
    rented_cars = Car.query.all()
    if Car.rent_status==True:
        result = [{'id': car.id, 'carID': car.carID, 'clientID': car.clientID, 'rent_status' : Car.rent_status, 'date_taken': car.date_taken,
            'returning_date': car.returning_date, 'cost_per_day': car.cost_per_day} for car in rented_cars]
    return jsonify(result)

@bp.route('/rent_car/<int:user_id>', methods=['GET'])
def list_rented_cars(user_id):
    
    rentals = Car.query.filter_by(user_id=user_id).all()
    rented_car_ids = [rental.car_id for rental in rentals]
    cars = Car.query.filter(Car.id.in_(rented_car_ids)).all()
    car_list = []
    for car in cars:
        car_info = {
            'id': car.id,
            'model': car.model,
            'car_name': car.car_name,
            'automatic': car.automatic,
            'speed': car.speed,
            'price': car.price,
            'img_url': car.img_url
        }
        car_list.append(car_info)
    
    return jsonify(car_list), 200