#!/usr/bin/python3
""" testing for review """

from unittest import TestCase
from models.base_model import BaseModel
from models import Review


class ReviewTestCase(TestCase):
    """tests the Review class"""
    def test_text(self):
        """test if place id is string"""
        self.assertIs(type(Review.text), str)

    def test_place_id(self):
        """test if place.id is correct"""
        self.assertIs(type(Review.place_id), str)

    def test_user_id(self):
        """tests if user id is correct"""
        self.assertIs(type(Review.user_id), str)
