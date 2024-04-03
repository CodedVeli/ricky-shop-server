from flask import request, jsonify
from ..models.model import Category
from app import db

def create_category():
    data = request.get_json()
    category = Category(name=data['name'], description=data['description'], products=[])
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created successfully'}), 201

def get_categories():
    categories = Category.query.all()
    return jsonify([category.serialize() for category in categories]), 200

def delete_category(category_id):
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'}), 200
    return jsonify({'message': 'Category not found'}), 404