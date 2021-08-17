from resources.status.controller import StatusController
from resources.product.controller import ProductController
from flask_restful import Api
from flask import Flask
import os


# Init app
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
api = Api(app)


# DB Settigns
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basedir, "db.sqlite")


@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()


# End Points Routes
api.add_resource(ProductController, ProductController.url)
api.add_resource(StatusController, StatusController.url)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
