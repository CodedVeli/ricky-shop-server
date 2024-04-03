from flask import request, jsonify
from ..models.model import Product, Image
from app import db

def create_product():
    data = request.get_json()
    product = Product(name=data['name'], description=data['description'], price=data['price'], category_id=data['category_id'], image=[], user_id=data['user_id'])
    images_data = data.pop('image', [])
    image = [Image(url=image) for image in images_data]
    product.image = image


    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products]), 200

def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200
    return jsonify({'message': 'Product not found'}), 404

def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.category_id = data['category_id']
        product.image=[]
        product.user_id=data['user_id']
        images_data = data.pop('image', [])
        image = [Image(url=image) for image in images_data]
        product.image = image

        db.session.commit()
        return jsonify({'message': 'Product updated successfully'}), 200
    return jsonify({'message': 'Product not found'}), 404

def get_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify(product.serialize()), 200
    return jsonify({'message': 'Product not found'}), 404