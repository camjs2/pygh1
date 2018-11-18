from flask_restful import Resource
# import sys
# sys.path.append("..")

from model import User

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class UserResource(Resource):
    def post(self):
        user = User("xxx", "yyy", "zzz")
        user.save()
        return {'saved': 'true'}