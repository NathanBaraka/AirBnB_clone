#!/usr/bin/python3
"""
This module is for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The class User that handles users' info
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
