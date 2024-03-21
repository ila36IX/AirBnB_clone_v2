#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """The cities property. for file Storage"""
        cities = []
        for instance in storage.all().values():
            if type(instance) is City and instance.state_id == self.id:
               cities.append(instance) 
        return cities
