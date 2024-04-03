from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask import Blueprint

bcrypt = Bcrypt()
jwt = JWTManager()
auth_bp = Blueprint('auth', __name__)
user_bp = Blueprint('users', __name__)
admin_bp = Blueprint('admin', __name__)
mpesa_bp = Blueprint('mpesa', __name__)