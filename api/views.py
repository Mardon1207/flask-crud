from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/api/v1/products/<int:product_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def product_view(product_id):
    if request.method == 'GET':
        # return product
        pass
    if request.method == 'POST':
        # add new product
        pass
    if request.method == 'PUT':
        # update product
        pass
    if request.method == 'DELETE':
        # delete product
        pass


@app.route('/api/v1/products')
def all_products_view():
    # return all product
    pass