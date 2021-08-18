from flask import Response
import json


def generateResponse(response):
    resp = Response(json.dumps({'msg': response["body"]}),
                    status=response["status_code"],
                    mimetype='application/json')
    return resp
