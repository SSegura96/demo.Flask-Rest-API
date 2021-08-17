from resources.product.schema import products_schema
from resources.product.model import Product
from flask_restful import Resource
from flask import request
from db import db
import json


class ProductController(Resource):
    url = "/product"

    def get(self):
        product_list = Product.query.all()
        return products_schema.dump(product_list)

    def post(self):
        name = request.json['name']
        description = request.json['description']
        new_product = Product(name, description)
        print(new_product)
        db.session.add(new_product)
        db.session.commit()
        return json.dumps({"msg": "all good"})
