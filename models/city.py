#!/usr/bin/python3
"""
This module is for the City class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
