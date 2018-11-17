from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    pwd_hash = db.Column(db.String(50), unique=False, nullable=True)
    forename = db.Column(db.String(25), unique=False, nullable=False)
    surname = db.Column(db.String(25), unique=False, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, username,  forename, surname):
        self.username = username
        self.forename = forename
        self.surname = surname


db.drop_all()
db.create_all()
user = User("camjs2", "james", "sadler")
db.session.add(user)
db.session.commit()


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)