#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import sys


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
