from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Float, DateTime, Column
#from sqlalchemy import Column


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://database:mugishab2020@localhost/mydatabase' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    orders = db.relationship('Order', backref='User', lazy=True)
    payments = db.relationship('Payment', backref='User', lazy=True)

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rent_status = db.Column(db.Boolean, default=False)
    registration_number = db.Column(db.String(20), unique=True, nullable=False)
    rental_price = db.Column(db.Float, nullable=False)
    rent_status = db.Column(db.Boolean, default=False)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.Boolean, default=False)

    def rent_car(cls, car_id):
        car = Car.query.get(car_id)
        if car:
            car.rent_status = True
            db.session.commit()
            return True
        return False

    @classmethod
    def return_car(cls, car_id):
        car = Car.query.get(car_id)
        if car:
            car.rent_status = False
            db.session.commit()
            return True
        return False

    

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='admin', uselist=False)

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    payment_amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    
