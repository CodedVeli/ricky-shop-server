from flask import Flask
from flask_migrate import Migrate
from .models.model import db
from .extensions import bcrypt, jwt
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = '35d7ddbd85a857199b244479'
    bcrypt.init_app(app)
    jwt.init_app(app)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')  

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecom.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    CORS(app)

    db.init_app(app)
    Migrate(app, db)
    from .routes import auth_bp, user_bp, admin_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/users')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    from .mpesaapi import mpesa_bp
    app.register_blueprint(mpesa_bp, url_prefix='/mpesa')
    with app.app_context(): 
        db.create_all()

    return app

JWT_SECRET_KEY = '8yrsxifxhsgvcjj8t58jj'
FLASK_JWT_SECRET_KEY ='35d7ddbd85a857199b244479'