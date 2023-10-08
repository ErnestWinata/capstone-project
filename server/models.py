from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from config import db


user_city_association = db.Table(
    'user_city',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('city_id', db.Integer, db.ForeignKey('cities.id'))
)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    cities = relationship('City', secondary=user_city_association, backref='users')

    city_names = association_proxy('cities', 'name')

    def __repr__(self):
        return f'<User {self.username}>'

class City(db.Model, SerializerMixin):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_of_visit = db.Column(db.Date, nullable=False)
    best_memories = db.Column(db.Text, nullable=False)
    accommodation = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<City {self.name}>'
