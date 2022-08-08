#!/usr/bin/python3
"""definition of City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherits from BaseModel"""

    state_id = ""
    name = ""
