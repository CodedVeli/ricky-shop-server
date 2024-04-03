from flask import request, jsonify
from ..models.model import Order, order_product
from app import db

def create_order():
    data = request.get_json()

    order = Order(
        user_id=data['user_id'], 
        quantity=data['quantity'], 
        total=data['total'], 
        status=data['status'],
        delivery_method=data['delivery_method'], 
        payment_method=data['payment_method'],
        shipping_cost=data['shipping_cost']
    )

    db.session.add(order)
    db.session.flush()  

    for product in data['products']:
        order_product_relation = order_product.insert().values(
            order_id=order.id, 
            product_id=product['id']
        )
        db.session.execute(order_product_relation)

    db.session.commit()

    return jsonify({'message': 'Order created successfully'}), 201

def get_orders():
    orders = Order.query.all()
    return jsonify([order.serialize() for order in orders]), 200

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    return jsonify({'message': 'Order not found'}), 404

def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'}), 200
    return jsonify({'message': 'Order not found'}), 404