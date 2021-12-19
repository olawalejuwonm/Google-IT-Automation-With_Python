from unittest.case import TestCase
from validations import validate_user

import unittest

class TestValidateUser(unittest.TestCase):
    def test_invalid_character(self):
        self.assertEqual(validate_user("invalid_user", 1), False)
    
    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "valid_user", -1)



unittest.main()