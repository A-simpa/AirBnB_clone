#!/usr/bin/python3
""" definition of the base_model of console"""

import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """args allow multiple arguments while kwargs allows
            for multiple key/value pair"""

        if not kwargs:
            """if kwargs is not empty, each key of the
                dictionary is an attribute name"""

            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    DATE_TIME = datetime.strptime(str(datetime.now().isformat
                                  (timespec='microseconds')), BaseModel.DATE_TIME)

                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.strptime
            (str(datetime.now().isoformat
                 (timespec='microseconds')), BaseModel.DATE_TIME)
            self.updated_at = datetime.strptime
            (str(datetime.now().isoformat
                 (timespec='microseconds')), BaseModel.DATE_TIME)

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
