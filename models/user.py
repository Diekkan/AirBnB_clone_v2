#!/usr/bin/python3
"""This module defines a class User"""
from os import environ as env
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user",
                          cascade="all, delete-orphan")
    reviews = relationship("Review", backref="user",
                           cascade="all, delete-orphan")
    if env.get('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place',
                              backref='city',
                              cascade='all, delete-orphan')
