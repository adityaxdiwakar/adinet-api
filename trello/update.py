import time, json

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

class latest(Resource):
        def post(self):
                with open("logs.txt", "w") as f:
                        f.write(str(request.json))
                return "", 200

        def head(self):
                return "", 200
