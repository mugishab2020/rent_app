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
        abort(401) 
        #pipmay be for security reasons

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user_name = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if (user_name == 'edson'):
        role=='admin'
    role = 'user'
    gender = data.get('gender')

    if not(user_name and email and password):
        return jsonify({'message': 'Please fill all fields'}), 400
    existing_user = User.query.filter_by(username=user_name).first()
    if existing_user:
        return jsonify({'Error': 'Usermane already exists'}), 409
    
    hash_password = generate_password_hash(password)

    new_user = User(username=user_name, email=email, password=hash_password, gender=gender, role=role)
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

@bp.route('/clients', methods=['GET'])
def get_clients():
    
    clients = User.query.all()
    print (clients)
    result = [{'clientID': User.id, 'Username': User.username,
               'Email': User.email, 'Gender': User.gender, 'Role': User.role} for user in clients]
    return jsonify(result)

@bp.route('/rented_cars', methods=['GET'])
def get_rented_cars():
    rented_cars = Car.query.filter_by(rent_status=True).all()  # Query for rented cars
    rented_cars_data = []  # List to store rented car details

    for car in rented_cars:
        rented_car_info = {
            'car_id': car.id,
            'car_name': car.carName,
            'user_id': car.user_id  
        }
        rented_cars_data.append(rented_car_info)

    return jsonify(rented_cars_data)

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