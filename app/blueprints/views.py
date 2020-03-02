from flask import render_template, abort, request

from app.blueprints.restapi import ProductResourse
from app.models.products_model import Products



def init_app(app):
    # Views
    @app.route('/')
    def index():
        products = Products.query.all()
        return render_template('index.html', products=products)

    @app.route('/products/<int:product_id>', methods=['GET'])
    def get_product(product_id) -> Products:
        Product = ProductResourse()
        product = Product.get(product_id)
        return product or abort(200)

    @app.route('/products/', methods=['GET'])
    def get_all() -> tuple:
        Product = ProductResourse()
        product = Product.get()
        return product, 200 or abort(404)

    @app.route('/products/<int:product_id>', methods=['PUT'])
    def put(product_id: int) -> tuple:
        data = request.get_json()
        Product = ProductResourse()
        product_update = Product.put(product_id, data)
        return product_update, 200

    @app.route('/products/', methods=['POST'])
    def post() -> tuple:
        data = request.get_json()
        Product = ProductResourse()
        print(data)
        product_create = Product.create(data)
        return product_create.to_dict() or abort(404)