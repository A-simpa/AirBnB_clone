#!/usr/bin/python3
""" initializes the module models """
from models.engine.file_storage import FileStorage
from models.city import City
from models.state import State
from models.amenity import Amenity

storage = FileStorage()
storage.reload()
