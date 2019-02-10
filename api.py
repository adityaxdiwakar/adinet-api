from disc import canary, stable, ptb
from trello import update as trello

from flask import Flask, request
from flask_restful import Api, Resource, reqparse

import time, json

#initiializing the flask webapp
app = Flask(__name__)
api = Api(app)

#writing canary endpoints
api.add_resource(canary.cbuilds, "/discord/canary/builds")
api.add_resource(canary.cretrieve_build, "/discord/canary/builds/<string:build_num>")
api.add_resource(canary.clatest, "/discord/canary/builds/latest") 

#writing ptb endpoints
api.add_resource(ptb.pbuilds, "/discord/ptb/builds")
api.add_resource(ptb.pretrieve_build, "/discord/ptb/builds/<string:build_num>")
api.add_resource(ptb.platest, "/discord/ptb/builds/latest")

#writing stable endpoints
api.add_resource(stable.sbuilds, "/discord/stable/builds")
api.add_resource(stable.sretrieve_build, "/discord/stable/builds/<string:build_num>")
api.add_resource(stable.slatest, "/discord/stable/builds/latest")

#writing trello endpoint
api.add_resource(trello.latest, "/trello")

#running and setting host port (local for nginx reverse proxy)
app.run(host='127.0.0.1', port=1337)
