"""Module Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Inherits from BaseModel
    Public attributes:
        user_id: (str)
        city_id: (str)
        name: (str)
        description: (str)
        number_rooms: (int)
        number_bathrooms: (int)
        max_guest: (int)
        price_by_night: (int)
        latitude: (float)
        longitude: (float)
        amenity_ids: (str)
     """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""