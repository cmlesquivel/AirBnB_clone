#!/usr/bin/python3
"""Test"""
import unittest
import pep8


class test_Amenity(unittest.TestCase):
    """Class test full"""
    def test_pep8_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def Case_1(self):
        """Case 1"""
        amenity = Amenity()
        self.assertEqual(type(amenity.name), str)

if __name__ == '__main__':
    unittest.main()
