#!/usr/bin/python3
""" testing for base_model """

from unittest import TestCase
from models.base_model import BaseModel


class BaseModelTestCases(TestCase):
    """ This class defines the test for the class BaseModel"""

    def test_instance(self):
        """ Test the creation of an instance of BaseModel"""
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_uniqid(self):
        """ test to see if id is unique """
        self.assertNotIn(BaseModel().id, [BaseModel().id, BaseModel().id])

    def test_idlen(self):
        """ test to see if length is 36 as per uuid4"""
        a = BaseModel()
        self.assertEqual(len(a.id), 36)

    def test_idtype(self):
        """ test if id is a string """
        a = BaseModel()
        self.assertIsInstance(a.id, str)

    def test_savemethod(self):
        """ testing the save method """
        a = BaseModel()
        b = BaseModel().updated_at
        a.save()
        c = BaseModel().updated_at
        self.assertNotEqual(b, c)

    def test_to_dict(self):
        """ test if to_dict works well """
        pass
