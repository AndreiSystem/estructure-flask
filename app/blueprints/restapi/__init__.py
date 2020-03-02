from flask import Blueprint
from flask_restful import Api
from .resources import ProductResourse
# ProductItemResource, ProductResourseUpgrade

# blueprint
bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)
api.add_resource(ProductResourse, '/products/')
api.add_resource(ProductResourse, '/products/<int:product_id>', endpoint='product')

def init_app(app):
    app.register_blueprint(bp)