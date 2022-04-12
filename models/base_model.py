#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(datetime.utcnow()), nullable=False)
    updated_at = Column(DateTime(datetime.utcnow()), nullable=False)
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.save()
        else:
            for key in kwargs:
                if key == '__class__':
                    continue
                else:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.all().update({self.to_dict()['__class__'] + '.' + str(self.id): self})
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = str(self.created_at)
        dictionary['updated_at'] = str(self.updated_at)

        return dictionary
    def delete(self):
        from models import storage
        storage.delete(self)
        storage.save()
