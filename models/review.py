#!/usr/bin/python3
"""definition of Review class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
