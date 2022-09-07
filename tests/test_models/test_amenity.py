#!/usr/bin/python3
""" testing for amenity """

from unittest import TestCase
from models.base_model import BaseModel
from models import Amenity


class AmenityTestCase(TestCase):
    """tests the Amenity class"""
    def test_name(self):
        """testd if name is a string"""
        self.assertIs(type(Amenity.name), str)
