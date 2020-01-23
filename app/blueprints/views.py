from flask import render_template, abort
from app.models.products_model import Products



def init_app(app):
    # Views
    @app.route('/')
    def index():
        products = Products.query.all()
        return render_template('index.html', products=products)

    @app.route('/product/<product_id>')
    def product(product_id):
        product = Products.query.filter_by(id=product_id).first() or abort(404, 'produto nao encontrado')

        return render_template('product.html', product=product)