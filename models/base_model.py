#!/usr/bin/python3
""" definition of the base_model of console"""


from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime
import models

DATE_TIME = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """args allow multiple arguments while kwargs allows
            for multiple key/value pair"""

        if kwargs:
            """if kwargs is not empty, each key of the
                dictionary is an attribute name"""

            for key, value in kwargs.items():
                if key not in ['__class__']:
                    setattr(self, key, value)
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(datetime.now().isoformat(), DATE_TIME))

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return (f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        """ change updated_at to the current time now"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    def to_dict(self):

        """a proper representation all object properties"""
        rep = self.__dict__
        rep["__class__"] = "BaseModel"
        rep["updated_at"] = rep["updated_at"].isoformat()
        rep["created_at"] = rep["created_at"].isoformat()
        return rep
