#!/usr/bin/python3
"""
Module Review Class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    Public attributes:
        user_id: (str)
        place_id: (str)
        text: (str)
    """
    place_id = ""
    user_id = ""
    text = ""
