from flask import request, jsonify
from ..models.model import User
from app import db
from app.extensions import bcrypt
from app.signupemail import send_signup_email
from dotenv import load_dotenv
import os
from validate_email_address import validate_email
import re
import random
import smtplib
from jinja2 import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, create_refresh_token


def is_valid_email_format(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# def is_valid_email(email):
#     is_valid = validate_email(email, verify=True)
#     return is_valid

load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
subject = os.getenv('SUBJECT')
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, 'signup.html')

with open(file_path, 'r') as body:    body = body.read()

def send_otp_email_signup(user_email, otp):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = 'Your Ricky\'s Shop  OTP'

    template = Template("Hello,\n\nYour OTP is: {{ otp }}.\n\nOTP Expires in 2 hours.\n\nThank you.")
    
    email_body = template.render(otp=otp)

    msg.attach(MIMEText(email_body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, user_email, text)
    server.quit()


def create_user():
    data = request.get_json()
    email = data['email']
    if not is_valid_email_format(email):
        return jsonify({'message': 'Please enter a valid email'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400
    user = User(name=data['name'], email=email, password=data['password'], address=data['address'], phone=data['phone'], city=data['city'],verified=False)
    user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user.address = ''.join(data['address'])
    db.session.add(user)
    otp = random.randint(100000, 999999)
    user.otp_hash = generate_password_hash(str(otp))
    user.otp_expiration = datetime.utcnow() + timedelta(hours=2)  # OTP expires after 10 minutes
    db.session.commit()
    send_otp_email_signup(email, otp)
    return jsonify({'message': 'An OTP code has been sent to your email'}), 200


  
def verify_otp_signup():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')
    if not email or not otp:
        return jsonify({'message': 'Email and OTP are required'}), 400
    user = User.query.filter_by(email=email).first()
    if user:
        if user.otp_hash is None:
            return jsonify({'message': 'Resend OTP request'}), 400
        if not check_password_hash(user.otp_hash, str(otp)):
            return jsonify({'message': 'Invalid OTP'}), 400
        if datetime.utcnow() > user.otp_expiration:
            return jsonify({'message': 'OTP has expired'}), 400
        recipient_email = email
        user.otp_hash = None
        user.otp_expiration = None
        user.verified = True
        db.session.commit()
        send_signup_email(sender_email, sender_password, recipient_email, subject, body)        return jsonify({'message': 'OTP verified successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

def send_otp_email(user_email, otp):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = user_email
    msg['Subject'] = 'Your Ricky\'s Shop  OTP'

    template = Template("Hello,\n\nYour OTP is: {{ otp }}.\n\nOTP Expires in 10 minutes.\n\nThank you.")
    
    email_body = template.render(otp=otp)

    msg.attach(MIMEText(email_body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, user_email, text)
    server.quit()

def forgot_password():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'message': 'Email is required'}), 400
    if not is_valid_email_format(email):
        return jsonify({'message': 'Invalid email format'}), 400
    # if not is_valid_email(email):
    #     return jsonify({'message': 'Please enter a valid email'}), 400
    user = User.query.filter_by(email=email).first()
    if user:
        otp = random.randint(100000, 999999)
        user.otp_hash = generate_password_hash(str(otp))
        user.otp_expiration = datetime.utcnow() + timedelta(minutes=10)  # OTP expires after 10 minutes
        db.session.commit()
        send_otp_email(email, otp)
        return jsonify({'message': 'An OTP code has been sent to your email'}), 200
    return jsonify({'message': 'User not found'}), 404


def verify_otp():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')
    if not email or not otp:
        return jsonify({'message': 'Email and OTP are required'}), 400
    user = User.query.filter_by(email=email).first()
    if user:
        if user.otp_hash is None:
            return jsonify({'message': 'Resend OTP request'}), 400
        if not check_password_hash(user.otp_hash, str(otp)):
            return jsonify({'message': 'Invalid OTP'}), 400
        if datetime.utcnow() > user.otp_expiration:
            return jsonify({'message': 'OTP has expired'}), 400
        user.otp_hash = None
        user.otp_expiration = None
        db.session.commit()
        access_token = create_access_token(identity=user.id,expires_delta=timedelta(days=5))
        refresh_token = create_refresh_token(identity=user.id, expires_delta=timedelta(days=6))
        return jsonify(
            {   
                'message': 'OTP verified successfully',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
                    ), 201
    return jsonify({'message': 'User not found'}), 404

def update_password():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400
    user = User.query.filter_by(email=email).first()
    if user:
        user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        db.session.commit()
        return jsonify({'message': 'Password updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        user.address = data['address']
        user.phone = data['phone']
        user.city = data['city']
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404



def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.serialize()), 200
    return jsonify({'message': 'User not found'}), 404

def get_user_orders(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify([order.serialize() for order in user.orders]), 200
    return jsonify({'message': 'User not found'}), 404
