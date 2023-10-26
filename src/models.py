import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

"""class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}"""


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    name = Column(String)
    description = Column(Text)
    gender = Column(String)
    height = Column(String)
    hair_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(Integer)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    description = Column(Text)
    name = Column(String)
    image_url = Column(String)
    climate = Column(String)
    population = Column(Integer)
    terrain = Column(String)
    orbital_period = Column(Integer)
    surface_water = Column(Integer)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    name = Column(String)
    description = Column(Text)
    model_name = Column(String)
    manufacturer = Column(String)
    price = Column(Integer)


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    user = relationship(User)
    character = relationship(Character)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime)
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment = Column(Text)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(Integer)
    user = relationship(User)
    post = relationship(Post)

    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
