#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # I have no Idea if this will work without this line
        # from models import storage
        self.id = kwargs.get("id", str(uuid.uuid4()))
        # <name>_t referes to time
        str_t = datetime.strptime
        now_t = datetime.utcnow
        format_t = "%Y-%m-%dT%H:%M:%S.%f"
        created_t = kwargs.get("created_at", now_t().isoformat())
        updated_t = kwargs.get("updated_at", now_t().isoformat())
        kwargs['created_at'] = str_t(created_t, format_t)
        kwargs['updated_at'] = str_t(updated_t, format_t)
        kwargs.pop('__class__', None)
        self.__dict__.update(kwargs)
        # storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.to_dict())

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop("_sa_instance_state", None)
        return dictionary

    def delete(self):
        """usage: delete object"""
        storage.delete(self)
