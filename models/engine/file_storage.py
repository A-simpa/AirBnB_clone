#!/usr/bin/python3
"""JSON representation of the data structure"""


import json as js
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns all objects """
        return self.__objects

    def new(self, obj):
        """ set a new obj"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """write(serialize) an object as a string to a json file"""
        with open(FileStorage.__file_path, "w") as f:
            store_object = {}
            for id, obj in FileStorage.__objects.items():
                store_object[id] = obj.to_dict()
            js.dump(store_object, f)

    def reload(self):
        """ deserialize json object in __file_path """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for obj in js.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
