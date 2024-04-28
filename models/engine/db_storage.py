#!/usr/bin/python3
"""THe database engine"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """The databse engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor of the DBStorage engine"""
        env_vars = [
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")
        ]
        db_info = "mysql+mysqldb://{}:{}@{}/{}".format(*env_vars)
        self.__engine = create_engine(db_info, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            print("Warning! This is a testing envirnement!")
            print(f"Everything will be deleted in {env_vars[3]}")
            metadata = MetaData()
            metadata.reflect(self.__engine)
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current db depending of the class name"""
        objects = {}
        classes = [User, State, City, Place, Review]
        if cls is not None:
            classes = [cls]
        for cls in classes:
            query = self.__session.query(cls)
            for row in query.all():
                key = cls.__name__ + '.' + row.id
                objects[key] = row

        return (objects)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.query(type(obj)).filter_by(id=obj.id).delete()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """releasing any connection/transactional resources owned by session"""
        self.__session.remove()
