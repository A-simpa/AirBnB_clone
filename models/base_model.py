#!/usr/bin/python3
""" definition of the base_model of console"""

import uuid
from datetime import datetime


class BaseModel:
    """ The BaseModel class for console """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """ change updated_at to the current time now"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """a proper representation all object properties"""
        rep = self.__dict__
        rep["__class__"] = "BaseModel"
        rep["updated_at"] = rep["updated_at"].isoformat()
        rep["created_at"] = rep["created_at"].isoformat()
        return rep
