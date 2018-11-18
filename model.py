from datetime import datetime
from app import app
from flask_sqlalchemy import SQLAlchemy

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

    def save(self):
        db.session.add(self)
        db.session.commit()


db.drop_all()
db.create_all()
