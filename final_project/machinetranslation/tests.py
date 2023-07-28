import unittest
import sys

sys.path.insert(0, '..')

from translator import english_to_french
from translator import french_to_english
class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('hello'), 'bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('hello'), 'hello')
        

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english('bonjour'), 'hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')
        

unittest.main()
