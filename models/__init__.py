#!/usr/bin/python3
""" initializes the module models """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
