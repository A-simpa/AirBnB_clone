#!/usr/bin/python3
"""Airbnb clone"""


import uuid
from datetime import datetime
"""imported uuid to give random UUID"""


class BaseModel:
    """defines all common attributes/methods for other classes"""



    def __init__(self, *args, **kwargs):
        """args allow multiple arguments while kwargs allows
            for multiple key/value pair"""

        if kwargs is not None:
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
        return ("[{}] ({}) {}".format
                (self.__class__.__name__,self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated
            current time"""
        return str(self.updated_at)

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of __dict__ of the instance"""

        new_dict = self.__dict__
        new_dict["__class__"] = self.__class__.__name__
        return new_dict


if __name__ == "__main__":
    main()
