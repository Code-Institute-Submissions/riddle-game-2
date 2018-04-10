import unittest
import run

class TestRiddle(unittest.TestCase):
    # Test for checking if username already exists
    def test_check_username_already_exists(self):
        check1 = run.check_if_username_already_exists('tjasa')
        check2 = run.check_if_username_already_exists('hgfsjkdgf')
        self.assertEqual(check1, True)
        self.assertEqual(check2, False)