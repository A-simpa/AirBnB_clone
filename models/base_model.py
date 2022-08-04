#!/usr/bin/python3
"""Airbnb clone"""


import uuid
from datetime import datetime
"""imported uuid to give random UUID"""


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = \
            str(datetime.now().isoformat(timespec='microseconds'))
        self.updated_at = \
            str(datetime.now().isoformat(timespec='microseconds'))

    def __str__(self):
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated
            current time"""
        return str(self.updated_at)

    def to_dict(self):
        """returns a dictionary containing all keys/values
            of __dict__ of the instance"""

        return self.__dict__


if __name__ == "__main__":
    main()
