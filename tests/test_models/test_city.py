#!/usr/bin/python3
""" testing for city """

from unittest import TestCase
from models.base_model import BaseModel
from models import City


class CityTestCase(TestCase):
    """tests the class City"""

    def test_name(self):
        """tests if name is a string"""
        self.assertIs(type(City.name), str)

    def test_state_id(self):
        """test if state id is string"""
        self.assertIs(type(City.state_id), str)
