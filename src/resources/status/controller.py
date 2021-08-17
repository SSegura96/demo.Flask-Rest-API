from flask_restful import Resource


class StatusController(Resource):
    url = "/status"

    def get(self):
        return {"msg": "Status OK"}
