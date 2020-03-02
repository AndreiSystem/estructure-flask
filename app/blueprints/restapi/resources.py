from flask import jsonify, abort
from flask_restful import Resource
from app.models.products_model import Products
from app.extensions.commands import commit, save


class ProductResourse(Resource):
    def get(self, product_id=None) -> Products:
        if product_id:
            product = Products.query.filter_by(id=product_id).first() or abort(404)
            return jsonify(product.to_dict())

        products = Products.query.all() or abort(204)

        return jsonify(
            {
                'products': [
                    product.to_dict()
                    for product in products]
            }
        )

    def put(self, product_id: int, data: dict) -> Products:

        Products.query.filter_by(id=product_id).update(data)
        commit()
        get_product = self.get(product_id)
        return get_product

    def create(self, data: dict) -> Products:
        return save(Products(**data))


