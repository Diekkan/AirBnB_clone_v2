#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State", cascade="all, delete-orphan")
    
    @property
    def cities(self):
        """getter cities"""
        from models import storage
        cityinst = []
        inst = storage.all(City)
        for key, value in inst.items():
            if value.state_id == self.id:
                cityinst.append(value)
        return cityinst
