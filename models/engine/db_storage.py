#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage():
    """ Database Storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """create engine"""

        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if (env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all objs depending on cls name"""
        new_dict = {}
        if cls is None:
            for clase in Base.__subclasses__():
                obj_list = self.__session.query(clase).all()
                for element in obj_list:
                    new_dict[str(type(element).__name__) +
                             '.' + str(element.id)] = element
            return (new_dict)
        else:
            obj_list = self.__session.query(cls).all()
            for element in obj_list:
                delattr(element, '_sa_instance_state')
                new_dict[str(type(element).__name__) +
                         '.' + str(element.id)] = element
            return (new_dict)

    def new(self, obj):
        """ add obj to current session"""
        self.__session.add(obj)

    def save(self, obj=None):
        """commit changes to curr session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj if not none"""
        if ob is not None:
            self.__session.delete(obj)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        sess_fact = sessionmaker(expire_on_commit=False, bind=self.__engine)
        Session = scoped_session(sess_fact)
        self.__session = Session()
