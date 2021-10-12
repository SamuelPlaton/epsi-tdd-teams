import unittest
from classes import Session

""" 
name : TestSession
description: Test the Generation of list
"""
class TestSession(unittest.TestCase):
    def setUp(self):
        self.session = Session()
