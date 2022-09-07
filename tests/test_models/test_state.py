#!/usr/bin/python3
""" testing for state """

from unittest import TestCase
from models.base_model import BaseModel
from models import State


class StateTestCase(TestCase):
    """tests the State class"""

    def test_name(self):
        """test if name is string"""
        self.assertIs(type(State.name), str)
