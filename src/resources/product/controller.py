from resources.product.schema import products_schema, product_schema
from resources.product.model import Product
from flask_restful import Resource
from flask import request
from utils import utils
from db import db


class ProductController(Resource):
    url = "/product"

    # Get List
    def get(self):
        product_list = Product.query.all()
        return utils.generateResponse(
            {
                "body": products_schema.dump(product_list),
                "status_code": 200
            })

    # Create
    def post(self):
        name = request.json['name']
        description = request.json['description']
        new_product = Product(name, description)
        db.session.add(new_product)
        db.session.commit()
        product_saved = Product.query.order_by(
            Product.id.desc()).limit(1).all()
        return utils.generateResponse({
            "body": product_schema.dump(product_saved[0]),
            "status_code": 201
        })


class ProductIDController(Resource):
    url = '/product/<product_id>'

    # Get by id
    def get(self, product_id):
        found_product = Product.query.get(product_id)
        if found_product is None:
            return utils.generateResponse({
                "body": f"Couldn't found a product with the ID {product_id}",
                "status_code": 404})
        return utils.generateResponse(
            {"body": product_schema.dump(found_product),
             "status_code": 200})

    # Update by id
    def put(self, product_id):
        product_update = Product.query.get(product_id)
        product_update.name = request.json['name']
        product_update.likes = int(request.json['likes'])
        product_update.description = request.json['description']
        db.session.commit()
        return utils.generateResponse({
            "body": product_schema.dump(product_update), "status_code": 200})

    # Delete by id
    def delete(self, product_id):
        product_delete = Product.query.get(product_id)
        db.session.delete(product_delete)
        db.session.commit()
        return utils.generateResponse({
            "body": f"product with the ID {product_id} has been deleted successfully",
            "status_code": 202})


def add_product_resource_table(api):
    api.add_resource(ProductController, ProductController.url)
    api.add_resource(ProductIDController, ProductIDController.url)
