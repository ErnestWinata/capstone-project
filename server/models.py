from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    cities = db.relationship('City', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'
    
class City(db.Model, SerializerMixin):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    date_of_visit = db.Column(db.Date, nullable=False)
    best_memories = db.Column(db.Text, nullable=False)
    accomodation = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullalbe=False)

    def __repr__(self):
        return f'<City {self.name}>'
    
user_city_association = db.Table('user_city',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('city_id', db.Integer, db.ForeignKey('cities.id'), primary_key=True)
)