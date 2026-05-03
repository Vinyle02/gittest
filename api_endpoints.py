# Product Catalog API Endpoints
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({"products": []})

@app.route('/api/products/<sku>', methods=['GET'])
def get_product(sku):
    return jsonify({"sku": sku, "name": "", "price": 0})

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    return jsonify({"status": "created"}), 201
