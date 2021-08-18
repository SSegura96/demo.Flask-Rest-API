from flask_restful import Resource


class StatusController(Resource):
    url = "/status"

    def get(self):
        return {"msg": "Status OK"}


def add_status_resource_table(api):
    api.add_resource(StatusController, StatusController.url)
