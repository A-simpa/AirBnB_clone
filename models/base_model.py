#!/usr/bin/python3
""" definition of the base_model of console"""


import uuid
from datetime import datetime


class BaseModel:
    """The BaseModel class for console"""

    def __init__(self, *args, **kwargs):
        """args allow multiple arguments while kwargs allows
            for multiple key/value pair"""
        if kwargs:
            for key, value in kwargs.items():
                if key not in ['__class__']:
                    setattr(self, key, value)
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return (f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """ change updated_at to the current time now"""
        self.updated_at = datetime.now()

        from models import storage

        storage.new(self)
        storage.save()

    def to_dict(self):

        """a proper representation all object properties"""
        rep = self.__dict__
        rep["__class__"] = "BaseModel"
        rep["updated_at"] = self.updated_at.isoformat()
        rep["created_at"] = self.created_at.isoformat()
        return rep
