#!/usr/bin/python3

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
