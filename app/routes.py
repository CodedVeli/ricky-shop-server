from flask import  request, jsonify
from .extensions import  jwt, admin_bp, user_bp, auth_bp, bcrypt
from .models.model import User, TokenBlocklist, db
from flask_jwt_extended import  create_access_token, create_refresh_token, jwt_required, get_jwt, current_user, get_jwt_identity
from app.controllers.user_controller import create_user, get_users, delete_user, update_user, get_user, get_user_orders, forgot_password, verify_otp, update_password
from app.controllers.product_controller import create_product, get_products, delete_product, update_product, get_product
from app.controllers.category_controller import create_category, get_categories, delete_category
from app.controllers.order_controller import create_order, get_orders, delete_order
from datetime import timedelta

#  Auth routes
# register route
@auth_bp.route('/register', methods=['POST'])
def register():
    return create_user()

# login route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    password = data['password']
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id,expires_delta=timedelta(days=5))
        refresh_token = create_refresh_token(identity=user.id, expires_delta=timedelta(days=6))
        return jsonify(
            {   
                'message': 'Login successful',
                'access_token': access_token,
                'refresh_token': refresh_token
            }
                    ), 201
    return jsonify({'message': 'Invalid email or password'}), 401

@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == 4:
        return{"is_admin": True}
    return {"is_admin": False}

# jwt error handlers

# jwt tokens expired
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({'message': 'Token has expired', 'error': 'token_expired'}), 401

# jwt token missing
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"message": "Request doesnt contain a valid token", "error":"authorization_header"}), 401

# jwt token invalid 
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"message": "Signature verification failed", "error":"invalid_token"}), 401

# jwt token not found
@jwt.user_lookup_loader
def user_lookup_callback(__jwt_headers,jwt_data):
    identity = jwt_data['sub']
    return User.query.filter_by(id=identity).one_or_none()

@auth_bp.get('/whoami')
@jwt_required()
def whoami():
    claims = get_jwt()
    return jsonify({'message': 'You are authenticated', 'user_details': {'name': current_user.name, 'email': current_user.email, 'id': current_user.id}, 'claims':{ 'user': claims}}), 200  

@auth_bp.get('/refresh')
@jwt_required(refresh=True)
def refresh():    
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user, expires_delta=timedelta(hours=2))
    return jsonify({'access_token': access_token}), 200

# tokenbloclist blocker 
@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_data):
    jti = jwt_data['jti']
    token = TokenBlocklist.query.filter_by(jti=jti).first()
    return token is not None

@auth_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']
    token = TokenBlocklist(jti=jti)
    db.session.add(token)
    db.session.commit()
    return jsonify({'message': 'Successfully logged out'}), 200


# user routes
@user_bp.get('/users')
@jwt_required()
def get_user_(user_id):
    return get_user(user_id)

@user_bp.route('/orders', methods=['GET'])
@jwt_required()
def get_user_orders_():
    return get_user_orders()

@user_bp.route('/all', methods=['GET'])
@jwt_required()
def get_all_user():
    claims = get_jwt()
    if claims['is_admin']:
        return get_users()
    return jsonify({'message': 'You are not authorized this access'}), 401

@user_bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_(user_id):
    return delete_user(user_id)

@user_bp.route('/update/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_(user_id):
    return update_user(user_id)

# product routes

@admin_bp.route('/post_products', methods=['POST'])
@jwt_required()
def create__product():
    claims = get_jwt()
    if claims['is_admin']:
        return create_product()
    return jsonify({'message': 'You are not authorized this access'}), 401
    # return create_product()

@user_bp.route('/get_products', methods=['GET'])
def get_products_():
    return get_products()

@user_bp.route('/delete_product/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product_(product_id):
    claims = get_jwt()
    if claims['is_admin']:
        return delete_product(product_id)
    return jsonify({'message': 'You are not authorized this access'}), 401

@user_bp.route('/update_product/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product_(product_id):
    claims = get_jwt()
    if claims['is_admin']:
        return update_product(product_id)
    return jsonify({'message': 'You are not authorized this access'}), 401

@user_bp.route('/get_product/<int:product_id>', methods=['GET'])
def get_product_(product_id):
    return get_product(product_id)

# category routes

@admin_bp.route('/post_category', methods=['POST'])
@jwt_required()
def create_category_():
    claims = get_jwt()
    if claims['is_admin']:
        return create_category()
    return jsonify({'message': 'You are not authorized this access'}), 401
    # return create_category()

@user_bp.route('/get_categories', methods=['GET'])
@jwt_required()
def get_categories_():
    return get_categories()

@admin_bp.route('/delete_category/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category_(category_id):
    claims = get_jwt()
    if claims['is_admin']:
        return delete_category(category_id)
    return jsonify({'message': 'You are not authorized this access'}), 401

# order routes

@user_bp.route('/post_order', methods=['POST'])
@jwt_required()
def create_order_():
    return create_order()

@user_bp.route('/get_orders', methods=['GET'])
@jwt_required()
def get_orders_():
    return get_orders()

@user_bp.route('/delete_order/<int:order_id>', methods=['DELETE'])
@jwt_required()
def delete_order_(order_id):
    return delete_order(order_id)

#  forgot password route    
@auth_bp.route('/forgot_password', methods=['POST'])
def forgot_password_():
    return forgot_password()

@auth_bp.route('/verify_otp', methods=['POST'])
def verify_otp_():
    return verify_otp()

@auth_bp.route('/update_password', methods=['PATCH'])
@jwt_required()
def update_password_():
    return update_password()


