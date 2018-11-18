from app import app, api
from resources.user import HelloWorld, UserResource


api.add_resource(HelloWorld, '/')
api.add_resource(UserResource, '/user')


if __name__ == '__main__':
    app.run(debug=True)