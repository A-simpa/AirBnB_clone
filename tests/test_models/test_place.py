#!/usr/bin/python3
""" testing for base_model """

from unittest import TestCase
from models.base_model import BaseModel
from models import Place


class PlaceTestCase(TestCase):
    """testing class Place"""
    def test_city_id(self):
        """tests if city id is a string"""
        self.assertIs(type(Place.city_id), str)

    def test_user_id(self):
        """tests if user id is a string"""
        self.assertIs(type(Place.user_id), str)

    def test_name(self):
        """if name is string"""
        self.assertIs(type(Place.name), str)

    def test_description(self):
        """if description is a string"""
        self.assertIs(type(Place.description), str)

    def test_number_rooms(self):
        """if number_rooms is an int"""
        self.assertIs(type(Place.number_rooms), int)

    def test_number_bathrooms(self):
        """if number_bathrooms is an int"""
        self.assertIs(type(Place.number_bathrooms), int)

    def test_max_guest(self):
        """if max_guest is an int"""
        self.assertIs(type(Place.max_guest), int)

    def test_price_by_night(self):
        """if price by night is an int"""
        self.assertIs(type(Place.price_by_night), int)

    def test_latitude(self):
        """if latitude is a float"""
        self.assertIs(type(Place.latitude), float)

    def test_longitude(self):
        """if longitude is float"""
        self.assertIs(type(Place.longitude), float)

    def test_amenity_ids(self):
        """if amenity_ids is a list of strings"""
        self.assertIs(type(Place.amenity_ids), list)
