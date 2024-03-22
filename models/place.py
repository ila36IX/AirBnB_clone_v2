#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

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
    
    # this is for DBStorage
    reviews = relationship('Review', cascade='all, delete', backref='place')
    amenities = relationship('Amenity', cascade='all, delete',
                            backref='place_amenity',
                            secondary=place_amenity,
                            viewonly=False)

    #this is for FileStorage
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
        pass

    @amenities.setter
    def amenities(self):
        """setter method to handle append method"""
        pass
