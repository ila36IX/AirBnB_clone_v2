#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # This is for DBStorage
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', cascade='all, delete',
                             secondary=place_amenity,
                             backref="places",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        # this is for FileStorage
        @property
        def reviews(self):
            """list of review instance """
            rev_list = []
            for rev in self.reviews:
                if rev.place_id == self.id:
                    review_list.append(rev)

            return (rev_list)

        @property
        def amenities(self):
            """method to return all list of Amenity instance"""
            from models import storage
            from models.amenity import Amenity
            amenities_instances = storage.all(Amenity)
            place_amenites = []
            for amenity_id in self.amenity_ids:
                for amenity in amenities_instances:
                    if amenity.id == amenity_id:
                        place_amenites.append(amenity)
            return place_amenites

        @amenities.setter
        def amenities(self, amenity_id):
            """setter method to handle append method"""
            amenity_id.append(amenity_id)
