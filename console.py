#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity

# constants for shell
class_names = [
    "BaseModel",
    "User",
    "State",
    "Place",
    "City",
    "Review",
    "Amenity"
]

storage = models.storage


class HBNBCommand(cmd.Cmd):
    """class for HNBN console"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program"
        return True

    def do_EOF(self, arg):
        """End of file"""
        return True

    def emptyline(self):
        return None

    def do_create(self, cls):
        """create an object of specified class"""
        if not cls:
            print("** class name missing **")
        elif cls in class_names:
            print(eval(f"{cls}")().id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ print the string representation of an object"""
        data = storage.all()
        line = (line.strip()).split()

        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in class_names:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif f"{line[0]}.{line[1]}" in data:
            print(data[f"{line[0]}.{line[1]}"])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """ remove an object from storage """
        line = (line.strip()).split()

        if len(line) == 0:
            print("** class name is missing **")
        elif line[0] not in class_names:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif f"{line[0]}.{line[1]}" in storage.all():
            del ((storage.all())[f"{line[0]}.{line[1]}"])
        else:
            print("** no instance found **")

    def do_all(self, line):
        """ print a list of all objects """
        line = (line.strip()).split()
        data = storage.all()
        all_object = []

        if len(line) == 0:
            for i in data:
                all_object.append(str(data[i]))
            print(all_object)
        elif line[0] in class_names:
            for i in data:
                if line[0] in i:
                    all_object.append(str(data[i]))
            print(all_object)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ updates the attributes of a class """
        line = (line.strip()).split()

        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in class_names:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        elif f"{line[0]}.{line[1]}" not in storage.all():
            print("** no instance found **")
        elif len(line) < 3:
            print("** attribute name missing **")
        elif len(line) < 4:
            print("** value missing **")
        else:
            cls, id, attr, val = line[0], line[1], line[2], line[3]
            statement = f"((storage.all())['{cls}.{id}']).{attr} = {val}"
            exec(statement)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
