#general requirements
import time, json, os

#environemnt information
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('/home/api') / '.env'
load_dotenv(dotenv_path=env_path)

#loading builds flatfile
with open("bin/stable.json", "r") as f:
    stable_builds = json.load(f)

#API dependencies
from flask import Flask
from flask_restful import Api, Resource, reqparse

class sbuilds(Resource):
    def get(self):
        return stable_builds
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("build_id")
        parser.add_argument("build_num")
        parser.add_argument("build_hash")
        parser.add_argument("build_time")
        parser.add_argument("secret")
        args = parser.parse_args()
        if args["secret"] != os.getenv('API_TOKEN'):
            return "Authorization denied", 401
        for build in stable_builds:
            if build['build_id'] == args['build_id']:
                return f"Build with Build ID {build['build_id']} already exists", 400

        build = {
            "build_id": args["build_id"],
            "build_num": args["build_num"],
            "build_hash": args["build_hash"],
            "build_rel_time": args["build_time"]
        }
        stable_builds.append(build)
        with open("bin/stable.json", "w") as f:
            json.dump(stable_builds, f, indent=1)
        return build, 201

class slatest(Resource):
    def get(self):
        build_num = -1
        seeked = {}
        for build in stable_builds:
            if int(build['build_num']) > int(build_num):
                build_num = build['build_num']
                seeked = build
        return seeked, 200

class sretrieve_build(Resource):
    def get(self, build_num):
        for build in stable_builds:
            if build['build_num'] == build_num:
                return build, 200
        return f"Could not find the requested build on storage", 404
