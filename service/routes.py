from flask import Flask, jsonify, request, abort
from myfactoryapp.models import Product 
from myfactoryapp import app, db  
@app.route('/products/<int:id>/', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.serialize())

@app.route('/products/<int:id>/', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.name = data.get('name', product.name)
    product.category = data.get('category', product.category)
    product.availability = data.get('availability', product.availability)
    db.session.commit()
    return jsonify(product.serialize())

@app.route('/products/<int:id>/', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204

@app.route('/products/', methods=['GET'])
def list_all_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products])

@app.route('/products/', methods=['GET'])
def list_products_by_name():
    name = request.args.get('name')
    products = Product.query.filter_by(name=name).all()
    return jsonify([product.serialize() for product in products])

@app.route('/products/', methods=['GET'])
def list_products_by_category():
    category = request.args.get('category')
    products = Product.query.filter_by(category=category).all()
    return jsonify([product.serialize() for product in products])

@app.route('/products/', methods=['GET'])
def list_products_by_availability():
    availability = request.args.get('availability', type=bool)
    products = Product.query
