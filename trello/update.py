import time, json

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

class latest(Resource):
        def post(self):
                with open("logs.json", "r") as f:
                        data = json.load(f)
                data.append(request.json)
                with open("logs.json", "w") as f:
                        json.dump(data, f, indent=4)
                return "", 200

        def head(self):
                return "", 200
