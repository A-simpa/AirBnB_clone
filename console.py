#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys

import models
from models.base_model import BaseModel

class_names = ["BaseModel"]



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

    def do_create(self, argv):
        """create an object of argv"""
        if not argv:
            print("** class name is missing **")
        elif argv in class_names:
            print(eval(f"{argv}")().id)
        else:
            print("** class doesn't exist **")

    def do_show(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
