from db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    likes = db.Column(db.Integer)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.likes = 0
        self.description = description
