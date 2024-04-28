#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """Get all city objects linked to the current State"""
        from models import storage
        from models.city import City
        cities = []
        for instance in storage.all(City).values():
            if instance.state_id == self.id:
                cities.append(instance)
        return cities
