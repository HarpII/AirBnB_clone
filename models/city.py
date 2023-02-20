#!/usr/bin/python3
"""
Module City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseModel
    Public attributes:
        state_id: (str)
        name: (str)
     """

    state_id = ""
    name = ""
