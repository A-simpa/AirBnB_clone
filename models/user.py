#!/usr/bin/python3
"""definition of the user class"""


class User(BaseModel):
    """this class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""


