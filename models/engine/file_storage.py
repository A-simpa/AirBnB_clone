#!/usr/bin/python3
"""JSON representation of the data structure"""


import json


class FileStorage:
    """serializes instances to a JSON file
        and deserializes JSON file to instances"""

    __path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        id = obj.id
        New = class_name + "." + id
        return New

    def save(self):
        with open(FileStorage.__path, 'w') as file:
            return json.dumps(file)

    def reload(self):
        if FileStorage.__path:
            with open(FileStorage.__path, 'r') as myfile:
                return json.loads(self, myfile)
