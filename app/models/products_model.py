from app.extensions.database import db
from sqlalchemy_serializer import SerializerMixin



class Products(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)
    supliers = db.Column(db.String(140))
    sku = db.Column(db.String(150))

    def __init__(self, **kwargs):
        super(Products, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.price = kwargs['price']
        self.description = kwargs['description']
        self.supliers = kwargs['supliers']
        self.sku = kwargs['sku']

