#!/usr/bin/python3
""" State Module for HBNB project """
from models import storage
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    #if (os.getenv(HBNB_TYPE_STORAGE) == 'db'):
     #   cities = relationship("City", backref="State", cascade="all, delete")
    #else:
    @property
    def cities(self):
        cityinst = []
        inst = storage.all(City)
        for key, value in inst.items():
            if value.state_id == self.id:
                cityinst.append(value)
        return cityinst
