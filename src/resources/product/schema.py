from flask_marshmallow import Marshmallow


ma = Marshmallow()


class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "likes", "description")


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
