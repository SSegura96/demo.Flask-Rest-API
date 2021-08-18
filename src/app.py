from resources.status.controller import add_status_resource_table
from resources.product.controller import add_product_resource_table
from dotenv import load_dotenv
from flask_restful import Api
from os import environ as env
from flask import Flask
import os


# Load .env file
load_dotenv()

# Init app
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
api = Api(app)


# DB Settigns
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = env['TRACK_MODIFICATIONS']
app.config['SQLALCHEMY_DATABASE_URI'] = env['DB_CONNECTION_STRING']


@app.before_first_request
def create_tables():
    from db import db
    db.init_app(app)
    db.create_all()


# End Points Routes
add_product_resource_table(api)
add_status_resource_table(api)


if __name__ == "__main__":
    app.run(port=env['API_PORT'], debug=env['DEBUG_MODE_ON'])
