#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship('Review',
                               backref='place', cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """getter attr returns list insts on place_id == Place.id"""
            from models import storage
            revinst = []
            inst = storage.all(Review)
            for key, value in inst.items():
                if value.place_id == self.id:
                    revinst.append(value)
            return revinst
