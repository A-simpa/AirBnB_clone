#!/usr/bin/python3
""" testing for User """

from unittest import TestCase
from models.base_model import BaseModel
from models import User


class UserTestCase(TestCase):
    """testing the User class"""
    def test_email(self):
        """tests if email is a string"""
        self.assertIs(type(User.email), str)

    def test_first_name(self):
        """tests if email is a string"""
        self.assertIs(type(User.first_name), str)

    def test_last_name(self):
        """tests if email is a string"""
        self.assertIs(type(User.last_name), str)

    def test_password(self):
        """tests if email is a string"""
        self.assertIs(type(User.password), str)

