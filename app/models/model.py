from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(70),unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False) 
    city = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)    
    orders = db.relationship('Order', backref='user', lazy=True)
    created_at =db.Column(db.DateTime,default = datetime.utcnow)
    otp_hash = db.Column(db.String(128))
    otp_expiration = db.Column(db.DateTime)
    verified = db.Column(db.Boolean, default=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'address': self.address,
            'city': self.city,
            'phone': self.phone,
            'orders': [order.serialize() for order in self.orders],
            'otp_hash': self.otp_hash,
            'otp_expiration': self.otp_expiration,
            'created_at': self.created_at
        }
order_product = db.Table('order_product',
         db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
         db.Column('product_id',  db.Integer, db.ForeignKey('product.id'), primary_key=True)             
 ) 

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key = True, unique=True ,nullable=False)
    name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Float,nullable=False )
    image = db.relationship('Image', backref='product', lazy=True)
    created_at =db.Column(db.DateTime,default = datetime.utcnow)
    updated_at = db.Column(db.DateTime,default = datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': [image.serialize() for image in self.image],
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'category_id': self.category_id
        }    




class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key = True, unique=True ,nullable=False)
    url = db.Column(db.String(50),nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'url': self.url,
            'product_id': self.product_id
        }

 

class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='pending')
    delivery_method = db.Column(db.String(50), default='pickup')  
    payment_method = db.Column(db.String(50), default='cash')
    shipping_cost = db.Column(db.Float, default=0)
    created_at =db.Column(db.DateTime,default = datetime.utcnow)
    products = db.relationship('Product', secondary=order_product)


    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'total': self.total,
            'quantity': self.quantity,
            'products': [product.serialize() for product in self.products],
            'status': self.status,
            'delivery_method': self.delivery_method,
            'created_at': self.created_at
        } 





class Category(db.Model):
    __tablename__ = 'category'  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    def serialize(self):
        return { 
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'products': [product.serialize() for product in self.products]
        }

class TokenBlocklist(db.Model):
    __tablename__ = 'token_blocklist'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'jti': self.jti,
            'created_at': self.created_at
        }    