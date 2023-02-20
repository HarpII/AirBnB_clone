#!/usr/bin/python3
"""
Module User Class
"""
from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    Inherits from BaseModel
    Public attributes:
        email: (str)
        password: (str)
        first_name: (str)
        last_name: (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
