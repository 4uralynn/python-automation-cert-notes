#!/usr/bin/env python3

import unittest
from raisingerrors import validate_user

class TestValidateUSer(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)
    
    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)
    #Behind  the scenes, this method is calling the function we want to test
    #and using a try-except block and checking that the expected error is raised



#Run the tests
unittest.main()
