#!/usr/bin/python3
""" initializes the module models """
from models.engine.file_storage import FileStorage
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User

storage = FileStorage()
storage.reload()
